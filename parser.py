from lark import Tree,Token,Lark, Transformer,Visitor, v_args
import pyactr as actr

aBoxCon = actr.ACTRModel(
    automatic_visual_search=False,
    motor_prepared=True,
 #   subsymbolic=True,
    utility_noise=0.2,
    partial_matching=False,
 #   utility_learning=True,
 #   production_compilation=True,
    activation_trace=True,
    retrieval_threshold=0,
    decay=0
)

aBoxCon.goals = {}
aBoxCon.set_goal("g")
aBoxCon.set_goal("imaginal")
aBoxCon.set_goal("imaginal_action")

actr.chunktype("goal", "state")
actr.chunktype("proposition", "thing, form, element, mainconnective, relation, subformula1, inferred1, subformula2, inferred2, derived")
actr.chunktype("checklist", "thing, form, element, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
actr.chunktype("storelist", "thing, form, element, mainconnective, relation, subformula1, subformula2, derived, inferred1, inferred2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")

dm = aBoxCon.decmem
goal = aBoxCon.goals["g"]
imaginal = aBoxCon.goals["imaginal"]
imaginal_action = aBoxCon.goals["imaginal_action"]
retrieval = aBoxCon.retrieval
production = aBoxCon.productions


form_grammar = """

    ?start: assertion (","+ assertion)*

    ?assertion: element ":" out_concept             -> con_ass
        | "(" element "," element ")" ":" role  -> role_ass

    ?out_concept: atom                            
        | "-" atom                          -> neg
        | ["("] concept "&" concept [")"]   -> conj
        | ["("] concept "%" concept [")"]   -> dis
        | "/E" role "." concept             -> exists
        | "/A" role "." concept             -> forall

    ?concept: atom                            
        | "-" atom                      -> neg
        | "(" concept "&" concept ")"   -> conj
        | "(" concept "%" concept ")"   -> dis
        | "/E" role "." concept         -> exists
        | "/A" role "." concept         -> forall

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
    con_ass = lambda self,el,con: el + ":" + con
    neg = lambda self,con : "-" + con

class AddFormToAbox(Visitor): # Adds a formula together with all subformulas to the DM. 

    def __init__(self):
        self.el=""
        self.derived="yes"

    def con_ass(self,tree):
        self.el=tree.children[0].children[0]

    def conj(self,tree):
        formstr = self.el + ":" + ToString().transform(tree)
        subformL = self.el + ":" + ToString().transform(tree.children[0])
        subformR = self.el + ":" + ToString().transform(tree.children[1])
        dm.add(actr.makechunk(typename="proposition", thing="proposition", 
            form=formstr, element=self.el, mainconnective="conjunction", 
            subformula1=subformL, subformula2=subformR, 
            derived=self.derived, inferred1="no", inferred2="no"))
        self.derived="no"

    def neg(self,tree):
        formstr = self.el + ":" + ToString().transform(tree)
        subform = ToString().transform(tree.children[0])
        dm.add(actr.makechunk(typename="proposition", thing="proposition", 
            form=formstr, element=self.el, mainconnective="negation", 
            subformula1=subform, derived=self.derived, inferred1="no"))
        self.derived="no"

    def atom(self,tree):
        formstr = self.el + ":" + ToString().transform(tree)
        subform = ToString().transform(tree)
        dm.add(actr.makechunk(typename="proposition", thing="proposition", 
            form=formstr, element=self.el, mainconnective="concept", 
            subformula1=subform, derived=self.derived, inferred1="no"))
        self.derived="no"

form_parser = Lark(form_grammar, parser='lalr')
parser = form_parser.parse

## Test of reading ABoxes from file:

with open('abox.txt', 'r') as file:
    data = file.read().replace('\n', ',') 
abox = parser(data)
if abox.data == "con_ass":
    aboxlst = [abox]
else:
    aboxlst=abox.children
for form in aboxlst:
    AddFormToAbox().visit_topdown(form) # Need to visit the tree top down to get the element first.
    print(ToString().transform(form))

print(dm)
