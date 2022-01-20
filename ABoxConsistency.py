import pyactr as actr
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
#import ProductionRules as prls
import Module1 as md1
import Module2 as md2
import Module3 as md3
import Module4 as md4
import parser as par
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import re

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

    actr.chunktype("goal", "state, form")
    actr.chunktype("proposition", "thing, form, element, mainconnective, relation, subformula1, subformula2, derived")
    actr.chunktype("checklist", "thing, form, element, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
    actr.chunktype("storelist", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")

    aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="find_clash_to_head", form='none'))
    aBoxCon.goals["imaginal"].add(actr.makechunk(typename="checklist", thing="checklist", form="none", element="none", mainconnective="none", relation="none", subformula1="none", subformula2="none", form2="none", form3="none", form4="none", form5="none", form6="none", form7="none", form8="none"))
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

def plot_list(it, abox):
    sim_time_list = []
    for i in range(it):
        aBoxCon = initial(True)
        dm = aBoxCon.decmem

        md1.module1(aBoxCon)
        md2.module2(aBoxCon)
        md3.module3(aBoxCon)
        md4.module4(aBoxCon)

        par.AddAboxFromFile(abox,dm.add)

        aBoxCon_sim = aBoxCon.simulation(realtime=False,gui=False)

        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        outp = trace(aBoxCon_sim, 'PROCEDURAL')
        sys.stdout = old_stdout
        sim_time_list.append(outp)
    return sim_time_list

def simulation_plot(iterations, abox):
    data = plot_list(iterations, abox)
    fig, ax = plt.subplots(tight_layout=True)
    ax.grid(visible=None, axis='x')
    ax.grid(linestyle=':', axis='y')
    bins = compute_histogram_bins(plot_list(iterations, abox),0.1)
    hist = ax.hist(data, bins=bins, color='forestgreen', label='time')

def compute_histogram_bins(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    min_boundary = -1.0 * (min_val % desired_bin_size - min_val)
    max_boundary = max_val - max_val % desired_bin_size + desired_bin_size
    n_bins = int((max_boundary - min_boundary) / desired_bin_size) + 1
    bins = np.linspace(min_boundary, max_boundary, n_bins)
    return bins


#simulation_plot(50, "abox.txt")

#plt.show()


aBoxCon = initial(True)
dm = aBoxCon.decmem
md1.module1(aBoxCon)
md2.module2(aBoxCon)
md3.module3(aBoxCon)
md4.module4(aBoxCon)

par.AddAboxFromFile("abox.txt",dm.add)

aBoxCon_sim = aBoxCon.simulation(realtime=False,gui=False)
trace(aBoxCon_sim, 'PROCEDURAL')
