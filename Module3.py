def module3(aBoxCon): #This module applies when a conjunction is found. It derives both conjuncts.
    aBoxCon.productionstring(name="Module 3, Unit 1, Step 1: conjunction found, put conjunct labels in imaginal and imaginal_action buffers", string="""
        =g>
        isa      goal
        state    module3
        form     =P
        =imaginal>
        isa      proposition
        thing    proposition
        form     =P
        element  =U
        mainconnective conjunction
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
        state    label_conjuncts
        form     =P
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Y
        element  =U
        mainconnective none
        relation none
        subformula1 none
        subformula2 none
        derived  none
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective none
        relation none
        subformula1 none
        subformula2 none
        derived  none
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2a, Step 1: retrieve first conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        derived  ~yes
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  =I
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  =I
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2b, Step 1: retrieve second conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        derived  =I
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  ~yes
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        derived  =I
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2a, Step 2: label first conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        derived  =J
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  =I
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =A
        relation =B
        subformula1 =C
        subformula2 =D
        derived  yes
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  =I
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 2b, Step 2: label second conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts2
        form     =P
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =C
        subformula2  =B
        relation   =A
        derived  =J
        =imaginal>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  =I
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        +imaginal_action>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =C
        subformula2  =B
        relation   =A
        derived  yes
        +imaginal>
        isa      proposition
        thing    proposition
        form     =Z
        element  =U
        mainconnective =E
        relation =F
        subformula1 =G
        subformula2 =H
        derived  =I
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 3a, Step 1: finalise inference and move on to find a clash on first conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective  ~conjunction
        mainconnective  ~disjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  =V
        subformula1  =C
        subformula2  =B
        relation   =A
        derived  yes
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Y
        element  =U
        mainconnective =Z
        subformula1  =D
        subformula2  =E
        relation   =F
        derived  yes
        ==>
        =g>
        isa      goal
        state    find_clash_to_head
        form     =P
        +imaginal>
        isa     checklist
        thing   checklist
        form    =X
        element =U
        mainconnective =V
        relation =A
        subformula1 =C
        subformula2 =B
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        ~retrieval>
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 3b, Step 1: finalise inference and move on to find a clash on second conjunct", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective =V
        subformula1  =C
        subformula2  =B
        relation   =A
        derived  yes
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Y
        element  =U
        mainconnective  ~conjunction
        mainconnective  ~disjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  =Z
        subformula1  =D
        subformula2  =E
        relation   =F
        derived  yes
        ==>
        =g>
        isa      goal
        state    find_clash_to_head
        form     =P
        +imaginal>
        isa     checklist
        thing   checklist
        form    =Y
        element =U
        mainconnective =Z
        relation =F
        subformula1 =D
        subformula2 =E
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        ~retrieval>
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 3, Unit 3c, Step 1: no concept or negation derived, so move on to derive new formula", string="""
        =g>
        isa      goal
        state    label_conjuncts
        form     =P
        ?retrieval>
        state    free
        =imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective =V
        subformula1  =C
        subformula2  =B
        relation   =A
        derived  yes
        =imaginal_action>
        isa      proposition
        thing    proposition
        form     =Y
        element  =U
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective =Z
        subformula1  =D
        subformula2  =E
        relation   =F
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
