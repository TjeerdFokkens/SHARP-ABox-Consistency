def module4(aBoxCon): #This module applies when an existential restriction is found. It derives the relation and concept assignment.
    aBoxCon.productionstring(name="Module 4, Unit 1: existential found, get role list", string="""
        =g>
        isa      goal
        state    inference_step
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
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
        concept  =Y99
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
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    get_role_list
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective existential
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation =V
        concept  =Y99
        +imaginal_action>
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
        +retrieval>
        isa      role_list
        thing    role_list
        role1    =R
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2a: no role list found, make one", string="""
        =g>
        isa      goal
        state    get_role_list
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
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
        concept  =Y99
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
        ?retrieval>
        state    error
        ==>
        =g>
        isa      goal
        state    label_role
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective existential
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation =V
        concept  =Y99
        +imaginal_action>
        isa      role_list
        thing    role_list
        role1    none
        role2    none
        role3    none
        role4    none
        role5    none
        role6    none
        role7    none
        role8    none
        role9    none
        role10   none
        +retrieval>
        isa      proposition
        thing    proposition
        mainconnective  relation
        subformula1  =U
        subformula2  ~=U
    """)

    aBoxCon.productionstring(name="Module 4, Unit 2b: role list found, select role not in list", string="""
        =g>
        isa      goal
        state    get_role_list
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
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
        concept  =Y99
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
        =retrieval>
        isa      role_list
        thing    role_list
        role1    =R
        role2    =B2
        role3    =B3
        role4    =B4
        role5    =B5
        role6    =B6
        role7    =B7
        role8    =B8
        role9    =B9
        role10   =B10
        ?retrieval>
        state   free
        ==>
        =g>
        isa      goal
        state    label_role
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        form     =X
        element  =U
        mainconnective existential
        subformula1  =Y
        subformula2  =Z
        derived  yes
        relation =V
        concept  =Y99
        +imaginal_action>
        isa      role_list
        thing    role_list
        role1    =B1
        role2    =B2
        role3    =B3
        role4    =B4
        role5    =B5
        role6    =B6
        role7    =B7
        role8    =B8
        role9    =B9
        role10   =B10
        +retrieval>
        isa      proposition
        thing    proposition
        mainconnective  relation
        subformula1  =U
        subformula2  ~=U
        form     ~=B1
        form     ~=B2
        form     ~=B3
        form     ~=B4
        form     ~=B5
        form     ~=B6
        form     ~=B7
        form     ~=B8
        form     ~=B9
        form     ~=B10
    """)

    aBoxCon.productionstring(name="Module 4, Unit 3: label role, find concept", string="""
        =g>
        isa      goal
        state    label_role
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =R
        checkclash =M
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
        concept  =Y99
        =imaginal_action>
        isa      role_list
        thing    role_list
        role1    =B1
        role2    =B2
        role3    =B3
        role4    =B4
        role5    =B5
        role6    =B6
        role7    =B7
        role8    =B8
        role9    =B9
        role10   =B10
        =retrieval>
        isa      proposition
        thing    proposition
        mainconnective  relation
        subformula1  =U
        subformula2  =W1
        form     =W2
        concept  none
        relation =W3
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    label_concept
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        mainconnective  relation
        subformula1  =U
        subformula2  =W1
        form     =W2
        concept  none
        relation =W3
        derived  yes
        +imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
        +retrieval>
        isa      proposition
        thing    proposition
        element  =W1
        concept  =Y99
        mainconnective ~relation
    """)

    aBoxCon.productionstring(name="Module 4, Unit 4a: label concept, atom found", string="""
        =g>
        isa      goal
        state    label_concept
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        =imaginal>
        isa      proposition
        thing    proposition
        mainconnective  relation
        subformula1  =U
        subformula2  =W1
        form     =W2
        concept  none
        relation =W3
        derived  yes
        =imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
        ?retrieval>
        state   free
        =retrieval>
        isa      proposition
        thing    proposition
        element  =W1
        concept  =Y99
        form     =A1
        mainconnective  =A2
        mainconnective  ~conjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~disjunction
        mainconnective  ~none
        relation =A3
        subformula1  =A4
        subformula2  =A5
        derived  =A6
        ==>
        =g>
        isa      goal
        state    label_concept_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        element  =W1
        concept  =Y99
        form     =A1
        mainconnective  =A2
        relation =A3
        subformula1  =A4
        subformula2  =A5
        derived  yes
        +imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
    """)

    aBoxCon.productionstring(name="Module 4, Unit 4a: atom found, prepare to look for clash", string="""
        =g>
        isa      goal
        state    label_concept_2
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        =imaginal>
        isa      proposition
        thing    proposition
        element  =W1
        concept  =Y99
        form     =A1
        mainconnective  =A2
        mainconnective  ~conjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~disjunction
        mainconnective  ~none
        relation =A3
        subformula1  =A4
        subformula2  =A5
        derived  yes
        =imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
        ?retrieval>
        state    free
        ==>
        =g>
        isa      goal
        state    find_clash_to_head
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        +imaginal>
        isa     checklist
        thing   checklist
        form    =A1
        element =W1
        concept  =Y99
        mainconnective =A2
        relation =A3
        subformula1 =A4
        subformula2 =A5
        form2    none
        form3    none
        form4    none
        form5    none
        form6    none
        form7    none
        form8    none
        +imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
        +retrieval>
        isa      storelist
        thing    storelist
        form     =P
    """)

    aBoxCon.productionstring(name="Module 4, Unit 4b: label concept, complex formula found", string="""
        =g>
        isa      goal
        state    label_concept
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        =imaginal>
        isa      proposition
        thing    proposition
        mainconnective  relation
        subformula1  =U
        subformula2  =W1
        form     =W2
        concept  none
        relation =W3
        derived  yes
        =imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
        =retrieval>
        isa      proposition
        thing    proposition
        element  =W1
        concept  =Y99
        form     =A1
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective  =A2
        relation =A3
        subformula1  =A4
        subformula2  =A5
        derived  =A6
        ?retrieval>
        state   free
        ==>
        =g>
        isa      goal
        state    derive_next_formulas
        form     =P
        count1   =Q1
        count2   =Q2
        mainconnective =R
        role     =W2
        checkclash =M
        +imaginal>
        isa      proposition
        thing    proposition
        element  =W1
        concept  =Y99
        form     =A1
        mainconnective  =A2
        relation =A3
        subformula1  =A4
        subformula2  =A5
        derived  yes
        +imaginal_action>
        isa      role_list
        thing    role_list
        role1    =W2
        role2    =B1
        role3    =B2
        role4    =B3
        role5    =B4
        role6    =B5
        role7    =B6
        role8    =B7
        role9    =B8
        role10   =B9
        +retrieval>
        isa      storelist
        thing    storelist
        form     =P
    """)
