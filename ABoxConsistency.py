import pyactr as actr
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

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

    actr.chunktype("goal", "state")
    actr.chunktype("proposition", "thing, form, element, mainconnective, relation, subformula1, inferred1, subformula2, inferred2, derived")
    actr.chunktype("checklist", "thing, form, element, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
    actr.chunktype("storelist", "thing, form, element, mainconnective, relation, subformula1, subformula2, derived, inferred1, inferred2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")

    aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="start"))
    aBoxCon.goals["imaginal"].add(actr.makechunk(typename="checklist", thing="checklist"))
    return aBoxCon

def module1(aBoxCon):
    aBoxCon.productionstring(name="find first formula", string="""
        =g>
        isa     goal
        state   start
        =imaginal>
        isa     checklist
        thing   checklist
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   store
        +retrieval>
        isa     proposition
        thing   proposition
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~relation
        mainconnective ~existential
        mainconnective ~universal
    """)

    aBoxCon.productionstring(name="skip and derive first formula", string="""
        =g>
        isa     goal
        state   store
        =imaginal>
        isa     checklist
        thing   checklist
        ?retrieval>
        state   error
        ==>
        =g>
        isa      goal
        state    module2
        ~retrieval>
    """)

    aBoxCon.productionstring(name="store first formula", string="""
        =g>
        isa     goal
        state   store
        =imaginal>
        isa     checklist
        thing   checklist
        =retrieval>
        isa     proposition
        thing   proposition
        form    =U
        element  =X
        mainconnective =Y
        subformula1 =Z
        ==>
        =g>
        isa     goal
        state   find_clash
        +imaginal>
        isa     checklist
        thing   checklist
        form    =U
        element =X
        mainconnective =Y
        subformula1 =Z
        relation none
        subformula2 none
        form2   none
        form3   none
        form4   none
        form5   none
        form6   none
        form7   none
        form8   none
    """)

    aBoxCon.productionstring(name="find clash 1", string="""
        =g>
        isa     goal
        state   find_clash
        =imaginal>
        isa     checklist
        thing   checklist
        element =X
        mainconnective concept
        relation =G
        subformula1 =Y
        form    =Z
        form2   =A
        form3   =B
        form4   =C
        form5   =D
        form6   =E
        form7   =F
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   signal_clash
        +imaginal>
        isa     checklist
        thing   checklist
        element =X
        mainconnective concept
        subformula1 =Y
        relation =G
        form    =Z
        form2   =A
        form3   =B
        form4   =C
        form5   =D
        form6   =E
        form7   =F
        +retrieval>
        isa     proposition
        thing   proposition
        element  =X
        mainconnective negation
        subformula1 =Y
        derived  yes
    """)

    aBoxCon.productionstring(name="show clash 1", string="""
        =g>
        isa     goal
        state   signal_clash
        =imaginal>
        isa     checklist
        thing   checklist
        element =X
        form    =X1
        mainconnective concept
        subformula1 =Y
        relation =Z1
        subformula2 =Z2
        form2   =Z3
        form3   =Z4
        form4   =Z5
        form5   =Z6
        form6   =Z7
        form7   =Z8
        form8   =Z9
        =retrieval>
        isa     proposition
        thing   proposition
        element  =X
        mainconnective negation
        subformula1 =Y
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        +manual>
        isa     _manual
        cmd     press_key
        key     C
    """)

    aBoxCon.productionstring(name="no clash 1", string="""
        =g>
        isa     goal
        state   signal_clash
        =imaginal>
        isa     checklist
        thing   checklist
        form    =Z
        element =X
        mainconnective concept
        subformula1 =Y
        form2   =A
        form3   =B
        form4   =C
        form5   =D
        form6   =E
        form7   =F
        form8   =G
        relation =Z1
        subformula2 =Z2
        ?retrieval>
        state   error
        ==>
        =g>
        isa     goal
        state   find_next_formula
        +imaginal>
        isa     checklist
        thing   checklist
        form    none
        element none
        mainconnective none
        subformula1 none
        subformula2 none
        relation none
        form2   =Z
        form3   =A
        form4   =B
        form5   =C
        form6   =D
        form7   =E
        form8   =F
        ~retrieval>
    """)

    aBoxCon.productionstring(name="find clash 2", string="""
        =g>
        isa     goal
        state   find_clash
        =imaginal>
        isa     checklist
        thing   checklist
        element =X
        mainconnective negation
        subformula1 =Y
        relation =G
        form    =Z
        form2   =A
        form3   =B
        form4   =C
        form5   =D
        form6   =E
        form7   =F
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   signal_clash
        +imaginal>
        isa     checklist
        thing   checklist
        element =X
        mainconnective negation
        subformula1 =Y
        relation =G
        form    =Z
        form2   =A
        form3   =B
        form4   =C
        form5   =D
        form6   =E
        form7   =F
        +retrieval>
        isa     proposition
        thing   proposition
        element  =X
        mainconnective concept
        subformula1 =Y
        derived  yes
    """)

    aBoxCon.productionstring(name="show clash 2", string="""
        =g>
        isa     goal
        state   signal_clash
        =imaginal>
        isa     checklist
        thing   checklist
        element =X
        form    =X1
        mainconnective negation
        subformula1 =Y
        relation =Z1
        subformula2 =Z2
        form2  =Z3
        form3  =Z4
        form4  =Z5
        form5  =Z6
        form6  =Z7
        form7  =Z8
        form8  =Z9
        =retrieval>
        isa     proposition
        thing   proposition
        element  =X
        mainconnective concept
        subformula1 =Y
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        +manual>
        isa     _manual
        cmd     press_key
        key     C
    """)

    aBoxCon.productionstring(name="no clash 2", string="""
        =g>
        isa     goal
        state   signal_clash
        =imaginal>
        isa     checklist
        thing   checklist
        form    =Z
        element =X
        mainconnective negation
        subformula1 =Y
        form2   =A
        form3   =B
        form4   =C
        form5   =D
        form6   =E
        form7   =F
        form8   =G
        relation =Z1
        subformula2 =Z2
        ?retrieval>
        state   error
        ==>
        =g>
        isa     goal
        state   find_next_formula
        +imaginal>
        isa     checklist
        thing   checklist
        form    none
        element none
        mainconnective none
        subformula1 none
        subformula2 none
        relation none
        form2   =Z
        form3   =A
        form4   =B
        form5   =C
        form6   =D
        form7   =E
        form8   =F
        ~retrieval>
    """)

    aBoxCon.productionstring(name="find next formula", string="""
        =g>
        isa     goal
        state   find_next_formula
        =imaginal>
        isa     checklist
        thing   checklist
        form    =X1
        mainconnective =X2
        subformula1 =X3
        subformula2 =X4
        relation =X5
        element =X6
        form2   =U0
        form3   =U1
        form4   =U2
        form5   =U3
        form6   =U4
        form7   =U5
        form8   =U6
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   decide
        +retrieval>
        isa     proposition
        thing   proposition
        derived yes
        form    ~=X1
        form    ~=U0
        form    ~=U1
        form    ~=U2
        form    ~=U3
        form    ~=U4
        form    ~=U5
        form    ~=U6
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~relation
        mainconnective ~existential
        mainconnective ~universal
        =imaginal>
        isa     checklist
        thing   checklist
        form    =X1
        mainconnective =X2
        subformula1 =X3
        subformula2 =X4
        relation =X5
        element =X6
        form2   =U0
        form3   =U1
        form4   =U2
        form5   =U3
        form6   =U4
        form7   =U5
        form8   =U6
    """)

    aBoxCon.productionstring(name="repeat", string="""
        =g>
        isa     goal
        state   decide
        =retrieval>
        isa     proposition
        element =X
        mainconnective =Y
        subformula1 =Z
        form    =U
        thing   proposition
        =imaginal>
        isa     checklist
        thing   checklist
        form    none
        element none
        mainconnective none
        subformula1 none
        subformula2 none
        relation none
        form2   =U0
        form3   =U1
        form4   =U2
        form5   =U3
        form6   =U4
        form7   =U5
        form8   =U6
        ==>
        =g>
        isa     goal
        state   find_clash
        +imaginal>
        isa     checklist
        thing   checklist
        form    =U
        element =X
        mainconnective =Y
        subformula1 =Z
        subformula2 none
        relation none
        form    =U
        form2   =U0
        form3   =U1
        form4   =U2
        form5   =U3
        form6   =U4
        form7   =U5
        form8   =U6
        ~retrieval>
    """)

    aBoxCon.productionstring(name="move on", string="""
        =g>
        isa     goal
        state   decide
        ?retrieval>
        state   error
        ==>
        =g>
        isa     goal
        state   module2
        ~retrieval>
    """)

