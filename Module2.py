def module2(aBoxCon): #This module either retrieves the list of used formulas and finds one not in the list, or it finds a universal restriction.
    aBoxCon.productionstring(name="Module 2, Unit 1: put storelist of used formulas in imaginal buffer", string="""
        =g>
        isa     goal
        state   derive_next_formulas
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
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
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        +imaginal>
        isa     storelist
        thing   storelist
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
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 2: create storelist in imaginal buffer and put first used formula in it", string="""
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        ?retrieval>
        state    error
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    find_formula_not_in_list
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
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
    """)

    aBoxCon.productionstring(name="Module 2, Unit 3a: retrieve non-universal formula", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
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
        state    update_storelist_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        mainconnective ~disjunction
        mainconnective ~relation
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

    aBoxCon.productionstring(name="Module 2, Unit 3b: retrieve universal formula", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
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
        ==>
        =g>
        isa      goal
        state    prepare_module_5_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        +retrieval>
        isa      uproposition
        thing    uproposition
        mainconnective universal
        derived  yes
        count    =Q1
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

    aBoxCon.productionstring(name="Module 2, Unit 4a: non-universal found, update list of used formulas and count", string="""
        =g>
        isa      goal
        state    update_storelist_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        concept  =Y
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
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        concept  =Y
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
    """)

    aBoxCon.productionstring(name="Module 2, Unit 4b: universal found, prepare for module 5", string="""
        =g>
        isa      goal
        state    prepare_module_5_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        =retrieval>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =X1
        mainconnective  universal
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  yes
        concept  =Y
        count    =Q1
        relation1  =Y2
        relation2  =Y3
        relation3  =Y4
        relation4  =Y5
        relation5  =Y6
        relation6  =Y7
        relation7  =Y8
        relation8  =Y9
        relation9  =Y10
        ?imaginal>
        state    free
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    module5
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        +imaginal_action>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =X1
        mainconnective  universal
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  yes
        concept  =Y
        count    =Q2
        relation1  =Y2
        relation2  =Y3
        relation3  =Y4
        relation4  =Y5
        relation5  =Y6
        relation6  =Y7
        relation7  =Y8
        relation8  =Y9
        relation9  =Y10
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    none
        form2   none
        form3   none
        form4   none
        form5   none
        form6   none
        form7   none
        form8   none
        form9   none
        +retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        relation =X3
        derived yes
        subformula1 =X1
        form    ~=Y10
        form    ~=Y2
        form    ~=Y3
        form    ~=Y4
        form    ~=Y5
        form    ~=Y6
        form    ~=Y7
        form    ~=Y8
        form    ~=Y9
    """)

    aBoxCon.productionstring(name="Module 2, Unit 5a: retrieve non-universal after universal", string="""
        =g>
        isa      goal
        state    prepare_module_5_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        ?retrieval>
        state    error
        ==>
        =g>
        isa      goal
        state    update_storelist_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        mainconnective ~disjunction
        mainconnective ~relation
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

    aBoxCon.productionstring(name="Module 2, Unit 5b: retrieve universal after non-universal", string="""
        =g>
        isa      goal
        state    update_storelist_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        ?retrieval>
        state    error
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
        state    prepare_module_5_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        +retrieval>
        isa      uproposition
        thing    uproposition
        mainconnective universal
        derived  yes
        count    =Q1
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 4b: universal found after non-universal, go to module 5", string="""
        =g>
        isa      goal
        state    prepare_module_5_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        =retrieval>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =X1
        mainconnective  universal
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  yes
        concept  =Y
        count    =Q1
        relation1  =Y2
        relation2  =Y3
        relation3  =Y4
        relation4  =Y5
        relation5  =Y6
        relation6  =Y7
        relation7  =Y8
        relation8  =Y9
        relation9  =Y10
        ?imaginal>
        state    free
        ?imaginal_action>
        state    free
        ==>
        =g>
        isa      goal
        state    module5
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        +imaginal_action>
        isa      uproposition
        thing    uproposition
        form     =X
        element  =X1
        mainconnective  universal
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        derived  yes
        concept  =Y
        count    =Q2
        relation1  =Y2
        relation2  =Y3
        relation3  =Y4
        relation4  =Y5
        relation5  =Y6
        relation6  =Y7
        relation7  =Y8
        relation8  =Y9
        relation9  =Y10
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    none
        form2   none
        form3   none
        form4   none
        form5   none
        form6   none
        form7   none
        form8   none
        form9   none
        +retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        relation =X3
        derived yes
        subformula1 =X1
        form    ~=Y10
        form    ~=Y2
        form    ~=Y3
        form    ~=Y4
        form    ~=Y5
        form    ~=Y6
        form    ~=Y7
        form    ~=Y8
        form    ~=Y9
    """)

    aBoxCon.productionstring(name="Module 2, Unit 6a: non-universal found after universal, update list of used formulas", string="""
        =g>
        isa      goal
        state    update_storelist_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        concept  =Y
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
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
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
        concept  =Y
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
    """)

    aBoxCon.productionstring(name="Module 2, Unit 7a: no formula found, signal consistency", string="""
        =g>
        isa      goal
        state    prepare_module_5_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        ?retrieval>
        state    error
        ?manual>
        state    free
        ==>
        =g>
        isa      goal
        state    stop
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)

    aBoxCon.productionstring(name="Module 2, Unit 7b: no formula found, signal consistency", string="""
        =g>
        isa      goal
        state    update_storelist_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        ?retrieval>
        state    error
        ?manual>
        state    free
        ==>
        =g>
        isa      goal
        state    stop
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)
