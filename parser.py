from lark import Lark, Transformer, Visitor, v_args
import pyactr as actr
import pprint
#import pprint

form_grammar = """

    ?start: assertion (","+ assertion)*

    ?assertion: element ":" out_concept             -> con_ass
        | "(" element "," element ")" ":" role      -> role_ass

    ?out_concept: atom
        | "-" atom                          -> neg
        | ["("] concept "&" concept [")"]   -> conj
        | ["("] concept "%" concept [")"]   -> dis
        | "/E" role "." concept             -> exists
        | "/A" role "." concept             -> universal

    ?concept: atom
        | "-" atom                      -> neg
        | "(" concept "&" concept ")"   -> conj
        | "(" concept "%" concept ")"   -> dis
        | "/E" role "." concept         -> exists
        | "/A" role "." concept         -> universal

    ?role: NAME                         -> role
    ?element : NAME                     -> element
    ?atom : NAME                        -> atom

    %import common.CNAME -> NAME
    %import common.WS_INLINE

    %ignore WS_INLINE
"""

@v_args(inline=True)    # Affects the signatures of the methods
class ToString(Transformer): # Transforms a tree recursively to a string
    role = str
    element = str
    atom = str
    conj = lambda self,ch1,ch2: "(" + ch1 + "&" + ch2 + ")"
    dis = lambda self,ch1,ch2: "(" + ch1 + "%" + ch2 + ")"
    exists = lambda self,role,con: "/E" + role + "." + con
    con_ass = lambda self,el,con: el + ":" + con
    role_ass = lambda self,elL,elR,role: "(" + elL + "," + elR + "):" + role
    neg = lambda self,con : "-" + con
    universal = lambda self,role,con: "/A" + role + "." + con

class SetOfElements(Visitor):
    def __init__(self,elements):
        self.elements=elements
    def element(self,tree):
        self.elements.add(str(tree.children[0]))

class CountNodes(Transformer):
    def __init__(self,name):
        self.name = name
    def __default__(self,data,children,meta):
        if data==self.name:
            return(sum(children)+1)
        else:
            return(sum(children))
    def __default_token__(self,data):
        return 0

class AddFormToAbox(Visitor): # Adds a formula together with all subformulas to the DM.

    def __init__(self,addtodm,elements, witnesses):
        self.derived="yes"
     #   self.insideuniversal=False
        #self.witness=1
        self.addtodm=addtodm
        self.elements=elements
        self.witnesses=witnesses

    def con_ass(self,tree):
        self.el=tree.children[0].children[0]

    def role_ass(self,tree):
        elL = tree.children[0].children[0]
        elR = tree.children[1].children[0]
        role = ToString().transform(tree.children[2])
        formstr = ToString().transform(tree)
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, concept="none", element=elL, mainconnective="relation",
            subformula1=elL, subformula2=elR, relation=role,
            derived=self.derived))
        self.derived="no"

    def conj(self,tree):
        constr = ToString().transform(tree)
        subconL = ToString().transform(tree.children[0])
        subconR = ToString().transform(tree.children[1])
        def addconj(el):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="conjunction",
                    subformula1=el + ":" + subconL, subformula2=el + ":" + subconR,
                    derived=self.derived))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                addconj(el)
        else:
            addconj(self.el)
        self.derived="no"

    # def dis(self,tree):
    #     constr = ToString().transform(tree)
    #     subconL = ToString().transform(tree.children[0])
    #     subconR = ToString().transform(tree.children[1])
    #     def adddisj(el):
    #         self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
    #                 form=el + ":" + constr, concept=constr, element=el, mainconnective="disjunction",
    #                 subformula1=el + ":" + subconL, subformula2=el + ":" + subconR,
    #                 derived=self.derived))
    #     if self.insideuniversal:
    #         for el in self.elements:
    #             adddisj(el)
    #     else:
    #         adddisj(self.el)
    #     self.derived="no"

    def exists(self,tree):
        constr = ToString().transform(tree)
        role = ToString().transform(tree.children[0])
        subcon = ToString().transform(tree.children[1])
        def addrole(e1,e2):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                form="(" + e1 +","+e2+"):"+role, concept="none", relation=role,
                mainconnective="relation", subformula1=e1, subformula2=e2,
                derived="no"))
        def addex(el,w):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="existential",
                    subformula1=w + ":" + subcon, subformula2="("+el+","+w+"):"+role,
                    derived=self.derived, relation=role))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                for w in self.witnesses:
                    addex(el,'foo')
                    addrole(el,w)
        else:
            for w in self.witnesses:
                addex(self.el,'foo')
                addrole(self.el,w)
        self.derived="no"

    def universal(self,tree):
        constr = ToString().transform(tree)
        role = ToString().transform(tree.children[0])
        subcon = ToString().transform(tree.children[1])
        def addun(el):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="universal",
                    subformula1=el + ":" + subcon, derived=self.derived, relation=role))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                addun(el)
        else:
            addun(self.el)
        self.derived="no"

    def neg(self,tree):
        constr = ToString().transform(tree)
        subcon = ToString().transform(tree.children[0])
        def addneg(el):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="negation",
                    subformula1=subcon, derived=self.derived))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                addneg(el)
        else:
            addneg(self.el)
        self.derived="no"

    def atom(self,tree):
        constr = ToString().transform(tree)
        def addatom(el):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="concept",
                    subformula1=constr, derived=self.derived))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                addatom(el)
        else:
            addatom(self.el)
        self.derived="no"

form_parser = Lark(form_grammar, parser='lalr')
parser = form_parser.parse

def AddAboxFromFile(filename,addtodm):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', ' ')
    abox = parser(data)
    witnesses=set()
    for i in range(1,1+max(CountNodes("role_ass").transform(abox),1)* CountNodes("exists").transform(abox)):
        witnesses.add("x"+str(i))
    elements=set()
    SetOfElements(elements).visit(abox)
    print(elements)
    print(witnesses)
    if abox.data in ["con_ass","role_ass"]:
        aboxlst = [abox]
    else:
        aboxlst=abox.children
    for form in aboxlst:
        addform = AddFormToAbox(addtodm,elements,witnesses)
        addform.visit_topdown(form) # Need to visit the tree top down to get the element first.

if __name__ == "__main__":
    import pyactr as actr
    aBoxCon = actr.ACTRModel()
    actr.chunktype("proposition", "thing, concept, form, element, mainconnective, relation, subformula1, subformula2, derived")
    dm = aBoxCon.decmem
    AddAboxFromFile("abox2.txt",dm.add)
    for a in dm:
        print (str(a[3][1]) + " :: " + str(a))
