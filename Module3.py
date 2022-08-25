def module3(aBoxCon): #This module applies when a conjunction is found. It derives both conjuncts.
    aBoxCon.productionstring(name="Module 3, Unit 1: conjunction found, put conjunct labels in imaginal and imaginal_action buffers", string="""
        =g>
        isa      goal
        state    inference_step
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa      proposition
        thing    proposition
        form     =P
        element  =U
        mainconnective conjunction
        subformula1  =Y
        subformula2  =Z
        subformula3  =X8
        derived  yes
        relation =V
        concept  =Y99
        =imaginal_action>
        isa      storelist
        thing    storelist
        form     =P
        form2    =A8
        form3    =A9
        form4    =A10
        form5    =A11
        form6    =A12
        form7    =A13
        form8    =A14
        form9    =A15
        form10   =A16
        form11   =A17
        form12   =A18
        form13   =A19
        form14   =A20
        form15   =A21
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =U
        mainconnective none
        relation none
        subformula1 none
        subformula2 none
        subformula3 none
        derived  none
        concept  none
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective none
        relation none
        subformula1 none
        subformula2 none
        subformula3 none
        derived  none
        concept  none
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2a, Step 1: retrieve first conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa      proposition
        thing    ~checklist
        thing    ~storelist
        thing    ~universal_list
        thing    ~goal
        thing    ~count_order
        thing    ~role_list
        thing    =K1
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        subformula3 =X8
        derived  ~yes
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    ~checklist
        thing    ~storelist
        thing    ~universal_list
        thing    ~goal
        thing    ~count_order
        thing    ~role_list
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +retrieval>
        isa      proposition
        thing    ~checklist
        thing    ~storelist
        thing    ~universal_list
        thing    ~goal
        thing    ~count_order
        thing    ~role_list
        form     =X
        element  =U
        mainconnective ~none
        +imaginal_action>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2b, Step 1: retrieve second conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa      proposition
        thing    ~checklist
        thing    ~storelist
        thing    ~universal_list
        thing    ~goal
        thing    ~count_order
        thing    ~role_list
        thing    =K1
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        subformula3 =X8
        derived  =I
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    ~checklist
        thing    ~storelist
        thing    ~universal_list
        thing    ~goal
        thing    ~count_order
        thing    ~role_list
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  ~yes
        concept  =Y98
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +retrieval>
        isa      proposition
        thing    ~checklist
        thing    ~storelist
        thing    ~universal_list
        thing    ~goal
        thing    ~count_order
        thing    ~role_list
        form     =Z
        element  =U
        mainconnective ~none
        +imaginal>
        isa      proposition
        thing    =K1
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        subformula3 =X8
        derived  =I
        concept  =Y99
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2a, Step 2: label first conjunct, non-universal found", string="""
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        subformula3 =X8
        derived  =J
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        subformula3 =X8
        derived  yes
        concept  =Y99
        +imaginal_action>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2a, Step 2: label first conjunct, universal found", string="""
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =retrieval>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =U
        mainconnective universal
        relation =B
        subformula1 =C
        subformula2 =D
        derived  =J
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =U
        mainconnective universal
        relation =B
        subformula1 =C
        subformula2 =D
        derived  yes
        concept  =Y99
        count     =Q1
        relation1 none
        relation2 none
        relation3 none
        relation4 none
        relation5 none
        relation6 none
        relation7 none
        relation8 none
        relation9 none
        +imaginal_action>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2b, Step 2: label second conjunct, non-universal found", string="""
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =C
        subformula2  =B
        subformula3 =X8
        relation   =A
        derived  =J
        concept  =Y99
        =imaginal>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =C
        subformula2  =B
        subformula3 =X8
        relation   =A
        derived  yes
        concept  =Y99
        +imaginal>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2b, Step 2: label second conjunct, universal found", string="""
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =retrieval>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =U
        mainconnective universal
        relation =B
        subformula1 =C
        subformula2 =D
        derived  =J
        concept  =Y99
        =imaginal>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal_action>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =U
        mainconnective universal
        relation =B
        subformula1 =C
        subformula2 =D
        derived  yes
        concept  =Y99
        count     =Q1
        relation1 none
        relation2 none
        relation3 none
        relation4 none
        relation5 none
        relation6 none
        relation7 none
        relation8 none
        relation9 none
        +imaginal>
        isa      proposition
        thing    =K2
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        subformula3 =X9
        derived  =I
        concept  =Y98
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 3a: finalise inference and move on to find a clash on first conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    =K1
        form     =X
        element  =U
        mainconnective  ~conjunction
        mainconnective  ~disjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~none
        mainconnective  =V
        subformula1  =C
        subformula2  =B
        subformula3 =X8
        relation   =A
        derived  yes
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    =K2
        form     =Y
        element  =U
        mainconnective =Z
        subformula1  =D
        subformula2  =E
        subformula3 =X9
        relation   =F
        derived  yes
        concept  =Y98
        ==>
        =g>
        isa      goal
        state    find_clash_to_head
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal>
        isa     checklist
        thing   checklist
        form    =X
        element =U
        mainconnective =V
        relation =A
        subformula1 =C
        subformula2 =B
        concept  =Y99
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
        form16   none
        ~retrieval>
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 3b: finalise inference and move on to find a clash on second conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    =K1
        form     =X
        element  =U
        mainconnective =V
        subformula1  =C
        subformula2  =B
        subformula3 =X8
        relation   =A
        derived  yes
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    =K2
        form     =Y
        element  =U
        mainconnective  ~conjunction
        mainconnective  ~disjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~none
        mainconnective  =Z
        subformula1  =D
        subformula2  =E
        subformula3 =X9
        relation   =F
        derived  yes
        concept  =Y98
        ==>
        =g>
        isa      goal
        state    find_clash_to_head
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal>
        isa     checklist
        thing   checklist
        form    =Y
        element =U
        mainconnective =Z
        relation =F
        subformula1 =D
        subformula2 =E
        concept  =Y98
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
        form16   none
        ~retrieval>
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 3c: no concept or negation derived, so move on to derive new formula", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    =K1
        form     =X
        element  =U
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective =V
        subformula1  =C
        subformula2  =B
        subformula3 =X8
        relation   =A
        derived  yes
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    =K2
        form     =Y
        element  =U
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective =Z
        subformula1  =D
        subformula2  =E
        subformula3 =X9
        relation   =F
        derived  yes
        concept  =Y98
        ==>
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +retrieval>
        isa      storelist
        thing    storelist
        form     =P
        ~imaginal_action>
        ~imaginal>
    """)
