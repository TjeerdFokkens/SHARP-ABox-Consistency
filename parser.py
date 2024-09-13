from lark import Lark, Transformer, Visitor, v_args
import pyactr as actr
import numpy as np

#The grammar of ALE ABoxes

form_grammar = """

    ?start: assertion (","+ assertion)*

    ?assertion: element ":" out_concept             -> con_ass
        | "(" element "," element ")" ":" role      -> role_ass

    ?out_concept: atom
        | "-" atom                          -> neg
        | ["("] concept "&" concept [")"]   -> conj
        | "/E" role "." concept             -> exists
        | "/A" role "." concept             -> universal

    ?concept: atom
        | "-" atom                      -> neg
        | "(" concept "&" concept ")"   -> conj
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

class AddFormToAbox(Visitor):
    #Adds a formula chunk to the declarative memory, together with all formula chunks that could possible be derived from it.
    #The functions below add the appropriate chunk for every type of formula.

    def __init__(self,addtodm,elements, witnesses):
        self.derived="yes"
        #self.insideuniversal=False
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
            derived=self.derived, subformula3='none'))
        self.derived="no"

    def conj(self,tree):
        constr = ToString().transform(tree)
        subconL = ToString().transform(tree.children[0])
        subconR = ToString().transform(tree.children[1])
        def addconj(el):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="conjunction",
                    subformula1=el + ":" + subconL, subformula2=el + ":" + subconR,
                    derived=self.derived, relation='none', subformula3='none'))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                addconj(el)
        else:
            addconj(self.el)
        self.derived="no"

    def exists(self,tree):
        constr = ToString().transform(tree)
        role = ToString().transform(tree.children[0])
        subcon = ToString().transform(tree.children[1])
        def addrole(e1,e2):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                form="(" + e1 +","+e2+"):"+role, concept="none", relation=role,
                mainconnective="relation", element=e1, subformula1=e1, subformula2=e2, subformula3='none',
                derived="no"))
        def addex(el,w):
            self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="existential",
                    subformula1=w + ":" + subcon, subformula2="("+el+","+w+"):"+role, subformula3=subcon,
                    derived=self.derived, relation=role))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                for w in self.witnesses:
                    addex(el,w)
                    addrole(el,w)
        else:
            for w in self.witnesses:
                addex(self.el,w)
                addrole(self.el,w)
        self.derived="no"

    def universal(self,tree):
        constr = ToString().transform(tree)
        role = ToString().transform(tree.children[0])
        subcon = ToString().transform(tree.children[1])
        def addun(el):
            self.addtodm(actr.makechunk(typename="uproposition", thing="uproposition",
                    form=el + ":" + constr, concept=constr, element=el, mainconnective="universal",
                    subformula1='none', subformula2=subcon, derived=self.derived, relation=role,
                    count=0, relation1='none', relation2='none', relation3='none', relation4='none',
                    relation5='none', relation6='none', relation7='none', relation8='none', relation9='none'))
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
                    subformula1=subcon, subformula2='none', derived=self.derived, relation='none', subformula3='none'))
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
                    subformula1=constr, subformula2='none', derived=self.derived, relation='none', subformula3='none'))
        if self.derived=="no":
            for el in self.elements.union(self.witnesses):
                addatom(el)
        else:
            addatom(self.el)
        self.derived="no"

form_parser = Lark(form_grammar, parser='lalr')
parser = form_parser.parse

def AddAboxFromFile(data,model_init):
    #This function takes an ABox and a model and then creates all necessary chunks from the ABox and adds them to the model.
    
    addtodm = model_init.decmem.add
    addtogoal = model_init.goals["g"].add
    addtoimaginal = model_init.goals["imaginal"].add

    addtoimaginal(actr.makechunk(typename="clash_list", thing="clash_list", concept="none", form="none", element="none", mainconnective="none", relation="none", subformula1="none", subformula2="none", form2="none", form3="none", form4="none", form5="none", form6="none", form7="none", form8="none", form9="none", form10="none", form11="none", form12="none", form13="none", form14="none", form15="none", form16="none"))

    for i in range(20):
        addtodm(actr.makechunk(typename="count_order", thing="count_order",number=str(i), successor=str(i+1)))

    #This calculates the number of witnesses necessary for expanding the ABox.
    #These elements are used for creating all the chunks necessary for expanding the ABox.
    abox = parser(data)
    witnesses=set()
    n = CountNodes("role_ass").transform(abox) + CountNodes("exists").transform(abox); # Number or role assertions + existential quantifiers
    m = CountNodes("universal").transform(abox) # Number of universal quantifiers
    f = np.ceil(n/(m+1))
    b = max(int(f**(m+2)-1),0,n)
    print('Number of witnesses: ',b)
    for i in range(1,b+1):
        witnesses.add("x"+str(i))
    elements=set()
    SetOfElements(elements).visit(abox)

    els = list(elements)
    def pick(li,ind):
        l = len(li)
        if ind<l:
            return li[ind]
        else:
            return 'none'
            #Fill the role_list chunk with all elements in the ABox and fill the rest of the role slots with 'none'-values.
    addtodm(actr.makechunk(typename="role_list", thing="role_list", role1=pick(els,0), role2=pick(els,1), role3=pick(els,2), role4=pick(els,3), role5=pick(els,4), role6=pick(els,5), role7=pick(els,6), role8=pick(els,7), role9=pick(els,8), role10=pick(els,9), role11=pick(els,10), role12=pick(els,11), role13=pick(els,12), role14=pick(els,13), role15=pick(els,14), role16=pick(els,15)))
    addtogoal(actr.makechunk(typename="goal", state="find_clash_to_head", form='none', count1=0, count2=1, mainconnective='none', role=pick(els,0), derivenew='yes'))

    if abox.data in ["con_ass","role_ass"]:
        aboxlst = [abox]
    else:
        aboxlst=abox.children
    #This loops through the formulas and adds the appropriate chunks to the model.
    for form in aboxlst:
        addform = AddFormToAbox(addtodm,elements,witnesses)
        addform.visit_topdown(form) # Need to visit the tree top down to get the element first.

if __name__ == "__main__":
    import pyactr as actr
    aBoxCon = actr.ACTRModel()
    actr.chunktype("proposition", "thing, concept, form, element, mainconnective, relation, subformula1, subformula2, subformula3, derived")
    dm = aBoxCon.decmem
    AddAboxFromFile("abox2.txt",dm.add)
    for a in dm:
        print (str(a[3][1]) + " :: " + str(a))
