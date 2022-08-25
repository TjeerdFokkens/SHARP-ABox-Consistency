def module1(aBoxCon): #This module looks for concept assignments and negated concept assignments and tries to find a clash. If there is no clash, some new formula needs to be derived.
    aBoxCon.productionstring(name="Module 1, Unit 1: find clash to concept or negation in head of list", string="""
        =g>
        isa     goal
        state   find_clash_to_head
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        +retrieval>
        isa     proposition
        thing   proposition
        element =A2
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        mainconnective ~relation
        mainconnective ~=A3
        mainconnective ~none
        form    ~=A1
        form    ~=A7
        form    ~=A8
        form    ~=A9
        form    ~=A10
        form    ~=A11
        form    ~=A12
        form    ~=A13
        form    ~=A14
        form    ~=A15
        form    ~=A16
        form    ~=A17
        form    ~=A18
        form    ~=A19
        form    ~=A20
        form    ~=A21
        subformula1 =A5
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2a: find concept or negation not in the list", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        ?retrieval>
        state   error
        ==>
        =g>
        isa      goal
        state    add_formula_to_list
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        +retrieval>
        isa     proposition
        thing   proposition
        derived yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        mainconnective ~relation
        mainconnective ~none
        form    ~=A1
        form    ~=A7
        form    ~=A8
        form    ~=A9
        form    ~=A10
        form    ~=A11
        form    ~=A12
        form    ~=A13
        form    ~=A14
        form    ~=A15
        form    ~=A16
        form    ~=A17
        form    ~=A18
        form    ~=A19
        form    ~=A20
        form    ~=A21
    """)

    aBoxCon.productionstring(name="Module 1, Unit 2b: signal a clash", string="""
        =g>
        isa     goal
        state   find_formula_not_in_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        =retrieval>
        isa     proposition
        thing   proposition
        element  =A2
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~universal
        mainconnective ~existential
        mainconnective ~relation
        mainconnective ~=A3
        mainconnective ~none
        subformula1 =A5
        derived yes
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        +manual>
        isa     _manual
        cmd     press_key
        key     C
    """)

    aBoxCon.productionstring(name="Module 1, Unit 3a: no formula found, need to derive new ones", string="""
        =g>
        isa     goal
        state   add_formula_to_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash no
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        ?retrieval>
        state   error
        ==>
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash no
        +retrieval>
        isa     storelist
        thing   storelist
        form    =P
        ~imaginal>
    """)

    aBoxCon.productionstring(name="Module 1, Unit 3b: add formula to list and find a clash", string="""
        =g>
        isa     goal
        state   add_formula_to_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash =M
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =A2
        concept  =B
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
        =retrieval>
        isa      proposition
        thing    proposition
        derived  yes
        form     =X1
        element  =X2
        mainconnective =X3
        relation =X4
        subformula1 =X5
        subformula2 =X6
        concept  =X7
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
        form    =X1
        element =X2
        mainconnective =X3
        relation =X4
        subformula1 =X5
        subformula2 =X6
        concept  =X7
        form2    =A1
        form3    =A7
        form4    =A8
        form5    =A9
        form6    =A10
        form7    =A11
        form8    =A12
        form9    =A13
        form10   =A14
        form11   =A15
        form12   =A16
        form13   =A17
        form14   =A18
        form15   =A19
        form16   =A20
        ~retrieval>
    """)

    aBoxCon.productionstring(name="Module 1, Unit 4: no formula found, signal consistency", string="""
        =g>
        isa     goal
        state   add_formula_to_list
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        checkclash yes
        =imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        concept  =X7
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
        form9    =A14
        form10   =A15
        form11   =A16
        form12   =A17
        form13   =A18
        form14   =A19
        form15   =A20
        form16   =A21
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
