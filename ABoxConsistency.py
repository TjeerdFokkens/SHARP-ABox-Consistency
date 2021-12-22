import pyactr as actr
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import ProductionRules as prls
import parser as par
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
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
        activation_trace=False,
        retrieval_threshold=0,
        decay=0)

    aBoxCon.goals = {}
    aBoxCon.set_goal("g")
    aBoxCon.set_goal("imaginal")
    aBoxCon.set_goal("imaginal_action")

    actr.chunktype("goal", "state")
    actr.chunktype("proposition", "thing, form, element, mainconnective, relation, subformula1, inferred1, subformula2, inferred2, derived")
    actr.chunktype("checklist", "thing, form, element, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
    actr.chunktype("storelist", "thing, form, element, mainconnective, relation, subformula1, subformula2, derived, inferred1, inferred2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")

    aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="start"))
    aBoxCon.goals["imaginal"].add(actr.makechunk(typename="checklist", thing="checklist"))
    return aBoxCon

def trace(sim, buffer, action=''):
    sim.step()
    while True:
        if sim.current_event.proc==buffer and sim.current_event.action.startswith(action):
            print(sim.current_event)
        try:
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            sim.step()
            sys.stdout = old_stdout
        except:
            sys.stdout = old_stdout
            print('End of simulation,', sim.current_event.time)
            break
    return sim.current_event.time

def plot_list(it):
    sim_time_list = []
    for i in range(it):
        aBoxCon = initial(True)
        dm = aBoxCon.decmem

        prls.module1(aBoxCon)
        prls.module2(aBoxCon)
        prls.module3(aBoxCon)
        prls.module4(aBoxCon)

        par.AddAboxFromFile("abox.txt",dm.add)

        aBoxCon_sim = aBoxCon.simulation(realtime=False,gui=False)

        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        outp = trace(aBoxCon_sim, 'PROCEDURAL')
        sys.stdout = old_stdout
        sim_time_list.append(outp)
    return sim_time_list

def simulation_plot(iterations):
    data = plot_list(iterations)
    fig, ax = plt.subplots(tight_layout=True)
    hist = ax.hist(data)


#simulation_plot(10)

#plt.show()

aBoxCon = initial(True)
dm = aBoxCon.decmem

module1(aBoxCon)
module2(aBoxCon)
module3(aBoxCon)
module4(aBoxCon)

parser.AddAboxFromFile("abox.txt",dm.add)

sim = aBoxCon.simulation(realtime=False,gui=False,trace=False)
lastfocusedform = None

while True:
    try:
        sim.step()
    except simpy.core.EmptySchedule:
        break
   # print("*" + str(sim.current_event.action))
    if re.match("^RULE FIRED:.*derived",sim.current_event.action):
        for x in aBoxCon.retrieval:
            print(str(round(sim.current_event.time,2)).ljust(7)[:7] + "DERIVED: *" + str(x.form))
    elif re.match("^RULE FIRED:.*found",sim.current_event.action):
        #print(sim.current_event.action)
        for x in aBoxCon.goals["imaginal"]:
            if (x.form != lastfocusedform) & (str(x.form) != "none"):
                print(str(round(sim.current_event.time,2)).ljust(7)[:7] +"FOCUS:   "+ str(x.form))
                lastfocusedform = x.form


print("DONE")


