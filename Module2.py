def module2(aBoxCon): #This module either retrieves the list of used formulas and finds one not in the list, or it finds a universal restriction.
    aBoxCon.productionstring(name="Module 2, Unit 1: put storelist of used formulas in imaginal buffer", string="""
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        =retrieval>
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
        derivenew =M
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 1: create storelist in imaginal buffer and put first used formula in it", string="""
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
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
        derivenew =M
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
        form16   none
        form17   none
        form18   none
        form19   none
        form20   none
    """)

    aBoxCon.productionstring(name="Module 2, Unit 2a: retrieve non-universal formula", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
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
        state    update_storelist_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
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
        form     ~=A22
        form     ~=A23
        form     ~=A24
        form     ~=A25
        form     ~=A26
        mainconnective ~negation
        mainconnective ~concept
        mainconnective ~disjunction
        mainconnective ~relation
        mainconnective ~none
        mainconnective ~universal
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
    """)

    aBoxCon.productionstring(name="Module 2, Unit 2b: retrieve universal formula", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
        ==>
        =g>
        isa      goal
        state    prepare_module_5_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
    """)

    aBoxCon.productionstring(name="Module 2, Unit 3a: non-universal found, update list of used formulas", string="""
        =g>
        isa      goal
        state    update_storelist_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        subformula3  =X6
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
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
        derivenew =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        subformula3  =X6
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
        form16   =A21
        form17   =A22
        form18   =A23
        form19   =A24
        form20   =A25
    """)

    aBoxCon.productionstring(name="Module 2, Unit 3b: universal found, prepare for module 5", string="""
        =g>
        isa      goal
        state    prepare_module_5_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
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
        count    ~=Q2
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
        derivenew =M
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

    aBoxCon.productionstring(name="Module 2, Unit 4a: retrieve non-universal after universal", string="""
        =g>
        isa      goal
        state    prepare_module_5_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
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
        derivenew =M
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
        form     ~=A22
        form     ~=A23
        form     ~=A24
        form     ~=A25
        form     ~=A26
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
    """)

    aBoxCon.productionstring(name="Module 2, Unit 4b: retrieve universal after non-universal", string="""
        =g>
        isa      goal
        state    update_storelist_1
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
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
        derivenew =M
        +retrieval>
        isa      uproposition
        thing    uproposition
        mainconnective universal
        derived  yes
        count    ~=Q2
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 2, Unit 5a: universal found after non-universal, go to module 5", string="""
        =g>
        isa      goal
        state    prepare_module_5_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
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
        count    ~=Q2
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
        derivenew =M
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
        derivenew =M
        =retrieval>
        isa      proposition
        thing    proposition
        form     =X
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        subformula3  =X6
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
        form16   =A22
        form17   =A23
        form18   =A24
        form19   =A25
        form20   =A26
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
        derivenew =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =X1
        mainconnective  =X2
        relation  =X3
        subformula1  =X4
        subformula2  =X5
        subformula3  =X6
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
        form16   =A21
        form17   =A22
        form18   =A23
        form19   =A24
        form20   =A25
    """)

    aBoxCon.productionstring(name="Module 2, Unit 7a: no formula found, last check for clash", string="""
        =g>
        isa      goal
        state    prepare_module_5_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        ?retrieval>
        state    error
        ?manual>
        state    free
        ==>
        =g>
        isa      goal
        state    last_clash
        derivenew =M
    """)

    aBoxCon.productionstring(name="Module 2, Unit 7b: no formula found, last check for clash", string="""
        =g>
        isa      goal
        state    update_storelist_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        ?retrieval>
        state    error
        ?manual>
        state    free
        ==>
        =g>
        isa      goal
        state    last_clash
        derivenew =M
    """)

    aBoxCon.productionstring(name="Module 2, Unit 8: prepare for last check for a clash", string="""
        =g>
        isa      goal
        state    last_clash
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        ?retrieval>
        state    error
        ?manual>
        state    free
        ==>
        =g>
        isa      goal
        state    find_clash_to_head
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew no
        +imaginal>
        isa     checklist
        thing   checklist
        form    none
        element none
        concept  none
        mainconnective none
        relation none
        subformula1 none
        subformula2 none
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
    """)
