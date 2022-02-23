def module5(aBoxCon): #This module looks for universal restrictions and the corresponding relations. It makes the appropriate deductions and does so exhaustively.
    aBoxCon.productionstring(name="Module 5, Unit 1, Step 1: update count", string="""
        =g>
        isa     goal
        state   module5
        form    =P
        count   =Q
        mainconnective none
        ?retrieval>
        state   free
        ==>
        =g>
        isa     goal
        state   count_up
        form    =P
        count   =Q
        mainconnective none
        +retrieval>
        isa     count_order
        thing   count_order
        number  =Q
    """)

    aBoxCon.productionstring(name="Module 5, Unit 1, Step 2: update count", string="""
        =g>
        isa     goal
        state   count_up
        form    =P
        count   =Q
        mainconnective none
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
        +retrieval>
        isa     proposition
        thing   proposition
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 1: find universal and create list", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective none
        ?retrieval>
        state   free
        =retrieval>
        isa     proposition
        thing   proposition
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
        isa     proposition
        thing   proposition
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
    """)

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 2: no universal found", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective none
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
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 2: find universal and create list", string="""
        =g>
        isa     goal
        state   find_relation
        form    =P
        count   =Q
        mainconnective =R
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
        isa     proposition
        thing   proposition
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
        count   =B
        mainconnective =R
        +retrieval>
        isa     proposition
        thing   proposition
        element =Z
        concept =D1
        derived no
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
        +imaginal_action>
        isa     proposition
        thing   proposition
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 3: derive formula from universal", string="""
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count   =Q
        mainconnective =R
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
        subformula1 =A8
        subformula2 =A9
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
        isa     proposition
        thing   proposition
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
        subformula1 =A8
        subformula2 =A9
        concept  =Y99
        +imaginal_action>
        isa     proposition
        thing   proposition
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 4: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_relation_2
        form    =P
        count   =B
        mainconnective =Y
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
        subformula1 =A8
        subformula2 =A9
        concept  =Y99
        =imaginal_action>
        isa     proposition
        thing   proposition
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
        isa     proposition
        thing   proposition
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 4: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_relation
        form    =P
        count   =R
        mainconnective =Y
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
        isa     proposition
        thing   proposition
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
        state   find_universal
        form    =P
        count   =R
        mainconnective =Y
        +retrieval>
        isa     proposition
        thing   proposition
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 4: find next relation to universal", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective ~concept
        mainconnective ~negation
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
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
        state   empty
        ?manual>
        state   free
        ==>
        =g>
        isa     goal
        state   stop
        form    =P
        count   =R
        mainconnective none
        +manual>
        isa     _manual
        cmd     press_key
        key     N
    """)

    aBoxCon.productionstring(name="Module 5, Unit 3, Step 1: go to module 1", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective ~none
        mainconnective ~conjunction
        mainconnective ~universal
        mainconnective ~existential
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
        state   empty
        ==>
        =g>
        isa     goal
        state   find_clash_to_head
        form    =P
        count   =Q
        mainconnective none
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

    aBoxCon.productionstring(name="Module 5, Unit 3, Step 2: go to module 2", string="""
        =g>
        isa     goal
        state   find_universal
        form    =P
        count   =R
        mainconnective ~none
        mainconnective ~concept
        mainconnective ~negation
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
        state   empty
        ==>
        =g>
        isa     goal
        state   derive_next_formulas
        form    =P
        count   =Q
        mainconnective none
        +retrieval>
        isa     storelist
        thing   storelist
        form    =P
    """)
