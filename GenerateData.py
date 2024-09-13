import pyactr as actr
import pandas as pd
import sys
import os
import Component1 as cp1
import Component2 as cp2
import Component3 as cp3
import Component4 as cp4
import Component5 as cp5
import parser as par
from lark import Lark, Transformer, Visitor, v_args


def model(abox, learning=False):
    #This function takes an ABox.
    #It initialises SHARP by:
    #    setting the sub-symbolic parameters
    #    defining the buffers
    #    defining the chunk types (find explanations of the chunktypes below)
    #    loading the goal buffer with the starting chunk
    #    loading the production rules into the procedural memory
    #    loading all chunks relevant for processing the input ABox into the declarative memory using the AddAboxFromFile-function.
    #It outputs the model.
    
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

    #In the following chunktypes, the 'thing' slot is used to differentiate the chunktypes in the production rules.
    #This chunktype contains information regarding the planning of solving the ABox consistency problem.
    actr.chunktype("goal", "state, form, count1, count2, mainconnective, role, derivenew")
    #This chunktype represents a formula in the description logic ALE which is of any type except a universal restriction.
    actr.chunktype("proposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, subformula3, derived")
    #This chunktype represents a universal restriction formula; it has a list of role/relation formulas to keep track of which inferences have been made (so that the same inference step is not made twice).
    actr.chunktype("uproposition", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, derived, count, relation1, relation2, relation3, relation4, relation5, relation6, relation7, relation8, relation9")
    #A clash_list-chunk is a list that stores the atomic concept assertions while looking for a clash. The atom in the head of the list, used to find a clashing atom, moves one place down the list after no such clashing atom can be found. A new atom then takes the place in the head of the list.
    actr.chunktype("clash_list", "thing, form, element, concept, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15, form16, form17, form18")
    #A used_list-chunk stores all the formulas that have already been used to make an inference on and hence do not qualify for makig further inferences.
    actr.chunktype("used_list", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15, form16, form17, form18 form19, form20, form21, form22, form23, form24, form25, form26, form27, form28, form29, form30, form31, form32, form33, form34, form35, form36, form37, form38, form39, form40")
    #The universal_list type stores the universal restriction formulas that are inspected during one execution of component 5.
    actr.chunktype("universal_list", "thing, form, form2, form3, form4, form5, form6, form7, form8, form9")
    #The count_order type allows SHARP to keep track of how many times component 5 is visited; it contains a number and its successor.
    actr.chunktype("count_order","number, successor, thing")
    #The role_list contains element names that have already been used for role/relation formulas. This is to ensure that when a new role/relation formula is derived (in component 4), an element is picked that is not used yet.
    actr.chunktype("role_list", "thing, role1, role2, role3, role4, role5, role6, role7, role8, role9, role10, role11, role12, role13, role14, role15, role16")

    aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="find_clash_to_head", form='none', count1=0, count2=1, mainconnective='none', role='none', derivenew='yes'))

    cp1.component1(aBoxCon)
    cp2.component2(aBoxCon)
    cp3.component3(aBoxCon)
    cp4.component4(aBoxCon)
    cp5.component5(aBoxCon)

    par.AddAboxFromFile(abox,aBoxCon)
    return aBoxCon

def result(abox):
    #Takes an abox.
    #Returns both the simulation time and a list with the formulas inspected.
    
    prove_tracks = []
    mod = model(abox, learning=True)
    sim = mod.simulation(realtime=False,gui=False)
    sim.step()
    while True:
        #This loop executes the simulation step-by-step.
        if sim.current_event.proc=='manual' and sim.current_event.action.startswith('KEY'):
            #The judgement that the model gives on the input ABox: 'C' for consistent and 'I' for inconsistent.
            judgement = str(sim.current_event).split('KEY PRESSED: ')[1][0]
        if sim.current_event.action.startswith('RULE SELECTED: Component 2, Rule 3a') or sim.current_event.action.startswith('RULE SELECTED: Component 2, Rule 4a') or sim.current_event.action.startswith('RULE SELECTED: Component 2, Rule 5a') or sim.current_event.action.startswith('RULE SELECTED: Component 2, Rule 6a') or sim.current_event.action.startswith('RULE SELECTED: Component 5, Rule 2a'):
            #In this case a formula is selected to make an inference on.
            #It is printed and added to the prove_tracks list.
            a = str(mod.retrieval)
            b = a.split('form= ',1)[1].split(', ',1)[0]
            print(b)
            prove_tracks.append(b)
        try:
            #The next step of the simulation is tried, without printing the simulation output.
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            sim.step()
            sys.stdout = old_stdout
        except:
            #In case the simulation cannot perform a next step, two situations are possible:
            #    the simulation has ended without problems
            #    a problem occured that made the simulation stop prematurely.
            sys.stdout = old_stdout
            goalstate = str(mod.goals['g']).split('state= ')[1].split(')')[0]
            if goalstate=='stop':
                #If the simulation has ended without problems, the time is printed and a string is made from the list of consecutively inspected formulas.
                time = sim.current_event.time
                print('End of simulation,', time)
                run = '|'
                for j in prove_tracks:
                    run = run + ' -> ' + j
            else:
                #In case a problem occured, some indications are printed with which one can try to solve the issue.
                #In all usual cases this should not happen.
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

def result_it(n, abox):
    #Takes a number of iterations and an ABox.
    #Returns a Dataframe with n many simulation results (run of inspected formulas, simulated time and the judgement whether the Abox was consistent or not).
    
    df = pd.DataFrame(columns=['ABox', 'Run', 'Time', 'Judgement'])
    for i in range(n):
        run, time, judgement = result(abox)
        new_row = pd.DataFrame([[abox,run,time,judgement]],columns=['ABox', 'Run', 'Time', 'Judgement'])
        df = pd.concat([
            df if not df.empty else None,
            new_row], ignore_index=True)
    return df

def result_aboxes(n, aboxes):
    #Takes a number of iterations and a list of ABoxes.
    #Returns a DataFrame with n many simulation results (run of inspected formulas, simulated time and the judgement whether the Abox was consistent or not) for each ABox in the list.
    
    df = pd.DataFrame(columns=['ABox', 'Run', 'Time', 'Judgement'])
    for abox in aboxes:
        new_rows = result_it(n, abox)
        df = pd.concat([
            df if not df.empty else None,
            new_rows], ignore_index=True)
    return dat

#This testset might be used to try out SHARP

testset = [
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


n = 10 #The number of simulations one wants for each ABox
t = testset #The set of ABoxes one wants simulations of
a = result_aboxes(n, t)
print(a.head())

#To save the data, use the following code
#path = ''
#a.to_csv(path,index_label='Index')
