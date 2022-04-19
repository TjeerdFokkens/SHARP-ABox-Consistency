def module5(aBoxCon): #This module looks for universal restrictions and the corresponding relations. It makes the appropriate deductions and does so exhaustively.
    aBoxCon.productionstring(name="Module 5, Unit 1: update count, retrieve count order", string="""
        =g>
        isa     goal
        state   module5
        form    =P
        count   =Q
        mainconnective none
        role    =L
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   count_up
        form    =P
        count   =Q
        mainconnective none
        role    =L
        +retrieval>
        isa     count_order
        thing   count_order
        number  =Q
    """)

    aBoxCon.productionstring(name="Module 5, Unit 1: update count, retrieve universal", string="""
        =g>
        isa     goal
        state   count_up
        form    =P
        count   =Q
        mainconnective none
        role    =L
        =retrieval>
        isa     count_order
        thing   count_order
        number  =Q
        successor =R
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective none
        role    =L
        +retrieval>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q
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
    """)

    aBoxCon.productionstring(name="Module 5, Unit 2: universal found, find relation", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective none
        role    =L
        ?retrieval>
        state   free
        =retrieval>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q
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
        isa     goal
        state   find_relation
        form    =P
        count   =R
        mainconnective none
        role    =L
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
        form    =A
        form2   =A1
        form3   =A2
        form4   =A3
        form5   =A4
        form6   =A5
        form7   =A6
        form8   =A7
        form9   =A8
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =R
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

    aBoxCon.productionstring(name="Module 5, Unit 2: no universal found, confirm consistency", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective none
        role    =L
        ?retrieval>
        state   error
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        form    =P
        count   =R
        mainconnective none
        role    =L
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)

    aBoxCon.productionstring(name="Module 5, Unit 3: infer the concept of the related element", string="""
        =g>
        isa     goal
        state   find_relation
        form    =P
        count   =Q
        mainconnective =R
        role    =L
        =retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        derived yes
        form    =X
        subformula1 =Y
        subformula2 =Z
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
        count   =Q
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
        count   =Q
        mainconnective =R
        role    =L
        +retrieval>
        isa     proposition
        thing   ~none
        thing   ~checklist
        thing   ~storelist
        thing   ~universal_list
        thing   ~count_order
        thing   ~role_list
        thing   ~goal
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
        count   =Q
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

    aBoxCon.productionstring(name="Module 5, Unit 3a: non-universal formula found, mark as derived", string="""
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count   =Q
        mainconnective =R
        role    =L
        =retrieval>
        isa     proposition
        thing   proposition
        mainconnective  =A1
        derived =A2
        form    =A3
        subformula1 =A4
        subformula2 =A5
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
        count   =Q
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
        count   =Q
        mainconnective =A1
        role    =L
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
        element =A6
        relation =A7
        concept  =Y99
        +imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q
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

    aBoxCon.productionstring(name="Module 5, Unit 3b: universal formula found, mark as derived", string="""
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count   =Q
        mainconnective =R
        role    =L
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
        count   =Q
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
        count   =B
        mainconnective =A1
        role    =L
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
        count   =Q
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

    aBoxCon.productionstring(name="Module 5, Unit 4a: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count   =Q
        mainconnective =Y
        role    =L
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
        element =A6
        relation =A7
        concept  =Y99
        =imaginal_action>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        count   =Q
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
        state   find_relation
        form    =P
        count   =Q
        mainconnective =Y
        role    =L
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
        count   =Q
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

    aBoxCon.productionstring(name="Module 5, Unit 4b: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count   =B
        mainconnective =Y
        role    =L
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
        count   =Q
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
        state   find_relation
        form    =P
        count   =R
        mainconnective =Y
        role    =L
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
        count   =Q
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

    aBoxCon.productionstring(name="Module 5, Unit 5: no relation found, find next universal", string="""
        =g>
        isa     goal
        state   find_relation
        form    =P
        count   =R
        mainconnective =Y
        role    =L
        ?retrieval>
        state   error
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
        count   =R
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
        state   find_universal
        form    =P
        count   =R
        mainconnective =Y
        role    =L
        +retrieval>
        isa     uproposition
        thing   uproposition
        mainconnective  universal
        derived yes
        form    ~=Z1
        form    ~=Z2
        form    ~=Z3
        form    ~=Z4
        form    ~=Z5
        form    ~=Z6
        form    ~=Z7
        form    ~=Z8
        form    ~=Z9
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
        ~imaginal_action>
    """)

    aBoxCon.productionstring(name="Module 5, Unit 6: go to module 1", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective ~none
        mainconnective ~conjunction
        mainconnective ~universal
        mainconnective ~existential
        role    =L
        ?retrieval>
        state   error
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
        ?imaginal_action>
        buffer  empty
        ==>
        =g>
        isa     goal
        state   find_clash_to_head
        form    =P
        count   =R
        mainconnective none
        role    =L
        ~retrieval>
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
    """)

    aBoxCon.productionstring(name="Module 5, Unit 6: go to module 2", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective ~none
        mainconnective ~concept
        mainconnective ~negation
        role    =L
        ?retrieval>
        state   error
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
        ?imaginal_action>
        buffer  empty
        ==>
        =g>
        isa     goal
        state   derive_next_formulas
        form    =P
        count   =R
        mainconnective none
        role    =L
        +retrieval>
        isa     storelist
        thing   storelist
        form    =P
    """)
