def module2(aBoxCon): #This module retrieves the list of used formulas and finds one not in the list.
    aBoxCon.productionstring(name="Module 2, Unit 1, Step 1: put storelist of used formulas in imaginal buffer", string="""
        =g>
        isa     goal
        state   derive_next_formulas
        form    =P
        =retrieval>
        isa     storelist
        thing   storelist
        form    =P
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
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    find_formula_not_in_list
        form     =P
        +imaginal>
        isa     storelist
        thing   storelist
        form    =P
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
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 2, Step 1: create storelist in imaginal buffer and put first used formula in it", string="""
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        ?retrieval>
        state    error
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    find_formula_not_in_list
        form     =P
        +imaginal>
        isa      storelist
        thing    storelist
        form     =P
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
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 3, Step 1: retrieve unused formula", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        =imaginal>
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
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    update_storelist
        form     =P
        +retrieval>
        isa      proposition
        thing    proposition
        form     ~=P
        form     ~=A8
        form     ~=A9
        form     ~=A10
        form     ~=A11
        form     ~=A12
        form     ~=A13
        form     ~=A14
        form     ~=A15
        form     ~=A16
        form     ~=A17
        form     ~=A18
        form     ~=A19
        form     ~=A20
        form     ~=A21
        mainconnective ~negation
        mainconnective ~concept
        mainconnective ~universal
        mainconnective ~disjunction
        mainconnective ~none
        derived  yes
        +imaginal>
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
    """)

    aBoxCon.productionstring(name="Module 2, Unit 4a, Step 1: update list of used formulas", string="""
        =g>
        isa      goal
        state    update_storelist
        form     =P
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  yes
        =imaginal>
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
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    inference_step
        form     =X
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  yes
        +imaginal_action>
        isa      storelist
        thing    storelist
        form     =X
        form2    =P
        form3    =A8
        form4    =A9
        form5    =A10
        form6    =A11
        form7    =A12
        form8    =A13
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 4b, Step 1: no formula found, signal consistency", string="""
        =g>
        isa      goal
        state    update_storelist
        form     =P
        ?retrieval>
        state    error
        ?manual>
        state    free
        ==>
        =g>
        isa      goal
        state    stop
        form     =P
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)
