def module5(aBoxCon): #This module finds all relations/roles corresponding to universal restrictions. It makes the appropriate deductions exhaustively.

    aBoxCon.productionstring(name="Module 5, Unit 1a: no relation found, prepare to retrieve next universal", string="""
        =g>
        isa     goal
        state   module5
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        ?retrieval>
        state   error
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y99
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =A1
        form2   =A2
        form3   =A3
        form4   =A4
        form5   =A5
        form6   =A6
        form7   =A7
        form8   =A8
        form9   =A9
        ==>
        =g>
        isa      goal
        state    prepare_find_next_universal
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        ~retrieval>
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    =A1
        form2   =A2
        form3   =A3
        form4   =A4
        form5   =A5
        form6   =A6
        form7   =A7
        form8   =A8
        form9   =A9
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y99
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
    """)

    aBoxCon.productionstring(name="Module 5, Unit 1a: no relation found, find next universal", string="""
        =g>
        isa     goal
        state   prepare_find_next_universal
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        ?retrieval>
        state    free
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y99
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =A1
        form2   =A2
        form3   =A3
        form4   =A4
        form5   =A5
        form6   =A6
        form7   =A7
        form8   =A8
        form9   =A9
        ==>
        =g>
        isa      goal
        state    find_next_universal
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
        form     ~=A
        form     ~=A1
        form     ~=A2
        form     ~=A3
        form     ~=A4
        form     ~=A5
        form     ~=A6
        form     ~=A7
        form     ~=A8
        form     ~=A9
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    =A
        form2   =A1
        form3   =A2
        form4   =A3
        form5   =A4
        form6   =A5
        form7   =A6
        form8   =A7
        form9   =A8
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y99
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
    """)

    aBoxCon.productionstring(name="Module 5, Unit 2a: universal found, back to start of module 5", string="""
        =g>
        isa      goal
        state    find_next_universal
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
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =A
        form2   =A1
        form3   =A2
        form4   =A3
        form5   =A4
        form6   =A5
        form7   =A6
        form8   =A7
        form9   =A8
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
        form    =A
        form2   =A1
        form3   =A2
        form4   =A3
        form5   =A4
        form6   =A5
        form7   =A6
        form8   =A7
        form9   =A8
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

    aBoxCon.productionstring(name="Module 5, Unit 2b: no universal found, retrieve storelist", string="""
        =g>
        isa      goal
        state    find_next_universal
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        ?retrieval>
        state    error
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =A
        form2   =A1
        form3   =A2
        form4   =A3
        form5   =A4
        form6   =A5
        form7   =A6
        form8   =A7
        form9   =A8
        =imaginal_action>
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
        ==>
        =g>
        isa      goal
        state    prepare_non_universal_retrieval
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =L
        derivenew =M
        ~imaginal_action>
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    =A
        form2   =A1
        form3   =A2
        form4   =A3
        form5   =A4
        form6   =A5
        form7   =A6
        form8   =A7
        form9   =A8
        +retrieval>
        isa      storelist
        thing    storelist
        form     =P
    """)

    aBoxCon.productionstring(name="Module 5, Unit 3a: put storelist of used formulas in imaginal buffer and update count", string="""
        =g>
        isa     goal
        state   prepare_non_universal_retrieval
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
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
        state    retrieve_non_universal
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
        +retrieval>
        isa      count_order
        thing    count_order
        number   =Q2
    """)

    aBoxCon.productionstring(name="Module 5, Unit 3a: retrieve non-universal proposition", string="""
        =g>
        isa     goal
        state   retrieve_non_universal
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        =imaginal>
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
        =retrieval>
        isa      count_order
        thing    count_order
        number   =Q2
        successor =Q3
        ?imaginal>
        state    free
        ==>
        =g>
        isa      goal
        state    update_storelist_2
        form     =P
        count1   =Q2
        count2   =Q3
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
    """)

    aBoxCon.productionstring(name="Module 5, Unit 3b: create storelist in imaginal buffer and put used formula in it", string="""
        =g>
        isa      goal
        state    prepare_non_universal_retrieval
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
        state    retrieve_non_universal
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
        +retrieval>
        isa      count_order
        thing    count_order
        number   =Q2
    """)

    aBoxCon.productionstring(name="Module 5, Unit 1b: infer the concept of the related element", string="""
        =g>
        isa     goal
        state   module5
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        =retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        derived yes
        form    =X
        subformula1 =Y
        subformula2 =Z
        subformula3 =Y8
        concept  =Y99
        ?retrieval>
        state   free
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        ==>
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        +retrieval>
        isa     proposition
        thing   ~none
        thing   ~checklist
        thing   ~storelist
        thing   ~universal_list
        thing   ~count_order
        thing   ~role_list
        thing   ~goal
        mainconnective ~relation
        element =Z
        concept =D2
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X
        relation2 =X1
        relation3 =X2
        relation4 =X3
        relation5 =X4
        relation6 =X5
        relation7 =X6
        relation8 =X7
        relation9 =X8
    """)

    aBoxCon.productionstring(name="Module 5, Unit 4a: non-universal formula found, mark as derived", string="""
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        =retrieval>
        isa     proposition
        thing   proposition
        mainconnective  =A1
        derived =A2
        form    =A3
        subformula1 =A4
        subformula2 =A5
        subformula3 =A8
        element =A6
        relation =A7
        concept  =Y99
        ?retrieval>
        state   free
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        ==>
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =A1
        role    =L
        derivenew =M
        +retrieval>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        +imaginal>
        isa     proposition
        thing   proposition
        mainconnective  =A1
        derived yes
        form    =A3
        subformula1 =A4
        subformula2 =A5
        subformula3 =A8
        element =A6
        relation =A7
        concept  =Y99
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
    """)

    aBoxCon.productionstring(name="Module 5, Unit 4b: universal formula found, mark as derived", string="""
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role    =L
        derivenew =M
        =retrieval>
        isa     uproposition
        thing   uproposition
        mainconnective  =A1
        derived =A2
        form    =A3
        subformula1 =A4
        subformula2 =A5
        element =A6
        relation =A7
        concept  =Y99
        count    =A10
        relation1  =A11
        relation2  =A12
        relation3  =A13
        relation4  =A14
        relation5  =A15
        relation6  =A16
        relation7  =A17
        relation8  =A18
        relation9  =A19
        ?retrieval>
        state   free
        =imaginal>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        ==>
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =A1
        role    =L
        derivenew =M
        +retrieval>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        +imaginal>
        isa     uproposition
        thing   uproposition
        mainconnective  =A1
        derived yes
        form    =A3
        subformula1 =A4
        subformula2 =A5
        element =A6
        relation =A7
        concept  =Y99
        count    =A10
        relation1  =A11
        relation2  =A12
        relation3  =A13
        relation4  =A14
        relation5  =A15
        relation6  =A16
        relation7  =A17
        relation8  =A18
        relation9  =A19
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
    """)

    aBoxCon.productionstring(name="Module 5, Unit 5a: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =Y
        role    =L
        derivenew =M
        =retrieval>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        ?retrieval>
        state   free
        =imaginal>
        isa     proposition
        thing   proposition
        mainconnective  =A1
        derived yes
        form    =A3
        subformula1 =A4
        subformula2 =A5
        subformula3 =A8
        element =A6
        relation =A7
        concept  =Y99
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        ==>
        =g>
        isa     goal
        state   module5
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =Y
        role    =L
        derivenew =M
        +retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        relation =C
        derived yes
        subformula1 =B
        form    ~=X1
        form    ~=X2
        form    ~=X3
        form    ~=X4
        form    ~=X5
        form    ~=X6
        form    ~=X7
        form    ~=X8
        form    ~=X9
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
    """)

    aBoxCon.productionstring(name="Module 5, Unit 5b: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =Y
        role    =L
        derivenew =M
        =retrieval>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        ?retrieval>
        state   free
        =imaginal>
        isa     uproposition
        thing   uproposition
        mainconnective  =A1
        derived yes
        form    =A3
        subformula1 =A4
        subformula2 =A5
        element =A6
        relation =A7
        concept  =Y99
        count    =A10
        relation1  =A11
        relation2  =A12
        relation3  =A13
        relation4  =A14
        relation5  =A15
        relation6  =A16
        relation7  =A17
        relation8  =A18
        relation9  =A19
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
        ==>
        =g>
        isa     goal
        state   module5
        form    =P
        count1   =Q1
        count2   =Q2
        mainconnective =Y
        role    =L
        derivenew =M
        +retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        relation =C
        derived yes
        subformula1 =B
        form    ~=X1
        form    ~=X2
        form    ~=X3
        form    ~=X4
        form    ~=X5
        form    ~=X6
        form    ~=X7
        form    ~=X8
        form    ~=X9
        +imaginal>
        isa     universal_list
        thing   universal_list
        form    =Z1
        form2   =Z2
        form3   =Z3
        form4   =Z4
        form5   =Z5
        form6   =Z6
        form7   =Z7
        form8   =Z8
        form9   =Z9
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q2
        form    =A
        element =B
        relation =C
        subformula1 =D1
        subformula2 =D2
        concept  =Y98
        relation1 =X1
        relation2 =X2
        relation3 =X3
        relation4 =X4
        relation5 =X5
        relation6 =X6
        relation7 =X7
        relation8 =X8
        relation9 =X9
    """)
