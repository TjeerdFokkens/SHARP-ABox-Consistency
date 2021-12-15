# A simple parser that takes formulas to be included in the ABox and *prints* all the actr commands that should be included. 
# Note:
# - Not sure if negation is treated as it should (as you do). 
# - It should be easy to change "print" to actually add the chunks to the dm
# - It should also be easy to expand for existential restriction, etc.
# - And to add the abox input as a file.
#
# Obs. This is my first try at coding python. Change and fix as you like.

from lark import Tree,Token,Lark, Transformer, v_args

calc_grammar = """
    ?start: element ":" out_concept   -> con_ass
        |   "(" element "," element ")" ":" role -> role_ass

    ?out_concept: atom                            
        | "-" atom              -> not
        | concept "&" concept   -> con
        | "(" concept "&" concept ")" -> con
        | concept "%" concept   -> dis
        | "(" concept "%" concept ")"   -> dis
        | "/E" role "." concept -> exists
        | "/A" role "." concept -> forall

    ?concept: atom                            
        | "-" atom              -> not
        | "(" concept "&" concept ")"   -> con
        | "(" concept "%" concept ")"   -> dis
        | "/E" role "." concept -> exists
        | "/A" role "." concept -> forall

    ?role: NAME                 -> role
    ?element : NAME             -> element
    ?atom : NAME                -> atom

    %import common.CNAME -> NAME
    %import common.WS_INLINE

    %ignore WS_INLINE
"""

form_parser = Lark(calc_grammar, parser='lalr')
parser = form_parser.parse

def TreeToString(form):
    if form.data == "con_ass":
        return(form.children[0].children[0] + ":" + TreeToString(form.children[1]))
    elif form.data == "con":
        return("(" + TreeToString(form.children[0]) + "&" + TreeToString(form.children[1])+ ")")
    elif form.data == "not":
        return("-" + TreeToString(form.children[0]))
    elif form.data == "atom":
        return(form.children[0])

def create_form_chunk(form,derived):
    if form.data == "con_ass":
        el=form.children[0].children[0]
        formtype=form.children[1].data
        subs=form.children[1].children
        if formtype == "atom":
            print('dm.add(actr.makechunk(typename="proposition", thing="proposition", form="'+TreeToString(form)+'", element="'+el+'", mainconnective="concept", subformula1="'+el+':'+subs[0]+'", derived="'+derived+'")')
        elif formtype == "not":
            print('dm.add(actr.makechunk(typename="proposition", thing="proposition", form="'+TreeToString(form)+'", element="'+el+'", mainconnective="negation", subformula1="'+el+':'+TreeToString(subs[0])+'", derived="'+derived+'", inferred1="no"))')        
        elif formtype == "con":
            print('dm.add(actr.makechunk(typename="proposition", thing="proposition", form="'+TreeToString(form)+'", element="'+el+'", mainconnective="conjunction", subformula1="'+el+':'+TreeToString(subs[0])+'", subformula2="'+el+':'+TreeToString(subs[1])+'", derived="'+derived+'", inferred1="no", inferred2="no"))')

def con_ass(el,concept):
    return(Tree("con_ass",[Tree('element', [Token('NAME', el)]),concept]))

def add_form_to_abox(form,derived="yes"):
    create_form_chunk(form,derived)
    if form.data == "con_ass":
        el=form.children[0].children[0]
        formtype=form.children[1].data
        subs=form.children[1].children
        if formtype == "not":
            create_form_chunk(con_ass(el,subs[0]),"no")
        elif formtype == "con":
            add_form_to_abox(con_ass(el,subs[0]),"no")
            add_form_to_abox(con_ass(el,subs[1]),"no")

for x in ["a : c", "a:-c", "b:-d&a", "b:-d & ((a&c) &b)"]:
    form=parser(x)
    print(TreeToString(form))
    add_form_to_abox(form)
