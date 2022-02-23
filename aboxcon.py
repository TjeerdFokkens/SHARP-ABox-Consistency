import pyactr as actr
import Module1 as md1
import Module2 as md2
import Module3 as md3
import Module4 as md4
import Module5 as md5
import simpy
import re
import parser

def initial(learning=False):
    aBoxCon = actr.ACTRModel(
        automatic_visual_search=False,
        motor_prepared=True,
        subsymbolic=learning,
        utility_noise=0.2,
        partial_matching=False,
        utility_learning=learning,
        production_compilation=learning,
        activation_trace=True,
        retrieval_threshold=0,
        decay=0)

    aBoxCon.goals = {}
    aBoxCon.set_goal("g")
    aBoxCon.set_goal("imaginal")
    aBoxCon.set_goal("imaginal_action")

    actr.chunktype("goal", "state, form, count, mainconnective")
    actr.chunktype("proposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, derived")
    actr.chunktype("checklist", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
    actr.chunktype("storelist", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")
    actr.chunktype("universal_list", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9")
    actr.chunktype("count_order","number, successor, thing")

    aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="find_clash_to_head", form='none', count='0', mainconnective='none'))
    aBoxCon.goals["imaginal"].add(actr.makechunk(typename="checklist", thing="checklist", form="none", element="none", mainconnective="none", relation="none", subformula1="none", subformula2="none", form2="none", form3="none", form4="none", form5="none", form6="none", form7="none", form8="none"))

    for i in range(10):
        aBoxCon.decmem.add(actr.makechunk(typename="count_order", thing="count_order",number=str(i), successor=str(i+1)))
    return aBoxCon


aBoxCon = initial(False)
dm = aBoxCon.decmem

md1.module1(aBoxCon)
md2.module2(aBoxCon)
md3.module3(aBoxCon)
md4.module4(aBoxCon)
#md5.module5(aBoxCon)

parser.AddAboxFromFile("abox.txt",dm.add)

sim = aBoxCon.simulation(realtime=False,gui=False,trace=False)
lastfocusedform = None

while True:
    try:
        sim.step()
    except simpy.core.EmptySchedule:
        break
    #print(sim.current_event.action)
    #if re.match("^RULE FIRED:",sim.current_event.action):
       # print(sim.current_event.action)
    if re.match("^RULE FIRED:.*derived",sim.current_event.action):
        for x in aBoxCon.retrieval:
            print(str(round(sim.current_event.time,2)).ljust(7)[:7] + "DERIVED: *" + str(x.form))
    elif re.match("^RULE FIRED:.*found",sim.current_event.action):
        for x in aBoxCon.goals["imaginal"]:
            if (x.form != lastfocusedform) & (str(x.form) != "none"):
                print(str(round(sim.current_event.time,2)).ljust(7)[:7] +"FOCUS:   "+ str(x.form))
                lastfocusedform = x.form
    elif re.match("^KEY PRESSED: C",sim.current_event.action):
        print(str(round(sim.current_event.time,2)).ljust(7)[:7] +"INCONSISTENT")
    elif re.match("^KEY PRESSED: N",sim.current_event.action):
        print(str(round(sim.current_event.time,2)).ljust(7)[:7] +"CONSISTENT")    


print("DONE")