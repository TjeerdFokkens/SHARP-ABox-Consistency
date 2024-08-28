#Overview
#This Component searches among the atomic concept assignments for a clash.
#A clash is a set of two concept assignments that assign - to the same element - two concepts that are contradictory.
#In case this component does not find a clash, two things can happen:
#    the ABox is deemed consistent (the goal state becomes 'stop'),
#    or some syntax expansion rule needs to be applied to one of the formulas (the goal state becomes 'derive_next_formulas').



def module1(aBoxCon):
    #This rule tries to retrieve a derived atomic concept assignment that clashes with the first formula of the checklist in the imaginal module. 
    aBoxCon.productionstring(name="Component 1, Rule 1: find clash to concept or negation in head of list", string="""
        =g>
        isa       goal
        state     find_clash_to_head
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       checklist
        thing     checklist
        form      =I1
        element   =I2
        concept   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        ?retrieval>
        state   free
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
        isa       checklist
        thing     checklist
        form      =I1
        element   =I2
        concept   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        +retrieval>
        isa       proposition
        thing     proposition
        element   =I2
        derived   yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        mainconnective ~relation
        mainconnective ~=I4
        mainconnective ~none
        form      ~=I1
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
        subformula1 =I6
    """)

    #In case no formula was found that clashes with the first formula in the checklist in the imaginal module, this rule tries to retrieve an atomic formula that is not yet in the list.
    aBoxCon.productionstring(name="Component 1, Rule 2a: find concept or negation not in the list", string="""
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
        isa       checklist
        thing     checklist
        form      =I1
        element   =I2
        concept   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        ?retrieval>
        state     error
        ==>
        =g>
        isa       goal
        state     add_formula_to_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       checklist
        thing     checklist
        form      =I1
        element   =I2
        concept   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        +retrieval>
        isa       proposition
        thing     proposition
        derived   yes
        mainconnective ~disjunction
        mainconnective ~conjunction
        mainconnective ~existential
        mainconnective ~universal
        mainconnective ~relation
        mainconnective ~none
        form      ~=I1
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
    """)
    
    #In case a clash is found, the goal state becomes 'stop' and the key 'I' is pressed, showing that the given ABox is inconsistent.
    aBoxCon.productionstring(name="Component 1, Rule 2b: signal a clash", string="""
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
        isa       checklist
        thing     checklist
        form      =I1
        element   =I2
        concept   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        =retrieval>
        isa       proposition
        thing     proposition
        element   =I2
        mainconnective ~conjunction
        mainconnective ~disjunction
        mainconnective ~universal
        mainconnective ~existential
        mainconnective ~relation
        mainconnective ~=I4
        mainconnective ~none
        subformula1 =I6
        derived   yes
        ?manual>
        state     free
        ==>
        =g>
        isa       goal
        state     stop
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +manual>
        isa       _manual
        cmd       press_key
        key       I
    """)
    
    #In case no new atomic formula was found, this rule modifies the goal state to 'derive_next_formulas' so that component 2 is invoked.
    aBoxCon.productionstring(name="Component 1, Rule 3a: no formula found, need to derive new ones", string="""
        =g>
        isa       goal
        state     add_formula_to_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew yes
        =imaginal>
        isa       checklist
        thing     checklist
        form      =I1
        concept   =I3
        element   =I2
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        ?retrieval>
        state     error
        ==>
        =g>
        isa       goal
        state     derive_next_formulas
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew yes
        +retrieval>
        isa       storelist
        thing     storelist
        form      =G1
        ~imaginal>
    """)

    #In case the 'derivenew' slot in the goal state is set to 'no' and no atomic formula can be found, the ABox is consistent: the goal state becomes 'stop' and the key 'C' is pressed, showing consistency of the ABox.
    aBoxCon.productionstring(name="Component 1, Rule 3b: no formula found, signal consistency", string="""
        =g>
        isa       goal
        state     add_formula_to_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew no
        =imaginal>
        isa       checklist
        thing     checklist
        form      =I1
        concept   =I3
        element   =I2
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        ?retrieval>
        state     error
        ?manual>
        state     free
        ==>
        =g>
        isa       goal
        state     stop
        +manual>
        isa       _manual
        cmd       press_key
        key       C
    """)

    #This rule puts the newly found formula in the first slots of the list and moves the other formulas one place down the list.
    #The goal state moves to 'find_clash_to_head', so that a new atomic concept assignment is searched for that clashes with the formula just put on top of the list. 
    aBoxCon.productionstring(name="Component 1, Rule 3c: add formula to list and find a clash", string="""
        =g>
        isa       goal
        state     add_formula_to_list
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       checklist
        thing     checklist
        form      =I1
        element   =I2
        concept   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        form2     =I8
        form3     =I9
        form4     =I10
        form5     =I11
        form6     =I12
        form7     =I13
        form8     =I14
        form9     =I15
        form10    =I16
        form11    =I17
        form12    =I18
        form13    =I19
        form14    =I20
        form15    =I21
        form16    =I22
        form17    =I23
        form18    =I24
        =retrieval>
        isa       proposition
        thing     proposition
        derived   yes
        form      =R1
        element   =R2
        mainconnective =R3
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        concept   =R7
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
        form      =R1
        element   =R2
        mainconnective =R3
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        concept   =R7
        form2     =I1
        form3     =I8
        form4     =I9
        form5     =I10
        form6     =I11
        form7     =I12
        form8     =I13
        form9     =I14
        form10    =I15
        form11    =I16
        form12    =I17
        form13    =I18
        form14    =I19
        form15    =I20
        form16    =I21
        form17    =I22
        form18    =I23
        ~retrieval>
    """)
