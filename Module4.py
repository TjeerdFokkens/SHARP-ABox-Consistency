def module4(aBoxCon): #This module applies when an existential restriction is found. It derives the relation and concept assignment.
    aBoxCon.productionstring(name="Module 4, Unit 1: existential found, derive relation and concept", string="""
        =g>
        isa      goal
        state    inference_step
        form     =P
        count    =Q
        mainconnective none
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective existential
        subformula1  =Y
        subformula2  =Z
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
        ==>
        =g>
        isa      goal
        state    label_formulas
        form     =P
        count   =Q
        mainconnective none
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  none
        mainconnective  none
        relation  none
        subformula1  none
        subformula2  none
        derived  none
        concept  none
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  none
        mainconnective  none
        relation  none
        subformula1  none
        subformula2  none
        derived  none
        concept  none
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2a, Step 1: retrieve existential relation", string="""
        =g>
        isa      goal
        state    label_formulas
        form     =P
        count   =Q
        mainconnective none
        =imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  ~yes
        concept  =Y98
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_formulas2
        form     =P
        count   =Q
        mainconnective none
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Z
        subformula1  ~none
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
        concept  =Y99
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  none
        concept  =Y98
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2b, Step 1: retrieve existential concept", string="""
        =g>
        isa      goal
        state    label_formulas
        form     =P
        count   =Q
        mainconnective none
        =imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  ~yes
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  =Z6
        concept  =Y98
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_formulas2
        form     =P
        count   =Q
        mainconnective none
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Y
        element  ~none
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  none
        concept  =Y99
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  =Z6
        concept  =Y98
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2a, Step 2: put existential relation in imaginal_action buffer", string="""
        =g>
        isa      goal
        state    label_formulas2
        form     =P
        count   =Q
        mainconnective none
        =retrieval>
        isa      proposition
        thing    proposition
        form     =Z
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  =Z6
        concept  =Y99
        =imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
        concept  =Y98
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  ~yes
        concept  =Y97
        ==>
        =g>
        isa      goal
        state    label_formulas
        form     =P
        count   =Q
        mainconnective none
        ~retrieval>
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
        concept  =Y98
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  none
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  yes
        concept  =Y97
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2b, Step 2: put existential concept in imaginal buffer", string="""
        =g>
        isa      goal
        state    label_formulas2
        form     =P
        count   =Q
        mainconnective none
        =retrieval>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  =Z6
        concept  =Y99
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        form     =Z
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  ~yes
        concept  =Y98
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
        concept  =Y97
        ==>
        =g>
        isa      goal
        state    label_formulas
        form     =P
        count   =Q
        mainconnective none
        ~retrieval>
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  yes
        concept  =Y99
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
        concept  =Y97
    """)

    aBoxCon.productionstring(name="Module 4, Unit 3: move on to derive new formula", string="""
        =g>
        isa      goal
        state    label_formulas
        form     =P
        count   =Q
        mainconnective none
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =U
        mainconnective  ~relation
        mainconnective  ~none
        subformula1  =D
        subformula2  =E
        relation   =F
        derived  yes
        concept  =Y99
        =imaginal_action>
        isa      proposition
        thing    proposition
        mainconnective relation
        form     =V1
        element  =V2
        subformula1  =V4
        subformula2  =V5
        relation   =V6
        derived  yes
        concept  =Y98
        ==>
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count   =Q
        mainconnective none
        +retrieval>
        isa      storelist
        thing    storelist
        form     =P
        ~imaginal>
        ~imaginal_action>
    """)