def module2(aBoxCon):
    aBoxCon.productionstring(name="find formula to apply rule to", string="""
        =g>
        isa      goal
        state    module2
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   find_rule
        +retrieval>
        isa     proposition
        thing   proposition
        mainconnective  conjunction
        derived  yes
    """)

    aBoxCon.productionstring(name="conjunction found, first conjunct inferred? 1", string="""
        =g>
        isa      goal
        state    find_rule
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        ==>
        =g>
        isa      goal
        state    first_conjunct_inferred1
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1  no
        subformula2  =Z
        inferred2  no
        derived  yes
        relation none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="conjunction found, first conjunct inferred? 2", string="""
        =g>
        isa      goal
        state    first_conjunct_inferred1
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1  no
        subformula2  =Z
        inferred2  no
        derived  yes
        relation none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    first_conjunct_inferred2
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        mainconnective conjunction
        inferred1 yes
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1  no
        subformula2  =Z
        inferred2  no
        derived  yes
        relation none
    """)

    aBoxCon.productionstring(name="label first conjunct as inferred", string="""
        =g>
        isa      goal
        state    first_conjunct_inferred2
        ?retrieval>
        state    error
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation none
        ==>
        =g>
        isa      goal
        state    retrieve_first_conjunct
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1  yes
        inferred2  none
        relation   none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="retrieve first conjunct", string="""
        =g>
        isa      goal
        state    retrieve_first_conjunct
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1  yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_first_conjunct
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Y
        ~imaginal>
    """)

    aBoxCon.productionstring(name="label first conjunct as derived", string="""
        =g>
        isa      goal
        state    label_first_conjunct
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    module3
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation none
        inferred1 none
        inferred2 none
    """)

    aBoxCon.productionstring(name="second_conjunct_inferred_a", string="""
        =g>
        isa      goal
        state    first_conjunct_inferred2
        ?retrieval>
        buffer   full
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 yes
        subformula2 =V
        inferred2 =W
        derived   =Z
        relation none
        ?imaginal>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        form     =T1
        element  =T2
        mainconnective conjunction
        subformula1  =T3
        inferred1  no
        subformula2  =T4
        inferred2  no
        derived  yes
        relation none
        ==>
        =g>
        isa      goal
        state    pre_infer_second_conjunct_after_first
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 yes
        subformula2 =V
        inferred2 =W
        derived   =Z
        relation  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="second_conjunct_inferred_b", string="""
        =g>
        isa      goal
        state    pre_infer_second_conjunct_after_first
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 yes
        subformula2 =V
        inferred2 =W
        derived   =Z
        relation none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    infer_second_conjunct_after_first
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 yes
        subformula2 =V
        inferred2 yes
        derived   =Z
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 yes
        subformula2 =V
        inferred2 =W
        derived   =Z
        relation  none
    """)

    aBoxCon.productionstring(name="store in list 1", string="""
        =g>
        isa      goal
        state    infer_second_conjunct_after_first
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        inferred1 yes
        inferred2 yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    store_in_list
        +imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        derived  none
        inferred1 none
        inferred2 none
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        form9    none
        form10   none
        form11   none
        form12   none
        form13   none
        form14   none
        form15   none
    """)

    aBoxCon.productionstring(name="label second conjunct as inferred after first", string="""
        =g>
        isa      goal
        state    infer_second_conjunct_after_first
        ?retrieval>
        state    error
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation none
        inferred1 =S1
        inferred2 =S2
        ==>
        =g>
        isa      goal
        state    retrieve_second_conjunct_after_first
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1 yes
        inferred2 yes
        relation  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="retrieve second conjunct after first", string="""
        =g>
        isa      goal
        state    retrieve_second_conjunct_after_first
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1 yes
        inferred2 yes
        relation  none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_second_conjunct_after_first
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        derived  no
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1 yes
        inferred2 yes
        relation  none
    """)

    aBoxCon.productionstring(name="label second conjunct as derived after first", string="""
        =g>
        isa      goal
        state    label_second_conjunct_after_first
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        relation  =S
        inferred1  =S1
        inferred2  =S2
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    module3
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation  =S
        inferred1 =S1
        inferred2 =S2
    """)


    #--------------------------------------------------------------------------------------------------


    aBoxCon.productionstring(name="conjunction found, second conjunct inferred? 1", string="""
        =g>
        isa      goal
        state    find_rule
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        ==>
        =g>
        isa      goal
        state    second_conjunct_inferred1
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1  no
        subformula2  =Z
        inferred2  no
        derived  yes
        relation none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="conjunction found, second conjunct inferred? 2", string="""
        =g>
        isa      goal
        state    second_conjunct_inferred1
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1  no
        subformula2  =Z
        inferred2  no
        derived  yes
        relation none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    second_conjunct_inferred2
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        mainconnective conjunction
        inferred2 yes
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1  no
        subformula2  =Z
        inferred2  no
        derived  yes
        relation none
    """)

    aBoxCon.productionstring(name="label second conjunct as inferred", string="""
        =g>
        isa      goal
        state    second_conjunct_inferred2
        ?retrieval>
        state    error
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation none
        ==>
        =g>
        isa      goal
        state    retrieve_second_conjunct
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred2  yes
        inferred1  none
        relation   none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="retrieve second conjunct", string="""
        =g>
        isa      goal
        state    retrieve_second_conjunct
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred2  yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_second_conjunct
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Z
    """)

    aBoxCon.productionstring(name="label second conjunct as derived", string="""
        =g>
        isa      goal
        state    label_second_conjunct
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    module3
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation  none
        inferred1 none
        inferred2 none
    """)

    aBoxCon.productionstring(name="first_conjunct_inferred_a", string="""
        =g>
        isa      goal
        state    second_conjunct_inferred2
        ?retrieval>
        buffer   full
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 =W
        subformula2 =V
        inferred2 yes
        derived   =Z
        relation none
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    pre_infer_first_conjunct_after_second
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 =W
        subformula2 =V
        inferred2 yes
        derived   =Z
        relation  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="first_conjunct_inferred_b", string="""
        =g>
        isa      goal
        state    pre_infer_first_conjunct_after_second
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 =W
        subformula2 =V
        inferred2 yes
        derived   =Z
        relation  none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    infer_first_conjunct_after_second
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 yes
        subformula2 =V
        inferred2 yes
        derived   =Z
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective conjunction
        subformula1 =U
        inferred1 =W
        subformula2 =V
        inferred2 yes
        derived   =Z
        relation  none
    """)

    aBoxCon.productionstring(name="store in list 2", string="""
        =g>
        isa      goal
        state    infer_first_conjunct_after_second
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        inferred1 yes
        inferred2 yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    store_in_list
        +imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        derived  none
        inferred1  none
        inferred2  none
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        form9    none
        form10   none
        form11   none
        form12   none
        form13   none
        form14   none
        form15   none
    """)

    aBoxCon.productionstring(name="label first conjunct as inferred after second", string="""
        =g>
        isa      goal
        state    infer_first_conjunct_after_second
        ?retrieval>
        state    error
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation none
        inferred1 =S1
        inferred2 =S2
        ==>
        =g>
        isa      goal
        state    retrieve_first_conjunct_after_second
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1 yes
        inferred2 yes
        relation  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="retrieve first conjunct after second", string="""
        =g>
        isa      goal
        state    retrieve_first_conjunct_after_second
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1 yes
        inferred2 yes
        relation  none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_first_conjunct_after_second
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Y
        derived  no
        element  =U
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        derived  yes
        inferred1 yes
        inferred2 yes
        relation  none
    """)

    aBoxCon.productionstring(name="label first conjunct as derived after second", string="""
        =g>
        isa      goal
        state    label_first_conjunct_after_second
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        relation  =S
        inferred1  =S1
        inferred2  =S2
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    module3
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation   =S
        inferred1  =S1
        inferred2  =S2
    """)

