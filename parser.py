from lark import Lark, Transformer, Visitor, v_args
import pyactr as actr
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

class AddFormToAbox(Visitor): # Adds a formula together with all subformulas to the DM.

    def __init__(self,addtodm):
        self.derived="yes"
        self.witness=1
        self.universals={}
        self.constants={}
        self.addtodm=addtodm

    def con_ass(self,tree):
        self.el=tree.children[0].children[0]

    def role_ass(self,tree):
        elL = tree.children[0].children[0]
        elR = tree.children[1].children[0]
        role = ToString().transform(tree.children[2])
        formstr = ToString().transform(tree)
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, element=elL, mainconnective="relation",
            subformula1=elL, subformula2=elR, relation=role,
            derived=self.derived))
        self.derived="no"

    def conj(self,tree):
        conceptstr = ToString().transform(tree)
        formstr = self.el + ":" + conceptstr
        subformL = self.el + ":" + ToString().transform(tree.children[0])
        subformR = self.el + ":" + ToString().transform(tree.children[1])
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, concept=conceptstr, element=self.el, mainconnective="conjunction",
            subformula1=subformL, subformula2=subformR,
            derived=self.derived))
        self.derived="no"

    def dis(self,tree):
        conceptstr = ToString().transform(tree)
        formstr = self.el + ":" + conceptstr
        subformL = self.el + ":" + ToString().transform(tree.children[0])
        subformR = self.el + ":" + ToString().transform(tree.children[1])
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, concept=conceptstr, element=self.el, mainconnective="disjunction",
            subformula1=subformL, subformula2=subformR,
            derived=self.derived))
        self.derived="no"

    def exists(self,tree):
        conceptstr = ToString().transform(tree)
        formstr = self.el + ":" + conceptstr
        witness = "X" + str(self.witness)
        self.witness=self.witness+1
        subform = witness + ":" + ToString().transform(tree.children[1])
        role = ToString().transform(tree.children[0])
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, concept=conceptstr, element=self.el, mainconnective="existential",
            subformula1=subform, subformula2="("+self.el +","+witness+"):"+role,
            derived=self.derived))
        self.derived="no"
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form="("+self.el +","+witness+"):"+role, relation=role,
            mainconnective="relation", subformula1=self.el, subformula2=witness,
            derived=self.derived))
        self.el = witness

    def universal(self,tree): #This function needs to be updated.
        conceptstr = ToString().transform(tree)        
        formstr = self.el + ":" + conceptstr
        subform = self.el + ":" + ToString().transform(tree.children[1])
        role = ToString().transform(tree.children[0])
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, concept=conceptstr, element=self.el, mainconnective="universal",
            subformula1=subform, derived=self.derived))
        self.derived="no"

    def neg(self,tree):
        conceptstr = ToString().transform(tree)        
        formstr = self.el + ":" + conceptstr
        subform = ToString().transform(tree.children[0])
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, concept=conceptstr, element=self.el, mainconnective="negation",
            subformula1=subform, derived=self.derived))
        self.derived="no"

    def atom(self,tree):
        formstr = self.el + ":" + ToString().transform(tree)
        subform = ToString().transform(tree)
        self.addtodm(actr.makechunk(typename="proposition", thing="proposition",
            form=formstr, element=self.el, mainconnective="concept",
            subformula1=subform, derived=self.derived))
        self.derived="no"

form_parser = Lark(form_grammar, parser='lalr')
parser = form_parser.parse

def AddAboxFromFile(filename,addtodm):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', ' ')
    abox = parser(data)
    if abox.data in ["con_ass","role_ass"]:
        aboxlst = [abox]
    else:
        aboxlst=abox.children
    for form in aboxlst:
        addform = AddFormToAbox(addtodm)
        addform.visit_topdown(form) # Need to visit the tree top down to get the element first.

if __name__ == "__main__":
    import pyactr as actr
    aBoxCon = actr.ACTRModel()
    actr.chunktype("proposition", "thing, concept, form, element, mainconnective, relation, subformula1, subformula2, derived")
    dm = aBoxCon.decmem
    AddAboxFromFile("abox.txt",dm.add)
    print(dm)
