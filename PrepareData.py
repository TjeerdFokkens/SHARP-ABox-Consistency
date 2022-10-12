import pyactr as actr
import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import Module1 as md1
import Module2 as md2
import Module3 as md3
import Module4 as md4
import Module5 as md5
import parser as par
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import re
from matplotlib.ticker import MaxNLocator
from collections import Counter
from scipy import stats
from lark import Lark, Transformer, Visitor, v_args
import pprint

def model(abox, learning=False):
    #This function takes an ABox.
    #It initialises the model and loads the ABox to the memory.
    aBoxCon = actr.ACTRModel(
        automatic_visual_search=False,
        motor_prepared=True,
        subsymbolic=learning,
        utility_noise=0.2,
        partial_matching=False,
        utility_learning=learning,
        production_compilation=learning,
        activation_trace=True,
        retrieval_threshold=-0.05,
        decay=0.005,
        instantaneous_noise=0.005)

    aBoxCon.goals = {}
    aBoxCon.set_goal("g")
    aBoxCon.set_goal("imaginal")
    aBoxCon.set_goal("imaginal_action")

    actr.chunktype("goal", "state, form, count1, count2, mainconnective, role, derivenew")
    actr.chunktype("proposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, subformula3, derived")
    actr.chunktype("uproposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, derived, count, relation1, relation2, relation3, relation4, relation5, relation6, relation7, relation8, relation9")
    actr.chunktype("checklist", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15, form16")
    actr.chunktype("storelist", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15, form16, form17, form18 form19, form20")
    actr.chunktype("universal_list", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9")
    actr.chunktype("count_order","number, successor, thing")
    actr.chunktype("role_list", "thing, role1, role2, role3, role4, role5, role6, role7, role8, role9, role10")

    aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="find_clash_to_head", form='none', count1=0, count2=1, mainconnective='none', role='none', derivenew='yes'))

    md1.module1(aBoxCon)
    md2.module2(aBoxCon)
    md3.module3(aBoxCon)
    md4.module4(aBoxCon)
    md5.module5(aBoxCon)

    par.AddAboxFromFile(abox,aBoxCon)
    return aBoxCon

def result(abox):
    #Takes an abox.
    #Returns a list with the formulas inspected and the simulation time.
    prove_tracks = []
    mod = model(abox, learning=True)
    sim = mod.simulation(realtime=False,gui=False)
    sim.step()
    while True:
        if sim.current_event.proc=='manual' and sim.current_event.action.startswith('KEY'):
            judgement = str(sim.current_event).split('KEY PRESSED: ')[1][0]
        if sim.current_event.action.startswith('RULE SELECTED: Module 2, Unit 3') or sim.current_event.action.startswith('RULE SELECTED: Module 2, Unit 5a') or sim.current_event.action.startswith('RULE SELECTED: Module 2, Unit 6a'):
            print('')
            a = str(mod.retrieval)
            b = a.split('form= ',1)[1].split(', ',1)[0]
            prove_tracks.append(b)
        try:
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            sim.step()
            sys.stdout = old_stdout
        except:
            sys.stdout = old_stdout
            goalstate = str(mod.goals['g']).split('state= ')[1].split(')')[0]
            if goalstate=='stop':
                time = sim.current_event.time
                print('End of simulation,', time)
                run = ''
                for j in prove_tracks:
                    run = run + ' -> ' + j
                #judgement = mod.utilities
                #print(judgement)
            else:
                time = 0
                print('Simulation stopped prematurely. Some rule does not fire')
                print(mod.decmem)
            break
    return run, time, judgement

def result_it(iterations, abox):
    #Takes the number of iteration and the Abox it's working with.
    #Returns a Dataframe with the results.
    dictionary = {}
    for i in range(iterations):
        run, time, judgement = result(abox)
        try:
            dictionary[str(abox+' '+run)].append((time,judgement))
        except:
            dictionary[str(abox+' '+run)] = [(time,judgement)]
    for i in dictionary.keys():
        dictionary[i] = pd.Series(dictionary[i])
    df = pd.DataFrame(dictionary)
    return df

def result_aboxes(iterations, aboxes):
    #Takes the number of iterations and a list of ABoxes.
    #Returns a DataFrame with the simulation times and judgements, categorised by ABox and run.
    j=0
    for abox in aboxes:
        if j>0:
            dat = dat.join(result_it(iterations, abox))
        else:
            dat = result_it(iterations, abox)
            j+=1
    return dat


aboxes_branch = ['a:(/Er.A&/Er.B)','b:((/Er.A&/Er.B)&/Ar.(/Er.A&/Er.B))','c:((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.(/Er.A&/Er.B)))','d:((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.(/Er.A&/Er.B))))','e:((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.(/Er.A&/Er.B)))))']


#print(result_aboxes(10, ['a:(/Er.A&/Er.B)']))
