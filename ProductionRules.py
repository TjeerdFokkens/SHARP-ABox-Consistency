#Production rules that always follow each other form a unit.
#A unit can consist of only one production rule, or several, indicated by 'Step n', with n a natural number.
#When several different production rules can fire after given one, they form new units, each labelled by a, b, etc.

def module1(aBoxCon): #This module looks for concept assignments and negated concept assignments and tries to find a clash. If there is no clash, some new formula needs to be derived.
    aBoxCon.productionstring(name="Module 1, Unit 1: find first concept or negation, Step 1", string="""
        =g>
        isa     goal
        state   find_clash
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   next_concept_negation
        form    =P
        +retrieval>
        isa     proposition
        thing   proposition
        element =A2
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        mainconnective ~=A3
        form    ~=A1
        form    ~=A7
        form    ~=A8
        form    ~=A9
        form    ~=A10
        form    ~=A11
        form    ~=A12
        form    ~=A13
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2a: skip and derive new formula, Step 1", string="""
        =g>
        isa     goal
        state   next_concept_negation
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        ?retrieval>
        state   error
        ==>
        =g>
        isa      goal
        state    find_clash
        form     =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        +retrieval>
        isa     proposition
        thing   proposition
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        form    ~=A1
        form    ~=A7
        form    ~=A8
        form    ~=A9
        form    ~=A10
        form    ~=A11
        form    ~=A12
        form    ~=A13
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2a: skip and derive new formula, Step 1", string="""
        =g>
        isa     goal
        state   next_concept_negation
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        =retrieval>
        isa     proposition
        thing   proposition
        element  =A2
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~universal
        mainconnective ~existential
        mainconnective ~=A3
        subformula1 =Y
        derived yes
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        form    =P
        +manual>
        isa     _manual
        cmd     press_key
        key     C
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2a: skip and derive new formula, Step 1", string="""
        =g>
        isa     goal
        state   find_clash
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        ?retrieval>
        state   error
        ==>
        =g>
        isa      goal
        state    derive_next
        form     =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        =retrieval>
        isa     proposition
        thing   proposition
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        form    ~=A1
        form    ~=A7
        form    ~=A8
        form    ~=A9
        form    ~=A10
        form    ~=A11
        form    ~=A12
        form    ~=A13
    """)
----------------------------
    aBoxCon.productionstring(name="Module 1, Unit 2a: skip and derive new formula, Step 1", string="""
        =g>
        isa     goal
        state   derive_next
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        ?retrieval>
        state   error
        ==>
        =g>
        isa      goal
        state    derive_next
        form     =P
        +retrieval>
        isa     proposition
        thing   proposition
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        form    ~=A1
        form    ~=A7
        form    ~=A8
        form    ~=A9
        form    ~=A10
        form    ~=A11
        form    ~=A12
        form    ~=A13
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2b: store first formula and find corresponding clash, Step 1", string="""
        =g>
        isa     goal
        state   store
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        mainconnective =A3
        relation =A4
        subformula1 =A5
        subformula2 =A6
        form2    =A7
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        =retrieval>
        isa     proposition
        thing   proposition
        form    =U
        element  =X
        mainconnective =Y
        subformula1 =Z
        derived yes
        ==>
        =g>
        isa     goal
        state   find_clash
        form    =P
        +imaginal>
        isa     checklist
        thing   checklist
        form    =U
        element =X
        mainconnective =Y
        subformula1 =Z
        relation none
        subformula2 none
        form2   =A1
        form3   =A7
        form4   =A8
        form5   =A9
        form6   =A10
        form7   =A11
        form8   =A12
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2b: store first formula and find corresponding clash, Step 2", string="""
        =g>
        isa     goal
        state   find_clash
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        element =X
        mainconnective =V
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
        form    =P
        +imaginal>
        isa     checklist
        thing   checklist
        element =X
        mainconnective =V
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
        mainconnective ~universal
        mainconnective ~existential
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~=V
        subformula1 =Y
        derived  yes
    """)

    aBoxCon.productionstring(name="Module 1, Unit 3a: show clash, Step 1", string="""
        =g>
        isa     goal
        state   signal_clash
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        element =X
        form    =X1
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~universal
        mainconnective ~existential
        mainconnective =V
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
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~universal
        mainconnective ~existential
        mainconnective ~=V
        subformula1 =Y
        derived yes
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        form    =P
        +manual>
        isa     _manual
        cmd     press_key
        key     C
    """)

    aBoxCon.productionstring(name="Module 1, Unit 3b: no clash, so find next concept or negation, Step 1", string="""
        =g>
        isa     goal
        state   signal_clash
        form    =P
        =imaginal>
        isa     checklist
        thing   checklist
        form    =Z
        element =X
        mainconnective ~universal
        mainconnective ~existential
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective =V
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
        form    =P
        +imaginal>
        isa     checklist
        thing   checklist
        form    =Z
        element =X
        mainconnective =V
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
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 1, Unit 3b: no clash, so find next concept or negation, Step 2", string="""
        =g>
        isa     goal
        state   find_next_formula
        form    =P
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
        form    =P
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

    aBoxCon.productionstring(name="Module 1, Unit 4a: repeat, Step 1", string="""
        =g>
        isa     goal
        state   decide
        form    =P
        =retrieval>
        isa     proposition
        element =X
        mainconnective =Y
        subformula1 =Z
        form    =U
        thing   proposition
        derived yes
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
        form    =P
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

    aBoxCon.productionstring(name="Module 1, Unit 4b: move on to next module, Step 1", string="""
        =g>
        isa     goal
        state   decide
        form    =P
        ?retrieval>
        state   error
        ==>
        =g>
        isa     goal
        state   derive_next
        form    =P
        ~retrieval>
    """)

def module2(aBoxCon): #This module applies when a conjunction is found. It derives a conjunct (right or left) that has not been derived yet.
    aBoxCon.productionstring(name="Module 2, Unit 1: find conjunction to apply derivation to, Step 1", string="""
        =g>
        isa      goal
        state    derive_next
        form    =P
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   find_rule
        form    =P
        +retrieval>
        isa     proposition
        thing   proposition
        mainconnective  conjunction
        derived  yes
    """) #Move this rule to module 1 in the future. Adjust 'mainconnective' to also allow for 'existential'.

    aBoxCon.productionstring(name="Module 2, Unit 2a: conjunction found, first conjunct inferred, Step 1", string="""
        =g>
        isa      goal
        state    find_rule
        form    =P
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
        form    =P
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

    aBoxCon.productionstring(name="Module 2, Unit 2a: conjunction found, first conjunct inferred, Step 2", string="""
        =g>
        isa      goal
        state    first_conjunct_inferred1
        form    =P
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
        form    =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        mainconnective conjunction
        inferred1 yes
        derived  yes
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

    aBoxCon.productionstring(name="Module 2, Unit 3a: label first conjunct as inferred and derived, Step 1", string="""
        =g>
        isa      goal
        state    first_conjunct_inferred2
        form    =P
        ?retrieval>
        state    error
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1 no
        subformula2  =Z
        inferred2 no
        derived  yes
        relation none
        ==>
        =g>
        isa      goal
        state    retrieve_first_conjunct
        form    =P
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

    aBoxCon.productionstring(name="Module 2, Unit 3a: label first conjunct as inferred and derived, Step 2", string="""
        =g>
        isa      goal
        state    retrieve_first_conjunct
        form     =P
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
        inferred2  none
        relation   none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_first_conjunct
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Y
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 3a: label first conjunct as inferred and derived, Step 3", string="""
        =g>
        isa      goal
        state    label_first_conjunct
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 3b: check if second conjunct inferred after first, Step 1", string="""
        =g>
        isa      goal
        state    first_conjunct_inferred2
        form     =P
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
        derived   yes
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
        form     =P
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
        derived   yes
        relation  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 3b: check if second conjunct inferred after first, Step 2", string="""
        =g>
        isa      goal
        state    pre_infer_second_conjunct_after_first
        form     =P
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
        derived   yes
        relation none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    infer_second_conjunct_after_first
        form     =P
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
        derived   yes
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
        derived   yes
        relation  none
    """)

    aBoxCon.productionstring(name="Module 2, Unit 4a: store in list of used formulas, Step 1", string="""
        =g>
        isa      goal
        state    infer_second_conjunct_after_first
        form     =P
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
        derived   yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    store_in_list
        form     =P
        +imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        derived  yes
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

    aBoxCon.productionstring(name="Module 2, Unit 4b: label second conjunct as inferred and derived after first, Step 1", string="""
        =g>
        isa      goal
        state    infer_second_conjunct_after_first
        form     =P
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
        inferred1 yes
        inferred2 =S2
        ==>
        =g>
        isa      goal
        state    retrieve_second_conjunct_after_first
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 4b: label second conjunct as inferred and derived after first, Step 2", string="""
        =g>
        isa      goal
        state    retrieve_second_conjunct_after_first
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 4b: label second conjunct as inferred and derived after first, Step 3", string="""
        =g>
        isa      goal
        state    label_second_conjunct_after_first
        form     =P
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
        derived   no
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    module3
        form     =P
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


    aBoxCon.productionstring(name="Module 2, Unit 2b: conjunction found, second conjunct inferred, Step 1", string="""
        =g>
        isa      goal
        state    find_rule
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 2b: conjunction found, second conjunct inferred, Step 2", string="""
        =g>
        isa      goal
        state    second_conjunct_inferred1
        form     =P
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
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        mainconnective conjunction
        inferred2 yes
        derived  yes
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

    aBoxCon.productionstring(name="Module 2, Unit 5a: label second conjunct as inferred and derived, Step 1", string="""
        =g>
        isa      goal
        state    second_conjunct_inferred2
        form     =P
        ?retrieval>
        state    error
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective conjunction
        subformula1  =Y
        inferred1 no
        subformula2  =Z
        inferred2 no
        derived  yes
        relation none
        ==>
        =g>
        isa      goal
        state    retrieve_second_conjunct
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 5a: label second conjunct as inferred and derived, Step 2", string="""
        =g>
        isa      goal
        state    retrieve_second_conjunct
        form     =P
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
        inferred1  none
        relation   none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_second_conjunct
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Z
    """)

    aBoxCon.productionstring(name="Module 2, Unit 5a: label second conjunct as inferred and derived, Step 3", string="""
        =g>
        isa      goal
        state    label_second_conjunct
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 5b: check if first conjunct inferred after second, Step 1", string="""
        =g>
        isa      goal
        state    second_conjunct_inferred2
        form     =P
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
        derived   yes
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
        state    pre_infer_first_conjunct_after_second
        form     =P
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
        derived   yes
        relation  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 5b: check if first conjunct inferred after second, Step 2", string="""
        =g>
        isa      goal
        state    pre_infer_first_conjunct_after_second
        form     =P
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
        derived   yes
        relation  none
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    infer_first_conjunct_after_second
        form     =P
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
        derived   yes
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
        derived   yes
        relation  none
    """)

    aBoxCon.productionstring(name="Module 2, Unit 6a: store in list of used formulas, Step 1", string="""
        =g>
        isa      goal
        state    infer_first_conjunct_after_second
        form     =P
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
        derived   yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    store_in_list
        form     =P
        +imaginal>
        isa      storelist
        thing    storelist
        form     =X
        element  =Y
        mainconnective =Z
        relation =U
        subformula1 =V
        subformula2 =W
        derived  yes
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

    aBoxCon.productionstring(name="Module 2, Unit 6b: label first conjunct as inferred and derived after second, Step 1", string="""
        =g>
        isa      goal
        state    infer_first_conjunct_after_second
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 6b: label first conjunct as inferred and derived after second, Step 2", string="""
        =g>
        isa      goal
        state    retrieve_first_conjunct_after_second
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 2, Unit 6b: label first conjunct as inferred and derived after second, Step 3", string="""
        =g>
        isa      goal
        state    label_first_conjunct_after_second
        form     =P
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
        derived  no
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    module3
        form     =P
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

def module3(aBoxCon): #This module decides if it's worth to look for a clash. If not, it demands some new formula to be derived.
    aBoxCon.productionstring(name="Module 3, Unit 1: check for a clash, find concept, Step 1", string="""
        =g>
        isa      goal
        state    module3
        form     =P
        ?retrieval>
        state    empty
        ?imaginal>
        state    empty
        ==>
        =g>
        isa      goal
        state    prepare1
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~existential
        mainconnective ~universal
        derived  yes
    """)

    aBoxCon.productionstring(name="Module 3, Unit 1: check for a clash, find concept, Step 1", string="""
        =g>
        isa      goal
        state    prepare1
        form     =P
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =Z
        subformula1  =Y
        derived  yes
        ?imaginal>
        state    empty
        ==>
        =g>
        isa      goal
        state    prepare2
        form     =P
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =Z
        subformula1  =Y
        derived  yes
    """)

    aBoxCon.productionstring(name="Module 3, Unit 1: do we need to check for a clash? concept found, Step 1", string="""
        =g>
        isa      goal
        state    prepare2
        form     =P
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =Z
        subformula1  =Y
        derived  yes
        ==>
        =g>
        isa      goal
        state    find_clash
        form     =P
        +imaginal>
        isa      checklist
        thing    checklist
        form     =X
        mainconnective =Z
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


def module4(aBoxCon): #This module retrievs the list of all formulas that are already used. It then chooses a new formula not in the list. If there is no such formula, it confirms consistency.
    aBoxCon.productionstring(name="Module 4, Unit 1: check if there is a formula to store in the list of used formulas, Step 1", string="""
        =g>
        isa      goal
        state    store_in_list
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 4 Unit 2a: store formula in the list of used formulas and repeat, Step 1", string="""
        =g>
        isa      goal
        state    store_in_list2
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 4, Unit 2b: no formula to store, use the list to select the next formula, Step 1", string="""
        =g>
        isa      goal
        state    store_in_list2
        form     =P
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
        form     =P
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

    aBoxCon.productionstring(name="Module 4, Unit 3: all formulas used, confirm consistency, Step 1", string="""
        =g>
        isa      goal
        state    find_rule
        form     =P
        ?retrieval>
        state    error
        ==>
        =g>
        isa     goal
        state   stop
        form     =P
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)
