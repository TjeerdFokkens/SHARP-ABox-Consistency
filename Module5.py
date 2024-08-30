#Overview
#This Component makes derivations from universal restriction concept assignments and the corresponding role assignments; it derives the appropriate concept assignments.
#It runs through all universal formulas that qualify for application of a syntax expansion rule.

#This component exhaustively inspects the universal formulas that are derived at the point of invoking this component.
#For every universal restriction formula, it looks for all corresponding role assignments, where corresponding means that the first element of the role assignment is identical to the element of the universal formula, and that the role names are the same for both.
#For every universal restriction formula, the corresponding role assignments together with which have been used to make an inference on, are stored in the universal restriction formula chunk.
#The count1 and count2 slots in the goal chunk keep track of how many times component 5 is visited.
#When for all universal formulas, all corresponding role assignments have been visited, the count is updated by retrieving a count-chunk from the declarative memory and updating the count1 and count2 slots in the goal chunk accordingly.

#Some rules come in two variants, because of the formal difference between universal and non-universal formulas.

def component5(aBoxCon):
    #In case no role formula can be found that corresponds to the universal formula in the imaginal_action buffer, this rule prepares to retrieve the next universal formula.
    aBoxCon.productionstring(name="Component 5, Rule 1a: no relation found, prepare to retrieve next universal", string="""
        =g>
        isa       goal
        state     component5
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        ==>
        =g>
        isa       goal
        state     prepare_find_next_universal
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ~retrieval>
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
    """)

    #This rules tries to retrieve a universal formula that is not in the universal_list.
    #This universal_list chunk contains the universal formulas that have been inspected in the current round of component 5.
    aBoxCon.productionstring(name="Component 5, Rule 1a: no relation found, find next universal", string="""
        =g>
        isa       goal
        state     prepare_find_next_universal
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     free
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        ==>
        =g>
        isa       goal
        state     find_next_universal
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
        form      ~=IA1
        form      ~=I1
        form      ~=I2
        form      ~=I3
        form      ~=I4
        form      ~=I5
        form      ~=I6
        form      ~=I7
        form      ~=I8
        form      ~=I9
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      =IA1
        form2     =I1
        form3     =I2
        form4     =I3
        form5     =I4
        form6     =I5
        form7     =I6
        form8     =I7
        form9     =I8
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
    """)

    #After the next universal restriction formula is retrieved, this rule goes back to state 'component5' to look for a corresponding role assignment.
    aBoxCon.productionstring(name="Component 5, Rule 2a: universal found, back to start of component 5", string="""
        =g>
        isa       goal
        state     find_next_universal
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
        count     =G2
        relation1 =R7
        relation2 =R8
        relation3 =R9
        relation4 =R10
        relation5 =R11
        relation6 =R12
        relation7 =R13
        relation8 =R14
        relation9 =R15
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
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
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
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

    #This rule fires if no universal formula can be found.
    #This means that all universal formulas that qualify for an application of a syntax expansion rule have been visited in the current round of component 5.
    #This rule then retrieves the storelist to use it to select a new formula to apply a syntax expansion rule to.
    aBoxCon.productionstring(name="Component 5, Rule 2b: no universal found, retrieve storelist", string="""
        =g>
        isa       goal
        state     find_next_universal
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     error
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        mainconnective  universal
        relation  =IA3
        subformula1  =IA4
        subformula2  =IA5
        derived   yes
        concept   =IA6
        count     =G3
        relation1 =IA6
        relation2 =IA7
        relation3 =IA8
        relation4 =IA9
        relation5 =IA10
        relation6 =IA11
        relation7 =IA12
        relation8 =IA13
        relation9 =IA14
        ==>
        =g>
        isa       goal
        state     prepare_non_universal_retrieval
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ~imaginal_action>
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        +retrieval>
        isa       storelist
        thing     storelist
        form      =G1
    """)

    #This rule moves the storelist to the imaginal buffer and retrieves a count from the declarative memory in order to update the count in the goal buffer, which keeps track of how many times component 5 is executed.
    aBoxCon.productionstring(name="Component 5, Rule 3a: put storelist of used formulas in imaginal buffer and update count", string="""
        =g>
        isa       goal
        state     prepare_non_universal_retrieval
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
        form2     =R1
        form3     =R2
        form4     =R3
        form5     =R4
        form6     =R5
        form7     =R6
        form8     =R7
        form9     =R8
        form10    =R9
        form11    =R10
        form12    =R11
        form13    =R12
        form14    =R13
        form15    =R14
        form16    =R15
        form17    =R16
        form18    =R17
        form19    =R18
        form20    =R19
        form21    =R20
        form22    =R21
        form23    =R22
        form24    =R23
        form25    =R24
        form26    =R25
        form27    =R26
        form28    =R27
        form29    =R28
        form30    =R29
        form31    =R30
        form32    =R31
        form33    =R32
        form34    =R33
        form35    =R34
        form36    =R35
        form37    =R36
        form38    =R37
        form39    =R38
        form40    =R39
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_non_universal
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
        form2     =R1
        form3     =R2
        form4     =R3
        form5     =R4
        form6     =R5
        form7     =R6
        form8     =R7
        form9     =R8
        form10    =R9
        form11    =R10
        form12    =R11
        form13    =R12
        form14    =R13
        form15    =R14
        form16    =R15
        form17    =R16
        form18    =R17
        form19    =R18
        form20    =R19
        form21    =R20
        form22    =R21
        form23    =R22
        form24    =R23
        form25    =R24
        form26    =R25
        form27    =R26
        form28    =R27
        form29    =R28
        form30    =R29
        form31    =R30
        form32    =R31
        form33    =R32
        form34    =R33
        form35    =R34
        form36    =R35
        form37    =R36
        form38    =R37
        form39    =R38
        form40    =R39
        +retrieval>
        isa       count_order
        thing     count_order
        number    =G3
    """)

    #This rules updates the count in the goal buffer, which keeps track of how many times component 5 is executed, then it tries to retrieve a non-universal complex formula on which no syntax expansion rule has been applied yet.
    aBoxCon.productionstring(name="Component 5, Rule 3a: retrieve non-universal proposition", string="""
        =g>
        isa       goal
        state     retrieve_non_universal
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
        form2     =I1
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
        =retrieval>
        isa       count_order
        thing     count_order
        number    =G3
        successor =R1
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     update_storelist_2
        form      =G1
        count1    =G3
        count2    =R1
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       storelist
        thing     storelist
        form      =G1
        form2     =I1
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
        +retrieval>
        isa       proposition
        thing     proposition
        form      ~=G1
        form      ~=I1
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
        mainconnective ~negation
        mainconnective ~concept
        mainconnective ~disjunction
        mainconnective ~relation
        mainconnective ~none
        derived   yes
    """)

    #In case no storelist has been made, this rule creates one by putting the just inspected formula in an otherwise empty list.
    aBoxCon.productionstring(name="Component 5, Rule 3b: create storelist in imaginal buffer and put used formula in it", string="""
        =g>
        isa       goal
        state     prepare_non_universal_retrieval
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
        state     retrieve_non_universal
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
        +retrieval>
        isa       count_order
        thing     count_order
        number    =G3
    """)

    #In case a role assignment is found that corresponds with the universal restriction formula currently under inspection (so that a syntax expansion rule can be applied to both), this rule retrieves the appropriate conclusion from the declarative memory.
    #The role formula is stored in the universal restriction formula chunk, so that this specific combination of universal restriction and role assignment does not qualify anymore for an application of a syntax expansion rule, i.e. this specific inference will not be made again, thereby preventing infinite looping.
    aBoxCon.productionstring(name="Component 5, Rule 1b: infer the concept of the related element", string="""
        =g>
        isa       goal
        state     component5
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        derived   yes
        form      =R1
        subformula1 =R2
        subformula2 =R3
        subformula3 =R4
        concept   =R5
        relation  =R6
        ?retrieval>
        state     free
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =R2
        relation  =R6
        subformula1 =IA2
        subformula2 =IA3
        concept   =IA4
        relation1 =IA5
        relation2 =IA6
        relation3 =IA7
        relation4 =IA8
        relation5 =IA9
        relation6 =IA10
        relation7 =IA11
        relation8 =IA12
        relation9 =IA13
        ==>
        =g>
        isa       goal
        state     deduce_from_universal
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~none
        thing     ~checklist
        thing     ~storelist
        thing     ~universal_list
        thing     ~count_order
        thing     ~role_list
        thing     ~goal
        mainconnective ~relation
        element   =R3
        concept   =IA5
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =R2
        relation  =R6
        subformula1 =IA2
        subformula2 =IA3
        concept   =IA4
        relation1 =IA5
        relation2 =IA6
        relation3 =IA7
        relation4 =IA8
        relation5 =IA9
        relation6 =IA10
        relation7 =IA11
        relation8 =IA12
        relation9 =IA13
    """)

    #In case a non-universal concept assignment is found, this rule labels the formula as derived.
    #It also retrieves the universal_list again, so that, if no further corresponding role assignments can be found, the next universal formula can be selected to make an inference from.
    aBoxCon.productionstring(name="Component 5, Rule 4a: non-universal formula found, mark as derived", string="""
        =g>
        isa       goal
        state     deduce_from_universal
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       proposition
        thing     proposition
        mainconnective  =R1
        derived   =R2
        form      =R3
        subformula1 =R4
        subformula2 =R5
        subformula3 =R6
        element   =R7
        relation  =R8
        concept   =R9
        ?retrieval>
        state     free
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
        ==>
        =g>
        isa       goal
        state     find_relation_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =R1
        role      =G5
        derivenew =G6
        +retrieval>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        +imaginal>
        isa       proposition
        thing     proposition
        mainconnective  =R1
        derived   yes
        form      =R3
        subformula1 =R4
        subformula2 =R5
        subformula3 =R6
        element   =R7
        relation  =R8
        concept   =R9
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
    """)

    #In case a universal concept assignment is found, this rule labels the formula as derived.
    #It also retrieves the universal_list again, so that, if no further corresponding role assignments can be found, the next universal formula can be selected to make an inference from.
    aBoxCon.productionstring(name="Component 5, Rule 4b: universal formula found, mark as derived", string="""
        =g>
        isa       goal
        state     deduce_from_universal
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       uproposition
        thing     uproposition
        mainconnective  =R1
        derived   =R2
        form      =R3
        subformula1 =R4
        subformula2 =R5
        element   =R6
        relation  =R7
        concept   =R8
        count     =R9
        relation1 =R10
        relation2 =R11
        relation3 =R12
        relation4 =R13
        relation5 =R14
        relation6 =R15
        relation7 =R16
        relation8 =R17
        relation9 =R18
        ?retrieval>
        state     free
        =imaginal>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
        ==>
        =g>
        isa       goal
        state     find_relation_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =R1
        role      =G5
        derivenew =G6
        +retrieval>
        isa       universal_list
        thing     universal_list
        form      =I1
        form2     =I2
        form3     =I3
        form4     =I4
        form5     =I5
        form6     =I6
        form7     =I7
        form8     =I8
        form9     =I9
        +imaginal>
        isa       uproposition
        thing     uproposition
        mainconnective  =R1
        derived   yes
        form      =R3
        subformula1 =R4
        subformula2 =R5
        element   =R6
        relation  =R7
        concept   =R8
        count     =R9
        relation1 =R10
        relation2 =R11
        relation3 =R12
        relation4 =R13
        relation5 =R14
        relation6 =R15
        relation7 =R16
        relation8 =R17
        relation9 =R18
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
    """)

    #This rule tries to find a role assignment that corresponds with the universal formula currently under inspection, so that the combination of the two has not been used yet make an inference from.
    #This rule has a counterpart that essentially performs the same action, but which is formally different due to the formal difference between universal and non-universal formula chunks.
    aBoxCon.productionstring(name="Component 5, Rule 5a: find next relation to universal", string="""
        =g>
        isa       goal
        state     find_relation_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       universal_list
        thing     universal_list
        form      =R1
        form2     =R2
        form3     =R3
        form4     =R4
        form5     =R5
        form6     =R6
        form7     =R7
        form8     =R8
        form9     =R9
        ?retrieval>
        state     free
        =imaginal>
        isa       proposition
        thing     proposition
        mainconnective  =I1
        derived   yes
        form      =I2
        subformula1 =I3
        subformula2 =I4
        subformula3 =I5
        element   =I6
        relation  =I7
        concept   =I8
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
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
        +retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        relation  =IA3
        derived   yes
        subformula1 =IA2
        form      ~=IA7
        form      ~=IA8
        form      ~=IA9
        form      ~=IA10
        form      ~=IA11
        form      ~=IA12
        form      ~=IA13
        form      ~=IA14
        form      ~=IA15
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      =R1
        form2     =R2
        form3     =R3
        form4     =R4
        form5     =R5
        form6     =R6
        form7     =R7
        form8     =R8
        form9     =R9
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
    """)

    #This rule tries to find a role assignment that corresponds with the universal formula currently under inspection, so that the combination of the two has not been used yet make an inference from.
    #This rule has a counterpart that essentially performs the same action, but which is formally different due to the formal difference between universal and non-universal formula chunks.
    aBoxCon.productionstring(name="Component 5, Rule 5b: find next relation to universal", string="""
        =g>
        isa       goal
        state     find_relation_2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =retrieval>
        isa       universal_list
        thing     universal_list
        form      =R1
        form2     =R2
        form3     =R3
        form4     =R4
        form5     =R5
        form6     =R6
        form7     =R7
        form8     =R8
        form9     =R9
        ?retrieval>
        state     free
        =imaginal>
        isa       uproposition
        thing     uproposition
        mainconnective  =I1
        derived   yes
        form      =I2
        subformula1 =I3
        subformula2 =I4
        element   =I5
        relation  =I6
        concept   =I7
        count     =I8
        relation1 =I9
        relation2 =I10
        relation3 =I11
        relation4 =I12
        relation5 =I13
        relation6 =I14
        relation7 =I15
        relation8 =I16
        relation9 =I17
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
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
        +retrieval>
        isa       proposition
        thing     proposition
        mainconnective  relation
        relation  =IA3
        derived   yes
        subformula1 =IA2
        form      ~=IA7
        form      ~=IA8
        form      ~=IA9
        form      ~=IA10
        form      ~=IA11
        form      ~=IA12
        form      ~=IA13
        form      ~=IA14
        form      ~=IA15
        +imaginal>
        isa       universal_list
        thing     universal_list
        form      =R1
        form2     =R2
        form3     =R3
        form4     =R4
        form5     =R5
        form6     =R6
        form7     =R7
        form8     =R8
        form9     =R9
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        mainconnective  universal
        derived   yes
        count     =G3
        form      =IA1
        element   =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA6
        relation1 =IA7
        relation2 =IA8
        relation3 =IA9
        relation4 =IA10
        relation5 =IA11
        relation6 =IA12
        relation7 =IA13
        relation8 =IA14
        relation9 =IA15
    """)
