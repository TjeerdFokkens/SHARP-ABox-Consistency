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
from matplotlib.ticker import MaxNLocator
from collections import Counter

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

def trace(mod, buffer, action=''):
    #Takes a simulation, a buffer and possibly an action.
    #Returns the latest event time, i.e. the simulation time.
    sim = mod.simulation(realtime=False,gui=False)
    sim.step()
    while True:
        if sim.current_event.proc==buffer and sim.current_event.action.startswith(action):
            print(sim.current_event)
            #mod.decmem.add(actr.makechunk(typename="test", thing="test")) Here some arbitrary chunks can be added to the dm.
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
    #Takes the number of simulations and the Abox it's working with.
    #Returns a list with simulation times.
    sim_time_list = []
    for i in range(it):
        #Simulation is initialised.
        aBoxCon = initial(True)
        dm = aBoxCon.decmem

        md1.module1(aBoxCon)
        md2.module2(aBoxCon)
        md3.module3(aBoxCon)
        md4.module4(aBoxCon)

        par.AddAboxFromFile(abox,dm.add)

        #Simulation is executed and the simulation time is appended to a list.
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        outp = trace(aBoxCon, 'PROCEDURAL')
        sys.stdout = old_stdout
        sim_time_list.append(outp)
    return sim_time_list

def simulation_plot(iterations, abox, desired_bin_size):
    #Takes the number of simulations, the abox it's working with and the desired size of the bins in the plot.
    #It returns a plot with the desired criteria using the results of the simulations.
    data = plot_list(iterations, abox)
    print(data)
    bins = compute_histogram_bins(data, desired_bin_size)
    min_val = bins[0]
    max_val = bins[-1]

    fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, tight_layout=True, sharex=True)

    ax1.grid(visible=None, axis='x')
    ax1.grid(linestyle=':', axis='y')
    ax1.set(xticks=np.arange(min_val-desired_bin_size, max_val+2*desired_bin_size, desired_bin_size))
    ax1.set_title('Simulated time of inference')
    ax1.hist(data, bins=bins, color='forestgreen', linewidth=0.5, edgecolor="white")
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

    timeintervals, linelengths, offsets = compute_line_lengths(data)

    ax2.eventplot(timeintervals, orientation="horizontal", linewidth=1, color='forestgreen', linelengths = linelengths, lineoffsets = offsets)
    ax2.get_yaxis().set_visible(False)
    ax2.grid(linestyle=':', axis='x')
    ax2.set_xlabel('time (s)')

def compute_line_lengths(data):
    #The different data points prepared in an array for the plot.
    total = len(data)
    di = dict((i, data.count(i)) for i in data)
    di2 = list(di.keys())
    timeintervals = np.array([[el] for el in di])
    #The corresponding length of the lines.
    l = []
    for i in di2:
        num = di[i]
        l.append(num)
    linelengths = [element/total*len(timeintervals) for element in l]
    #The offsets such that the eventlines are aligned.
    offsets = [ 0 for el in linelengths]
    return timeintervals, linelengths, offsets

def compute_histogram_bins(data, desired_bin_size):
    #Takes a list with the simulation times and the desired bin size.
    #Returns the boundaries of the bins in a list.
    min_val = min(data)
    max_val = max(data)
    min_boundary = np.round(np.floor(min_val/desired_bin_size)*desired_bin_size,1)
    max_boundary = np.round(np.ceil(max_val/desired_bin_size)*desired_bin_size,1)
    n_bins = int(round((max_boundary - min_boundary) / desired_bin_size,0))
    bins = np.linspace(min_boundary, max_boundary, n_bins+1)
    return bins

'''
simulation_plot(8, "abox2.txt", 0.2)

plt.show()

'''
aBoxCon = initial(learning=True)
dm = aBoxCon.decmem
md1.module1(aBoxCon)
md2.module2(aBoxCon)
md3.module3(aBoxCon)
md4.module4(aBoxCon)

par.AddAboxFromFile("abox2.txt",dm.add)
print(dm)
#aBoxCon_sim = aBoxCon.simulation(realtime=False,gui=False)
trace(aBoxCon, 'PROCEDURAL', action='RULE SELECTED')
print(aBoxCon.goals["g"])
print(aBoxCon.goals["imaginal"])
print(aBoxCon.goals["imaginal_action"])
print(aBoxCon.retrieval)
print(dm)
