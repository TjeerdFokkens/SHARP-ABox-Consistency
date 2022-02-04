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
        form2   none
        form3   none
        form4   none
        form5   none
        form6   none
        form7   none
        form8   none
        form9   none
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 1: find universal and create list", string="""
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
        mainconnective none
        =retrieval>
        isa     proposition
        thing   proposition
        mainconnective  relation
        derived yes
        form    =X
        subformula1 =Y
        subformula2 =Z
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
        mainconnective none
        +retrieval>
        isa     proposition
        thing   proposition
        element =Z
        subformula1 =D1
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

    aBoxCon.productionstring(name="Module 5, Unit 2, Step 2: find universal and create list", string="""
        =g>
        isa     goal
        state   deduce_from_universal
        form    =P
        count   =Q
        mainconnective none
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
        state   find_relation_variant
        form    =P
        count   =B
        mainconnective =A1
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
