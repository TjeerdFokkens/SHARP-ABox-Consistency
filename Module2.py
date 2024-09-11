#Overview
#This Component searches among the derived complex concept assignments for one on which an inference can be made.
#Three such concept assignments exist: conjunctions, existential restrictions and universal restrictions.
#After finding a concept assignment, components 3, 4 and 5 are invoked respectively.


#The storelist chunk stores all the concept assignments that do not qualify for further inferences.
#This storelist is later used to retrieve a formula not in this list to prevent infinite looping.

#For implementation reasons, the formulas come in two types: universal and non-universal.
#The latter is designated by the string 'proposition' in the 'thing' slot, while the former is designated by the string 'uproposition' in the 'thing' slot.
#In the following, rules often come in pairs, one for each type of formula.


def component2(aBoxCon):
    #This rule puts the retrieved storelist chunk in the imaginal buffer.
    aBoxCon.productionstring(name="Component 2, Rule 1: put storelist of used formulas in imaginal buffer", string="""
        =g>
        isa       goal
        state     derive_next_formulas
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =R2
        form3     =R3
        form4     =R4
        form5     =R5
        form6     =R6
        form7     =R7
        form8     =R8
        form9     =R9
        form10    =R10
        form11    =R11
        form12    =R12
        form13    =R13
        form14    =R14
        form15    =R15
        form16    =R16
        form17    =R17
        form18    =R18
        form19    =R19
        form20    =R20
        form21    =R21
        form22    =R22
        form23    =R23
        form24    =R24
        form25    =R25
        form26    =R26
        form27    =R27
        form28    =R28
        form29    =R29
        form30    =R30
        form31    =R31
        form32    =R32
        form33    =R33
        form34    =R34
        form35    =R35
        form36    =R36
        form37    =R37
        form38    =R38
        form39    =R39
        form40    =R40
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     find_formula_not_in_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =R2
        form3     =R3
        form4     =R4
        form5     =R5
        form6     =R6
        form7     =R7
        form8     =R8
        form9     =R9
        form10    =R10
        form11    =R11
        form12    =R12
        form13    =R13
        form14    =R14
        form15    =R15
        form16    =R16
        form17    =R17
        form18    =R18
        form19    =R19
        form20    =R20
        form21    =R21
        form22    =R22
        form23    =R23
        form24    =R24
        form25    =R25
        form26    =R26
        form27    =R27
        form28    =R28
        form29    =R29
        form30    =R30
        form31    =R31
        form32    =R32
        form33    =R33
        form34    =R34
        form35    =R35
        form36    =R36
        form37    =R37
        form38    =R38
        form39    =R39
        form40    =R40
        ~retrieval>
    """)

    #In case there is no storelist chunk yet, this rule makes one in the imaginal buffer and puts one formula in it.
    aBoxCon.productionstring(name="Component 2, Rule 1: create storelist in imaginal buffer and put first used formula in it", string="""
        =g>
        isa       goal
        state     derive_next_formulas
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     find_formula_not_in_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       storelist
        thing     storelist
        form      =G1
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
        form19    none
        form20    none
        form21    none
        form22    none
        form23    none
        form24    none
        form25    none
        form26    none
        form27    none
        form28    none
        form29    none
        form30    none
        form31    none
        form32    none
        form33    none
        form34    none
        form35    none
        form36    none
        form37    none
        form38    none
        form39    none
        form40    none
        ~retrieval>
    """)

    #This rule retrieves a non-universal formula that is not in the storelist.
    aBoxCon.productionstring(name="Component 2, Rule 2a: retrieve non-universal formula", string="""
        =g>
        isa       goal
        state     find_formula_not_in_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     update_storelist_1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     proposition
        form      ~=G1
        form      ~=I2
        form      ~=I3
        form      ~=I4
        form      ~=I5
        form      ~=I6
        form      ~=I7
        form      ~=I8
        form      ~=I9
        form      ~=I10
        form      ~=I11
        form      ~=I12
        form      ~=I13
        form      ~=I14
        form      ~=I15
        form      ~=I16
        form      ~=I17
        form      ~=I18
        form      ~=I19
        form      ~=I20
        form      ~=I21
        form      ~=I22
        form      ~=I23
        form      ~=I24
        form      ~=I25
        form      ~=I26
        form      ~=I27
        form      ~=I28
        form      ~=I29
        form      ~=I30
        form      ~=I31
        form      ~=I32
        form      ~=I33
        form      ~=I34
        form      ~=I35
        form      ~=I36
        form      ~=I37
        form      ~=I38
        form      ~=I39
        form      ~=I40
        mainconnective ~negation
        mainconnective ~concept
        mainconnective ~disjunction
        mainconnective ~relation
        mainconnective ~none
        mainconnective ~universal
        derived   yes
        +imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
    """)

    #This rule retrieves a universal formula.
    #Note that the storelist is never used for universal restrictions.
    #Any derived universal restriction formula with the correct count-label can, therefore, be retrieved.
    aBoxCon.productionstring(name="Component 2, Rule 2b: retrieve universal formula", string="""
        =g>
        isa       goal
        state     find_formula_not_in_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     prepare_component_5_1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       uproposition
        thing     uproposition
        mainconnective universal
        derived   yes
        count     =G2
        +imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
    """)

    #This rule moves the storelist to the imaginal_action buffer while adding the newly found formula to it.
    aBoxCon.productionstring(name="Component 2, Rule 3a: non-universal found, update list of used formulas", string="""
        =g>
        isa       goal
        state     update_storelist_1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       proposition
        thing     proposition
        form      =R1
        element   =R2
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   yes
        concept   =R8
        =imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     inference_step
        form      =R1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        form      =R1
        element   =R2
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   yes
        concept   =R8
        +imaginal_action>
        isa       storelist
        thing     storelist
        form      =R1
        form2     =G1
        form3     =I2
        form4     =I3
        form5     =I4
        form6     =I5
        form7     =I6
        form8     =I7
        form9     =I8
        form10    =I9
        form11    =I10
        form12    =I11
        form13    =I12
        form14    =I13
        form15    =I14
        form16    =I15
        form17    =I16
        form18    =I17
        form19    =I18
        form20    =I19
        form21    =I20
        form22    =I21
        form23    =I22
        form24    =I23
        form25    =I24
        form26    =I25
        form27    =I26
        form28    =I27
        form29    =I28
        form30    =I29
        form31    =I30
        form32    =I31
        form33    =I32
        form34    =I33
        form35    =I34
        form36    =I35
        form37    =I36
        form38    =I37
        form39    =I38
        form40    =I39
    """)

    #This rule invokes  5, puts the newly found universal restriction formula in the imaginal_action buffer, creates a universal_list in the imaginal buffer and tries to retrieve a relation that corresponds to the universal restriction formula. 
    aBoxCon.productionstring(name="Component 2, Rule 3b: universal found, prepare for component 5", string="""
        =g>
        isa       goal
        state     prepare_component_5_1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       uproposition
        thing     uproposition
        form      =R1
        element   =R2
        mainconnective  universal
        relation  =R3
        subformula1  =R4
        subformula2  =R5
        derived   yes
        concept   =R6
        count     ~=G3
        relation1 =R7
        relation2 =R8
        relation3 =R9
        relation4 =R10
        relation5 =R11
        relation6 =R12
        relation7 =R13
        relation8 =R14
        relation9 =R15
        ?imaginal>
        state     free
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     component5
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =R1
        element   =R2
        mainconnective  universal
        relation  =R3
        subformula1  =R4
        subformula2  =R5
        derived   yes
        concept   =R6
        count     =G3
        relation1  =R7
        relation2  =R8
        relation3  =R9
        relation4  =R10
        relation5  =R11
        relation6  =R12
        relation7  =R13
        relation8  =R14
        relation9  =R15
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      none
        form2     none
        form3     none
        form4     none
        form5     none
        form6     none
        form7     none
        form8     none
        form9     none
        +retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        relation  =R3
        derived   yes
        subformula1 =R2
        form      ~=R7
        form      ~=R8
        form      ~=R9
        form      ~=R10
        form      ~=R11
        form      ~=R12
        form      ~=R13
        form      ~=R14
        form      ~=R15
    """)

    #If no universal restriction formula can be found, this rules tries to retrieve a non-universal formula that is not in the storelist.
    aBoxCon.productionstring(name="Component 2, Rule 4a: retrieve non-universal after universal", string="""
        =g>
        isa       goal
        state     prepare_component_5_1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
        ?imaginal_action>
        state     free
        ?retrieval>
        state     error
        ==>
        =g>
        isa       goal
        state     update_storelist_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     proposition
        form      ~=G1
        form      ~=I2
        form      ~=I3
        form      ~=I4
        form      ~=I5
        form      ~=I6
        form      ~=I7
        form      ~=I8
        form      ~=I9
        form      ~=I10
        form      ~=I11
        form      ~=I12
        form      ~=I13
        form      ~=I14
        form      ~=I15
        form      ~=I16
        form      ~=I17
        form      ~=I18
        form      ~=I19
        form      ~=I20
        form      ~=I21
        form      ~=I22
        form      ~=I23
        form      ~=I24
        form      ~=I25
        form      ~=I26
        form      ~=I27
        form      ~=I28
        form      ~=I29
        form      ~=I30
        form      ~=I31
        form      ~=I32
        form      ~=I33
        form      ~=I34
        form      ~=I35
        form      ~=I36
        form      ~=I37
        form      ~=I38
        form      ~=I39
        form      ~=I40
        mainconnective ~negation
        mainconnective ~concept
        mainconnective ~disjunction
        mainconnective ~relation
        mainconnective ~none
        derived   yes
        +imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
    """)

    #If no non-universal formula can be found, this rule tries to retrieve a universal formula.
    aBoxCon.productionstring(name="Component 2, Rule 4b: retrieve universal after non-universal", string="""
        =g>
        isa       goal
        state     update_storelist_1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        =imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     prepare_component_5_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       uproposition
        thing     uproposition
        mainconnective universal
        derived   yes
        count     ~=G3
        ~imaginal>
    """)

    #This rule prepares component 5, adds the newly found universal formula to the imaginal_action buffer, creates an empty universal_list in the imaginal buffer and tries to retrieve a relation corresponding to the universal formula.
    aBoxCon.productionstring(name="Component 2, Rule 5a: universal found after non-universal, go to component 5", string="""
        =g>
        isa       goal
        state     prepare_component_5_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       uproposition
        thing     uproposition
        form      =R1
        element   =R2
        mainconnective  universal
        relation  =R3
        subformula1  =R4
        subformula2  =R5
        derived   yes
        concept   =R6
        count     ~=G3
        relation1 =R7
        relation2 =R8
        relation3 =R9
        relation4 =R10
        relation5 =R11
        relation6 =R12
        relation7 =R13
        relation8 =R14
        relation9 =R15
        ?imaginal>
        state     free
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     component5
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =R1
        element   =R2
        mainconnective  universal
        relation  =R3
        subformula1  =R4
        subformula2  =R5
        derived   yes
        concept   =R6
        count     =G3
        relation1 =R7
        relation2 =R8
        relation3 =R9
        relation4 =R10
        relation5 =R11
        relation6 =R12
        relation7 =R13
        relation8 =R14
        relation9 =R15
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      none
        form2     none
        form3     none
        form4     none
        form5     none
        form6     none
        form7     none
        form8     none
        form9     none
        +retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        relation  =R3
        derived   yes
        subformula1 =R2
        form      ~=R7
        form      ~=R8
        form      ~=R9
        form      ~=R10
        form      ~=R11
        form      ~=R12
        form      ~=R13
        form      ~=R14
        form      ~=R15
    """)

    #After a non-universal formula is found, it is moved to the imaginal buffer and it is added to the storelist, which is moved to the imaginal_action buffer.
    aBoxCon.productionstring(name="Component 2, Rule 6a: non-universal found after universal, update list of used formulas", string="""
        =g>
        isa       goal
        state     update_storelist_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       proposition
        thing     proposition
        form      =R1
        element   =R2
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   yes
        concept   =R8
        =imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        form10    =I10
        form11    =I11
        form12    =I12
        form13    =I13
        form14    =I14
        form15    =I15
        form16    =I16
        form17    =I17
        form18    =I18
        form19    =I19
        form20    =I20
        form21    =I21
        form22    =I22
        form23    =I23
        form24    =I24
        form25    =I25
        form26    =I26
        form27    =I27
        form28    =I28
        form29    =I29
        form30    =I30
        form31    =I31
        form32    =I32
        form33    =I33
        form34    =I34
        form35    =I35
        form36    =I36
        form37    =I37
        form38    =I38
        form39    =I39
        form40    =I40
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     inference_step
        form      =R1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       proposition
        thing     proposition
        form      =R1
        element   =R2
        mainconnective  =R3
        relation  =R4
        subformula1  =R5
        subformula2  =R6
        subformula3  =R7
        derived   yes
        concept   =R8
        +imaginal_action>
        isa       storelist
        thing     storelist
        form      =R1
        form2     =G1
        form3     =I2
        form4     =I3
        form5     =I4
        form6     =I5
        form7     =I6
        form8     =I7
        form9     =I8
        form10    =I9
        form11    =I10
        form12    =I11
        form13    =I12
        form14    =I13
        form15    =I14
        form16    =I15
        form17    =I16
        form18    =I17
        form19    =I18
        form20    =I19
        form21    =I20
        form22    =I21
        form23    =I22
        form24    =I23
        form25    =I24
        form26    =I25
        form27    =I26
        form28    =I27
        form29    =I28
        form30    =I29
        form31    =I30
        form32    =I31
        form33    =I32
        form34    =I33
        form35    =I34
        form36    =I35
        form37    =I36
        form38    =I37
        form39    =I38
        form40    =I39
    """)

    #If no non-universal formula and (after that) no universal formula can be found, move to the last_clash state.
    aBoxCon.productionstring(name="Component 2, Rule 7a: no formula found, last check for clash", string="""
        =g>
        isa       goal
        state     prepare_component_5_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        ?manual>
        state     free
        ==>
        =g>
        isa       goal
        state     last_clash
        derivenew =G6
    """)

    #If no universal formula and (after that) no non-universal formula can be found, move to the last_clash state.
    aBoxCon.productionstring(name="Component 2, Rule 7b: no formula found, last check for clash", string="""
        =g>
        isa       goal
        state     update_storelist_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        ?manual>
        state     free
        ==>
        =g>
        isa       goal
        state     last_clash
        derivenew =G6
    """)

    #The last_clash state sets the 'derivenew' slot in the goal buffer to no, and moves to Component 1, which looks for a clash.
    #The 'derivenew' slot is important, because it shows that nothing else can be derived from the syntax expansion rules, so that if no clash can be found, the ABox is in fact consistent.
    aBoxCon.productionstring(name="Component 2, Rule 8: prepare for last check for a clash", string="""
        =g>
        isa       goal
        state     last_clash
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        ?manual>
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
        derivenew no
        +imaginal>
        isa       checklist
        thing     checklist
        form      none
        element   none
        concept   none
        mainconnective none
        relation  none
        subformula1 none
        subformula2 none
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
        ~retrieval>
    """)
