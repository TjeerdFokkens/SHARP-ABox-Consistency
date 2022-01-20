def module4(aBoxCon): #This module applies when an existential restriction is found. It derives the relation and concept assignment.
    aBoxCon.productionstring(name="Module 4, Unit 1, Step 1: existential found, derive relation and concept", string="""
        =g>
        isa      goal
        state    inference_step
        form     =P
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
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2a, Step 1: retrieve existential relation", string="""
        =g>
        isa      goal
        state    label_formulas
        form     =P
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
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_formulas2
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Z
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
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2b, Step 1: retrieve existential concept", string="""
        =g>
        isa      goal
        state    label_formulas
        form     =P
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
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_formulas2
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Y
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
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2a, Step 2: put existential relation in imaginal_action buffer", string="""
        =g>
        isa      goal
        state    label_formulas2
        form     =P
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
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    label_formulas
        form     =P
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =Z1
        mainconnective  =Z2
        relation  =Z3
        subformula1  =Z4
        subformula2  =Z5
        derived  yes
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
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2b, Step 2: put existential concept in imaginal buffer", string="""
        =g>
        isa      goal
        state    label_formulas2
        form     =P
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
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    label_formulas
        form     =P
        +imaginal_actional>
        isa      proposition
        thing    proposition
        form     =Y
        element  =Y1
        mainconnective  =Y2
        relation  =Y3
        subformula1  =Y4
        subformula2  =Y5
        derived  =Y6
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
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 4, Unit 3, Step 1: move on to derive new formula", string="""
        =g>
        isa      goal
        state    label_formulas
        form     =P
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        derived  yes
        =imaginal_action>
        isa      proposition
        thing    proposition
        derived  yes
        ==>
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        +retrieval>
        isa      storelist
        thing    storelist
        form     =P
        ~imaginal_action>
        ~imaginal>
    """)