def module3(aBoxCon):
    aBoxCon.productionstring(name="do we need to check for a clash? concept found", string="""
        =g>
        isa      goal
        state    module3
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective concept
        subformula1  =Y
        derived  yes
        ==>
        =g>
        isa      goal
        state    find_clash
        +imaginal>
        isa      checklist
        thing    checklist
        form     =X
        mainconnective concept
        element  =U
        subformula1 =Y
        relation none
        subformula2 none
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="do we need to check for a clash? negation found", string="""
        =g>
        isa      goal
        state    module3
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective negation
        subformula1  =Y
        derived  yes
        ==>
        =g>
        isa      goal
        state    find_clash
        +imaginal>
        isa      checklist
        thing    checklist
        mainconnective negation
        element  =U
        subformula1 =Y
        form     =X
        relation none
        subformula2 none
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="do we need to derive something new?", string="""
        =g>
        isa      goal
        state    module3
        =imaginal>
        isa      proposition
        thing    proposition
        element  =X
        subformula1 =Y
        form     =Z
        mainconnective ~concept
        mainconnective ~negation
        ==>
        =g>
        isa      goal
        state    module2
        ~imaginal>
        ~retrieval>
    """)

def module4(aBoxCon):
    aBoxCon.productionstring(name="retrieve the next proposition to store in the list", string="""
        =g>
        isa      goal
        state    store_in_list
        =imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        form2    =T1
        form3    =T2
        form4    =T3
        form5    =T4
        form6    =T5
        form7    =T6
        form8    =T7
        form9    =T8
        form10   =T9
        form11   =T10
        form12   =T11
        form13   =T12
        form14   =T13
        form15   =T14
        derived  =S1
        inferred1 =S2
        inferred2 =S3
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    store_in_list2
        +retrieval>
        isa      proposition
        thing    proposition
        form     ~=X
        form     ~=T1
        form     ~=T2
        form     ~=T3
        form     ~=T4
        form     ~=T5
        form     ~=T6
        form     ~=T7
        form     ~=T8
        form     ~=T9
        form     ~=T10
        form     ~=T11
        form     ~=T12
        form     ~=T13
        form     ~=T14
        derived  yes
        inferred1 yes
        inferred2 yes
    """)

    aBoxCon.productionstring(name="store the next proposition in the list", string="""
        =g>
        isa      goal
        state    store_in_list2
        =imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        form2    =T1
        form3    =T2
        form4    =T3
        form5    =T4
        form6    =T5
        form7    =T6
        form8    =T7
        form9    =T8
        form10   =T9
        form11   =T10
        form12   =T11
        form13   =T12
        form14   =T13
        derived   =S1
        inferred1 =S2
        inferred2 =S3
        form15    =S4
        ?retrieval>
        state    free
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X2
        derived  yes
        inferred1 yes
        inferred2 yes
        element  =Y2
        mainconnective =Z2
        relation =U2
        subformula1 =V2
        subformula2 =W2
        ==>
        =g>
        isa      goal
        state    store_in_list
        +imaginal>
        isa      storelist
        thing    storelist
        element  =Y2
        mainconnective =Z2
        relation =U2
        subformula1 =V2
        subformula2 =W2
        form     =X2
        form2    =X
        form3    =T1
        form4    =T2
        form5    =T3
        form6    =T4
        form7    =T5
        form8    =T6
        form9    =T7
        form10   =T8
        form11   =T9
        form12   =T11
        form13   =T11
        form14   =T12
        form15   =T13
        derived  yes
        inferred1 yes
        inferred2 yes
    """)

    aBoxCon.productionstring(name="use the list to select the next formula", string="""
        =g>
        isa      goal
        state    store_in_list2
        =imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        form2    =T1
        form3    =T2
        form4    =T3
        form5    =T4
        form6    =T5
        form7    =T6
        form8    =T7
        form9    =T8
        form10   =T9
        form11   =T10
        form12   =T11
        form13   =T12
        form14   =T13
        derived   =S1
        inferred1 =S2
        inferred2 =S3
        form15    =S4
        ?retrieval>
        state    error
        ==>
        =g>
        isa     goal
        state   find_rule
        +retrieval>
        isa     proposition
        thing   proposition
        form     ~=X
        form     ~=T1
        form     ~=T2
        form     ~=T3
        form     ~=T4
        form     ~=T5
        form     ~=T6
        form     ~=T7
        form     ~=T8
        form     ~=T9
        form     ~=T10
        form     ~=T11
        form     ~=T12
        form     ~=T13
        form     ~=S4
        mainconnective  conjunction
        derived  yes
    """)

    aBoxCon.productionstring(name="confirm consistency", string="""
        =g>
        isa      goal
        state    find_rule
        ?retrieval>
        state    error
        ==>
        =g>
        isa     goal
        state   stop
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)

def trace(mod, buffer, action=''):
    sim = mod.simulation(realtime=False,gui=False)
    sim.step()
    while True:
        if sim.current_event.proc==buffer and sim.current_event.action.startswith(action):
            print(mod.retrieval)
        try:
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
            sim.step()
            sys.stdout = old_stdout
        except:
            sys.stdout = old_stdout
            print('End of simulation.')
            break
    return sim.current_event.time

def plot_list(it):
    sim_time_list = []
    for i in range(it):
        aBoxCon = initial(True)
        dm = aBoxCon.decmem

        module1(aBoxCon)
        module2(aBoxCon)
        module3(aBoxCon)
        module4(aBoxCon)

        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A&/Es.F", element="a", mainconnective="conjunction", subformula1="a:A", subformula2="a:/Es.F", derived="yes", inferred1="no", inferred2="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:/As.(nF%nB)", element="a", mainconnective="universal", relation="s", subformula1="b:nF%nB", derived="yes"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:B", element="b", mainconnective="concept", subformula1="B", derived="yes"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,b):s", mainconnective="relation", relation="s", subformula1="a", subformula2="b", derived="yes"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,c):r", mainconnective="relation", relation="r", subformula1="a", subformula2="c", derived="yes"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:C&/Es.D", element="c", mainconnective="conjunction", subformula1="c:C", subformula2="c:/Es.D", derived="yes", inferred1="no", inferred2="no"))

        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A", element="a", mainconnective="concept", subformula1="A", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nF%nB", element="b", mainconnective="disjunction", subformula1="b:nF", subformula2="b:nB", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nF", element="b", mainconnective="negation", subformula1="F", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:/Es.F", element="a", mainconnective="existential", relation="s", subformula1="x:F", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,x):s", mainconnective="relation", relation="s", subformula1="a", subformula2="x", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nF%nB", element="x", mainconnective="disjunction", subformula1="x:nF", subformula2="x:nB", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nB", element="x", mainconnective="negation", subformula1="B", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nF", element="x", mainconnective="negation", subformula1="F", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:C", element="c", mainconnective="concept", subformula1="C", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:/Es.D", element="c", mainconnective="existential", relation="s", subformula1="y:D", derived="no"))
        dm.add(actr.makechunk(typename="proposition", thing="proposition", form="y:D", element="y", mainconnective="concept", subformula1="D", derived="no"))

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

#simulation_plot(2)

#plt.show()


aBoxCon = initial(True)
dm = aBoxCon.decmem

module1(aBoxCon)
module2(aBoxCon)
module3(aBoxCon)
module4(aBoxCon)

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A&/Es.F", element="a", mainconnective="conjunction", subformula1="a:A", subformula2="a:/Es.F", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:/As.(nF%nB)", element="a", mainconnective="universal", relation="s", subformula1="b:nF%nB", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:B", element="b", mainconnective="concept", subformula1="B", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,b):s", mainconnective="relation", relation="s", subformula1="a", subformula2="b", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,c):r", mainconnective="relation", relation="r", subformula1="a", subformula2="c", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:C&/Es.D", element="c", mainconnective="conjunction", subformula1="c:C", subformula2="c:/Es.D", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A", element="a", mainconnective="concept", subformula1="A", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nF%nB", element="b", mainconnective="disjunction", subformula1="b:nF", subformula2="b:nB", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nF", element="b", mainconnective="negation", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:/Es.F", element="a", mainconnective="existential", relation="s", subformula1="x:F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,x):s", mainconnective="relation", relation="s", subformula1="a", subformula2="x", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nF%nB", element="x", mainconnective="disjunction", subformula1="x:nF", subformula2="x:nB", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nB", element="x", mainconnective="negation", subformula1="B", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nF", element="x", mainconnective="negation", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:C", element="c", mainconnective="concept", subformula1="C", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:/Es.D", element="c", mainconnective="existential", relation="s", subformula1="y:D", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="y:D", element="y", mainconnective="concept", subformula1="D", derived="no"))

trace(aBoxCon, 'retrieval')
