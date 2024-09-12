#Overview
#This Component makes derivations from an existential restriction concept assignment.
#It derives a concept assignment and a role assignment.

#A role_list is used to retrieve a role assignment that does not appear in the list to make sure it is new, as the application of the syntax expansion rules require the related element to be new.
#Some rules come in two variants that function the same way in principle, but are formally different because of the formal difference between universal and non-universal formula chunks.

def component4(aBoxCon):
    #This rule retrieves a role list with role formulas that are already used.
    #Later, this list is used to retrieve a new role formula.
    aBoxCon.productionstring(name="Component 4, Rule 1: existential found, get role list", string="""
        =g>
        isa       goal
        state     inference_step
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        form      =I1
        element   =I2
        mainconnective existential
        subformula1  =I3
        subformula2  =I4
        subformula3  =I5
        derived   yes
        relation  =I6
        concept   =I7
        =imaginal_action>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =IA1
        form3     =IA2
        form4     =IA3
        form5     =IA4
        form6     =IA5
        form7     =IA6
        form8     =IA7
        form9     =IA8
        form10    =IA9
        form11    =IA10
        form12    =IA11
        form13    =IA12
        form14    =IA13
        form15    =IA14
        form16    =IA15
        form17    =IA16
        form18    =IA17
        form19    =IA18
        form20    =IA19
        form21    =IA20
        form22    =IA21
        form23    =IA22
        form24    =IA23
        form25    =IA24
        form26    =IA25
        form27    =IA26
        form28    =IA27
        form29    =IA28
        form30    =IA29
        form31    =IA30
        form32    =IA31
        form33    =IA32
        form34    =IA33
        form35    =IA34
        form36    =IA35
        form37    =IA36
        form38    =IA37
        form39    =IA38
        form40    =IA39
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     get_role_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        form      =I1
        element   =I2
        mainconnective existential
        subformula1  =I3
        subformula2  =I4
        subformula3  =I5
        derived   yes
        relation  =I6
        concept   =I7
        +imaginal_action>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =IA1
        form3     =IA2
        form4     =IA3
        form5     =IA4
        form6     =IA5
        form7     =IA6
        form8     =IA7
        form9     =IA8
        form10    =IA9
        form11    =IA10
        form12    =IA11
        form13    =IA12
        form14    =IA13
        form15    =IA14
        form16    =IA15
        form17    =IA16
        form18    =IA17
        form19    =IA18
        form20    =IA19
        form21    =IA20
        form22    =IA21
        form23    =IA22
        form24    =IA23
        form25    =IA24
        form26    =IA25
        form27    =IA26
        form28    =IA27
        form29    =IA28
        form30    =IA29
        form31    =IA30
        form32    =IA31
        form33    =IA32
        form34    =IA33
        form35    =IA34
        form36    =IA35
        form37    =IA36
        form38    =IA37
        form39    =IA38
        form40    =IA39
        +retrieval>
        isa       role_list
        thing     role_list
        role1     =G5
    """)

    #This rule retrieves a role formula that is not in the list, ensuring the related element is new.
    aBoxCon.productionstring(name="Component 4, Rule 2: role list found, select role not in list", string="""
        =g>
        isa       goal
        state     get_role_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        form      =I1
        element   =I2
        mainconnective existential
        subformula1  =I3
        subformula2  =I4
        subformula3  =I5
        derived   yes
        relation  =I6
        concept   =I7
        =imaginal_action>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =IA1
        form3     =IA2
        form4     =IA3
        form5     =IA4
        form6     =IA5
        form7     =IA6
        form8     =IA7
        form9     =IA8
        form10    =IA9
        form11    =IA10
        form12    =IA11
        form13    =IA12
        form14    =IA13
        form15    =IA14
        form16    =IA15
        form17    =IA16
        form18    =IA17
        form19    =IA18
        form20    =IA19
        form21    =IA20
        form22    =IA21
        form23    =IA22
        form24    =IA23
        form25    =IA24
        form26    =IA25
        form27    =IA26
        form28    =IA27
        form29    =IA28
        form30    =IA29
        form31    =IA30
        form32    =IA31
        form33    =IA32
        form34    =IA33
        form35    =IA34
        form36    =IA35
        form37    =IA36
        form38    =IA37
        form39    =IA38
        form40    =IA39
        =retrieval>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =R2
        role3     =R3
        role4     =R4
        role5     =R5
        role6     =R6
        role7     =R7
        role8     =R8
        role9     =R9
        role10    =R10
        role11    =R11
        role12    =R12
        role13    =R13
        role14    =R14
        role15    =R15
        role16    =R16
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_role
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        form      =I1
        element   =I2
        mainconnective existential
        subformula1  =I3
        subformula2  =I4
        subformula3  =I5
        derived   yes
        relation  =I6
        concept   =I7
        +imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =R2
        role3     =R3
        role4     =R4
        role5     =R5
        role6     =R6
        role7     =R7
        role8     =R8
        role9     =R9
        role10    =R10
        role11    =R11
        role12    =R12
        role13    =R13
        role14    =R14
        role15    =R15
        role16    =R16
        +retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        relation  =I6
        subformula1  =I2
        subformula2  ~=G5
        subformula2  ~=R2
        subformula2  ~=R3
        subformula2  ~=R4
        subformula2  ~=R5
        subformula2  ~=R6
        subformula2  ~=R7
        subformula2  ~=R8
        subformula2  ~=R9
        subformula2  ~=R10
        subformula2  ~=R11
        subformula2  ~=R12
        subformula2  ~=R13
        subformula2  ~=R14
        subformula2  ~=R15
        subformula2  ~=R16
    """)

    #This rule labels the role formula as derived and retrieves the appropriate concept assignment.
    aBoxCon.productionstring(name="Component 4, Rule 3: label role, find concept", string="""
        =g>
        isa       goal
        state     retrieve_role
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        form      =I1
        element   =I2
        mainconnective existential
        subformula1  =I3
        subformula2  =I4
        subformula3  =I5
        derived   yes
        relation  =I6
        concept   =I7
        =imaginal_action>
        isa       role_list
        thing     role_list
        role1     =IA1
        role2     =IA2
        role3     =IA3
        role4     =IA4
        role5     =IA5
        role6     =IA6
        role7     =IA7
        role8     =IA8
        role9     =IA9
        role10    =IA10
        role11    =IA11
        role12    =IA12
        role13    =IA13
        role14    =IA14
        role15    =IA15
        role16    =IA16
        =retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        subformula1  =I2
        subformula2  =R1
        subformula3  =R2
        form      =R3
        concept   none
        relation  =R4
        element   =R5
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_concept
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =R1
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        mainconnective  relation
        subformula1  =I2
        subformula2  =R1
        subformula3  =R2
        form      =R3
        concept   none
        relation  =R4
        derived   yes
        element   =R5
        +imaginal_action>
        isa       role_list
        thing     role_list
        role1     =R1
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        +retrieval>
        isa       proposition
        element   =R1
        concept   =I5
        mainconnective ~relation
    """)

    #In case an atomic concept assignment is found, this formula is labelled and the concept assignment chunk is moved to the imaginal buffer as a preparation for component 1 (which looks for a clash among atomic concept assignments).
    aBoxCon.productionstring(name="Component 4, Rule 4a: label concept, atom found", string="""
        =g>
        isa       goal
        state     retrieve_concept
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        mainconnective  relation
        subformula1  =I1
        subformula2  =G5
        subformula3  =I2
        form      =I3
        concept   none
        relation  =I4
        derived   yes
        element   =I5
        =imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        ?retrieval>
        state     free
        =retrieval>
        isa       proposition
        thing     proposition
        element   =G5
        concept   =R1
        form      =R2
        mainconnective  =R3
        mainconnective  ~conjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~disjunction
        mainconnective  ~none
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   =R8
        ==>
        =g>
        isa       goal
        state     label_concept
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        element   =G5
        concept   =R1
        form      =R2
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   yes
        +imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
    """)

    #After an atomic formula is found, component 1 is invoked to look for a clash.
    aBoxCon.productionstring(name="Component 4, Rule 5: atom found, prepare to look for clash", string="""
        =g>
        isa       goal
        state     label_concept
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        element   =G5
        concept   =I1
        form      =I2
        mainconnective  =I3
        mainconnective  ~conjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~disjunction
        mainconnective  ~none
        relation  =I4
        subformula1  =I5
        subformula2  =I6
        subformula3  =I7
        derived   yes
        =imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     find_clash_to_head
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       checklist
        thing     checklist
        form      =I2
        element   =G5
        concept   =I1
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        form2     none
        form3     none
        form4     none
        form5     none
        form6     none
        form7     none
        form8     none
        form9     none
        form10    none
        form11    none
        form12    none
        form13    none
        form14    none
        form15    none
        form16    none
        form17    none
        form18    none
        +imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        +retrieval>
        isa       storelist
        thing     storelist
        form      =G1
    """)

    #In case complex non-universal formula is found, this chunk is labelled as derived and component 2 is invoked, i.e. the next (derived) formula is selected to apply a syntax expansion rule to.
    #This rule has a similarly working counterpart for universal formulas, because of the formal difference between universal and non-universal formulas.
    aBoxCon.productionstring(name="Component 4, Rule 4b: label concept, non-universal complex formula found", string="""
        =g>
        isa       goal
        state     retrieve_concept
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        mainconnective  relation
        subformula1  =I1
        subformula2  =G5
        subformula3  =I2
        form      =I3
        concept   none
        relation  =I4
        derived   yes
        element   =I5
        =imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        =retrieval>
        isa       proposition
        thing     proposition
        element   =G5
        concept   =R1
        form      =R2
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~universal
        mainconnective  ~none
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   =R8
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     derive_next_formulas
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        element   =G5
        concept   =R1
        form      =R2
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   yes
        +imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        +retrieval>
        isa       storelist
        thing     storelist
        form      =G1
    """)

    #In case a universal formula is found, its chunk is labelled as derived and component 2 is invoked, i.e. the next formula is selected to apply a syntax expansion rule to.
    #This rule has a similarly working counterpart for non-universal formulas, because of the formal difference between universal and non-universal formulas.
    aBoxCon.productionstring(name="Component 4, Rule 4c: label concept, universal formula found", string="""
        =g>
        isa       goal
        state     retrieve_concept
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     proposition
        mainconnective  relation
        subformula1  =I1
        subformula2  =G5
        subformula3  =I2
        form      =I3
        concept   none
        relation  =I4
        derived   yes
        element   =I5
        =imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        =retrieval>
        isa       uproposition
        thing     uproposition
        element   =G5
        concept   =R1
        form      =R2
        mainconnective  universal
        relation  =R3
        subformula1  =R4
        subformula2  =R5
        derived   =R6
        count     =R7
        relation1 =R8
        relation2 =R9
        relation3 =R10
        relation4 =R11
        relation5 =R12
        relation6 =R13
        relation7 =R14
        relation8 =R15
        relation9 =R16
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     derive_next_formulas
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       uproposition
        thing     uproposition
        element   =G5
        concept   =R1
        form      =R2
        mainconnective  universal
        relation  =R3
        subformula1  =R4
        subformula2  =R5
        derived   yes
        count     =G2
        relation1 =R8
        relation2 =R9
        relation3 =R10
        relation4 =R11
        relation5 =R12
        relation6 =R13
        relation7 =R14
        relation8 =R15
        relation9 =R16
        +imaginal_action>
        isa       role_list
        thing     role_list
        role1     =G5
        role2     =IA1
        role3     =IA2
        role4     =IA3
        role5     =IA4
        role6     =IA5
        role7     =IA6
        role8     =IA7
        role9     =IA8
        role10    =IA9
        role11    =IA10
        role12    =IA11
        role13    =IA12
        role14    =IA13
        role15    =IA14
        role16    =IA15
        +retrieval>
        isa       storelist
        thing     storelist
        form      =G1
    """)
