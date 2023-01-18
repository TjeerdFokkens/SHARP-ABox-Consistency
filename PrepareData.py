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
        utility_learning=False,
        production_compilation=learning,
        activation_trace=True,
        retrieval_threshold=-0.05,
        decay=0.005,
        instantaneous_noise=0.005,
        optimized_learning=False)

    aBoxCon.goals = {}
    aBoxCon.set_goal("g")
    aBoxCon.set_goal("imaginal")
    aBoxCon.set_goal("imaginal_action")

    actr.chunktype("goal", "state, form, count1, count2, mainconnective, role, derivenew")
    actr.chunktype("proposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, subformula3, derived")
    actr.chunktype("uproposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, derived, count, relation1, relation2, relation3, relation4, relation5, relation6, relation7, relation8, relation9")
    actr.chunktype("checklist", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15, form16, form17, form18")
    actr.chunktype("storelist", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15, form16, form17, form18 form19, form20, form21, form22, form23, form24, form25, form26, form27, form28, form29, form30, form31, form32, form33, form34, form35, form36, form37, form38, form39, form40")
    actr.chunktype("universal_list", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9")
    actr.chunktype("count_order","number, successor, thing")
    actr.chunktype("role_list", "thing, role1, role2, role3, role4, role5, role6, role7, role8, role9, role10, role11, role12, role13, role14, role15, role16")

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
        #print(sim.current_event)
        if sim.current_event.proc=='manual' and sim.current_event.action.startswith('KEY'):
            judgement = str(sim.current_event).split('KEY PRESSED: ')[1][0]
        if sim.current_event.action.startswith('RULE SELECTED: Module 2, Unit 3') or sim.current_event.action.startswith('RULE SELECTED: Module 2, Unit 5a') or sim.current_event.action.startswith('RULE SELECTED: Module 2, Unit 6a') or sim.current_event.action.startswith('RULE SELECTED: Module 5, Unit 2a'):
            a = str(mod.retrieval)
            b = a.split('form= ',1)[1].split(', ',1)[0]
            print(b)
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
                run = '|'
                for j in prove_tracks:
                    run = run + ' -> ' + j
            else:
                time = sim.current_event.time
                print('Simulation stopped prematurely. Some rule does not fire')
                if str(mod.goals['g']).split('state= ')[1].startswith('label_role'):
                    print('Probably not enough role witnesses.')
                print(mod.decmem)
                print(mod.goals['g'])
                judgement = 'Fail'
                run = '|'
                for j in prove_tracks:
                    run = run + ' -> ' + j
            break
    return run, time, judgement

def result_it(iterations, abox):
    #Takes the number of iteration and the Abox it's working with.
    #Returns a Dataframe with the results.
    df = pd.DataFrame(columns=['ABox', 'Run', 'Time', 'Judgement'])
    for i in range(iterations):
        run, time, judgement = result(abox)
        df2 = pd.DataFrame([[abox,run,time,judgement]],columns=['ABox', 'Run', 'Time', 'Judgement'])
        df = df.append(df2, ignore_index=True)
    return df

def result_aboxes(iterations, aboxes):
    #Takes the number of iterations and a list of ABoxes.
    #Returns a DataFrame with the simulation times and judgements, categorised by ABox and run.
    dat = pd.DataFrame(columns=['ABox', 'Run', 'Time', 'Judgement'])
    for abox in aboxes:
        dat = dat.append(result_it(iterations, abox), ignore_index=True)
    return dat


aboxes1 = ['a:A,b:-A,a:B', 'a:A,a:-A,a:B', 'a:A,b:-A,b:B', 'a:A,a:-A,b:B'] #tests dependence on element name

aboxes2 = ['a:/Er.A,a:/Ar.-A,a:/Er.B', 'a:/Er.A,a:/Ar.-A,a:/Es.B', 'a:/Er.A,a:/Ar.-A,a:/Ar.B', 'a:/Er.A,a:/Ar.-A,a:/As.B',
        'a:/Er.A,a:/As.-A,a:/Er.B', 'a:/Er.A,a:/As.-A,a:/Es.B', 'a:/Er.A,a:/As.-A,a:/Ar.B', 'a:/Er.A,a:/As.-A,a:/As.B'] #tests dependence on role name

aboxes3 = ['a:A,b:A,a:-A', 'a:A,b:B,a:-A', 'a:A,b:A,a:-B', 'a:A,b:B,a:-B'] #tests dependence on concept name

aboxes4 = ['a:(A&B),a:C','a:C,a:(A&B)','a:(A&B),a:-A','a:-A,a:(A&B)'] #tests dependence on order of formulas

aboxes5 = ['a:(A&B),a:B','a:(B&A),a:B','a:(A&B),a:-B','a:(B&A),a:-B'] #tests dependence on order of conjuncts

aboxes6 = ['a:((A&-A)&(B&C))','a:((A&B)&(-A&C))','a:(A&(-A&(B&C)))','a:(A&(B&(-A&C)))','a:(B&(A&(-A&C)))','a:(B&(C&(-A&A)))'] #tests the dependence of nesting

aboxes7 = ['a:(/Er.A&/Er.B)','a:((/Er.A&/Er.B)&/Ar.(/Er.A&/Er.B))','a:((/Er.A&/Er.B)&/Ar.((/Er.A&/Er.B)&/Ar.(/Er.A&/Er.B)))'] #tests the performance with AND-branching
aboxes7b = ['a:(/Er.(/Er.A&/Er.B)&/Er.B)','a:((/Er.A&/Er.B)&/Ar.(/Er.(/Er.A&/Er.B)&/Er.B))']

aboxes8 = ['a:(A&(B&(C&(D&-A))))','a:(A&B),a:(B&C),a:(C&D),a:(D&-A)'] #tests the spreading effect

aboxes9 = ['a:A,a:B','a:-A,a:-B','a:(A&B)','a:(-A&-B)','a:/Er.A','a:/Er.-A'] #tests negation indifference

aboxes10 = ['a:(A&B),a:(B&C),a:(C&F),a:(F&-A)']

testset = ['a:A, a:-A',
'a:(-C&A), a:(B&-A)',
'a:(/Er.A&/Er.-A), b:(B&C)',
'a:-A, (c,b):r, (b,a):s, c:/Ar.(/As.A&-B)',
'a:A, (b,a):r, b:/Ar.((-A&-B)&-C),c:(B&-B)',
'b:/Er.(-B&A), b:/Ar.-A, a:/As.B',
'a:-A, (b,a):r, b:(/Ar.A&B), c:/Es.(B&A)',
'a:A, (b,a):r, b:(B&/Ar.-A), b:(/Es.B&C)',
'a:(C&A), a:(B&D)',
'a:(/Er.A&/Es.-A)',
'b:/Ar./Es.-A, (b,c):r, c:/As.-E',
'a:A, (c,b):r, (b,a):s, c:/Ar./As.-B',
'a:A, (b,a):r, b:/Ar.((-D&B)&-C)',
'b:/Er.(B&C), b:/Ar.A',
'a:-A, (b,a):r, b:(/Ar.-A&B)',
'a:A, (d,c):r, (c,b):s, (b,a):t, d:/Ar./As./At.E, b:(B&C)']


testset2 = [
'a:A, b:-A, a:-B',
'a:/Er./As./Er./At.-A',
'a:A, a:-A, b:/Ar.A',
'a:(A&(-B&(C&D))), a:D',
'a:/Ar./Es./Er.-A, b:/As.-B',
'a:(A&-B), b:(-C&-D), a:-C',
'a:/Ar./Es.(-A&-B), b:-A, c:-B',
'a:/Er.A, a:/Ar.-A, b:/As.(B&A)',
'a:/Er./Es.-A, a:/Ar./As.A, b:/Es.-B',
'a:-A, a:-B, b:-C, b:-A, c:-A, c:B',
'a:/Ar./As./Es.-A, (a,b):r, b:/Es./As.A',
'a:/Er.(A&(B&-A)), b:/Ar./Es./Et.(B&-C)',
'b:-D, (a,b):r, a:/Es.(-A&(-B&(-C&D)))',
'a:/Ar./Es.-B, b:/As.(-A&(-C&B)), (a,b):r',
'a:/Ar./Es.-B, (a,b):r, b:/As.B, a:-A, b:B',
'a:/Er.A, a:/Ar.-A, b:/Es.B, b:/As.A, (b,a):s',
'a:/Er.-A, a:/Ar.(A&-B), b:/Er.-B, a:-C, a:-B',
'a:(-A&(B&-C)), b:(-B&(C&A)), b:(A&C), a:B',
'a:/Ar./As.(A&-B), (a,b):r, (b,c):s, c:A, b:B',
'a:/Ar./Es./At.-B, b:(-C&/Er.(-B&A)), c:/Es./Et.B',
'a:/Ar./Es./Et.(-A&B), (a,b):r, b:/As./At.(-B&-C)',
'a:(A&-B), b:(C&-A), a:(-B&(C&-A)), b:(C&(D&B))',
'a:/Ar./Er./As.-A, (a,b):r, b:/Ar./Es.(-B&(-D&(-C&A)))',
'a:/Ar./Er./Es./Et.(-A&(-C&(-B&(-D&(-E&A))))), (a,b):r',
'a:/Ar.(A&(B&-C)), (a,c):r, c:(-B&-C), b:-A, b:/Er.A',
'a:/Ar.(A&-B), b:/Er.(A&(B&C)), c:(A&B), (b,c):s, (c,d):r',
'a:/Er.(A&-B), b:/As./Et.-C, c:/Ar.(B&-A), b:(C&-D), (a,b):s',
'a:/Ar.(/As.-A&B), (a,b):r, b:/Es.(A&B), b:/Ar.(-A&(B&/As.A))',
'a:/Ar./As.(A&-B), (a,b):r, (b,c):s, c:B, b:/Er./Er.(A&B), b:/As.B',
'a:/As.(-A&B), (b,a):r, b:/Ar./Es.(A&B), c:(-B&C), a:(B&-C), (b,c):s']



aboxesorder = ['a:(A&(B&C)),a:(D&(E&-C))','a:/Er.(A&B),a:(C&/Ar.-A)']

test_linear = ['a:A', 'a:A, b:B', 'a:A, b:B, c:C', 'a:A, b:B, c:C, d:D', 'a:A, b:B, c:C, d:D, e:E']
test_polynomial = ['a:A', 'a:A, (a,b):r, a:/Ar.B', 'a:A, (a,b):r, (a,c):r, a:/Ar.B, a:/Ar.C', 'a:A, (a,b):r, (a,c):r, (a,d):r, a:/Ar.B, a:/Ar.C, a:/Ar.D', 'a:A, (a,b):r, (a,c):r, (a,d):r, (a,e):r, a:/Ar.B, a:/Ar.C, a:/Ar.D, a:/Ar.E']

a = result_aboxes(10, [test_polynomial[4]])

#a.to_csv('/Users/xfoktj/Documents/GitHub/ABox-Consistency/data/data19.csv', mode='a', index=True, header=False)
#a.to_csv('/Users/xfoktj/Documents/GitHub/ABox-Consistency/data/data22.csv',index_label='Index')
