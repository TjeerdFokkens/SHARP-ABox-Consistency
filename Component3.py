#Overview
#This Component makes derivations from a conjunction concept assignment.
#It derives concept assignments for both the conjuncts.

#Some rules in the following come in pairs, as they are designed to be symmetric regarding both conjuncts, i.e. either conjunct can be derived first and can be selected first for further inferences.
#Moreover, some rules come in pairs on top of that, as there is a formal distinction between universal and non-universal formula chunks, i.e. rules that do the same thing in principle are different because of the different forms of those formula chunks.


def component3(aBoxCon):
    #This rule takes the conjunct labels of the conjunction chunk and stores the first of them in the imaginal and the second of them in the imaginal_action buffers, so that the respective chunks can be retrieved later.
    aBoxCon.productionstring(name="Component 3, Rule 1: conjunction found, put conjunct labels in imaginal and imaginal_action buffers", string="""
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
        form      =G1
        element   =I1
        mainconnective conjunction
        subformula1  =I2
        subformula2  =I3
        subformula3  =I4
        derived   yes
        relation  =I5
        concept   =I6
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
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6 
        +imaginal>
        isa       proposition
        thing     proposition
        form      =I2
        element   =I1
        mainconnective none
        relation  none
        subformula1 none
        subformula2 none
        subformula3 none
        derived   none
        concept   none
        +imaginal_action>
        isa       proposition
        thing     proposition
        form      =I3
        element   =I1
        mainconnective none
        relation  none
        subformula1 none
        subformula2 none
        subformula3 none
        derived   none
        concept   none
        ~retrieval>
    """)

    #This rule tries to retrieve the first conjunct, i.e. the one which label was stored in the imaginal buffer.
    aBoxCon.productionstring(name="Component 3, Rule 2a: retrieve first conjunct", string="""
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     ~clash_list
        thing     ~storelist
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        thing     =I1
        form      =I2
        element   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        subformula3 =I8
        derived   ~yes
        concept   =I9
        =imaginal_action>
        isa       proposition
        thing     ~clash_list
        thing     ~storelist
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        thing     =IA1
        form      =IA2
        element   =I3
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        concept   =IA9
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~storelist
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        form      =I2
        element   =I3
        mainconnective ~none
        +imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =I3
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        concept   =IA9
        ~imaginal>
    """)

    #This rule tries to retrieve the second conjunct, i.e. the one which label is stored in the imaginal_action buffer.
    aBoxCon.productionstring(name="Component 3, Rule 2b: retrieve second conjunct", string="""
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     ~clash_list
        thing     ~storelist
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        thing     =I1
        form      =I2
        element   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        subformula3 =I8
        derived   =I9
        concept   =I10
        =imaginal_action>
        isa       proposition
        thing     ~clash_list
        thing     ~storelist
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        thing     =IA1
        form      =IA2
        element   =I3
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   ~yes
        concept   =IA8
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~storelist
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        form      =IA2
        element   =I3
        mainconnective ~none
        +imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =I3
        mainconnective =I4
        relation  =I5
        subformula1 =I6
        subformula2 =I7
        subformula3 =I8
        derived   =I9
        concept   =I10
        ~imaginal_action>
    """)

    #In case the first conjunct is a formula that is non-universal, this rule labels that formula as derived.
    #Due to the formal difference between universal and non-universal formula chunks, this rule has a counterpart which does the same thing for a universal formula.
    aBoxCon.productionstring(name="Component 3, Rule 3a(n): label first conjunct, non-universal found", string="""
        =g>
        isa       goal
        state     label_conjuncts
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
        mainconnective =R3
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        subformula3 =R7
        derived   =R8
        concept   =R9
        =imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =R2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        concept   =IA9
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
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
        mainconnective =R3
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        subformula3 =R7
        derived   yes
        concept   =R9
        +imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =R2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        concept   =IA9
        ~retrieval>
    """)

    #In case the first conjunct is a universal formula, this rule labels the formula as derived.
    #Due to the formal difference between universal and non-universal formula chunks, this rule has a counterpart which does the same thing for a non-universal formula.
    aBoxCon.productionstring(name="Component 3, Rule 3a(u): label first conjunct, universal found", string="""
        =g>
        isa       goal
        state     label_conjuncts
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
        mainconnective universal
        relation  =R3
        subformula1 =R4
        subformula2 =R5
        derived   =R6
        concept   =R7
        =imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =R2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        concept   =IA9
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal>
        isa       uproposition
        thing     uproposition
        form      =R1
        element   =R2
        mainconnective universal
        relation  =R3
        subformula1 =R4
        subformula2 =R5
        derived   yes
        concept   =R7
        count     =G2
        relation1 none
        relation2 none
        relation3 none
        relation4 none
        relation5 none
        relation6 none
        relation7 none
        relation8 none
        relation9 none
        +imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =R2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        concept   =IA9
        ~retrieval>
    """)

    #In case the second conjunct is a non-universal formula, this rule labels that formula as derived.
    #Due to the formal difference between universal and non-universal formula chunks, this rule has a counterpart which does the same thing for a universal formula.
    aBoxCon.productionstring(name="Component 3, Rule 3b(n): label second conjunct, non-universal found", string="""
        =g>
        isa       goal
        state     label_conjuncts
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
        mainconnective =R3
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   =R8
        concept   =R9
        =imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =R2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   =I8
        concept   =I9
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +imaginal_action>
        isa       proposition
        thing     proposition
        form      =R1
        element   =R2
        mainconnective =R3
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   yes
        concept   =R9
        +imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =R2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   =I8
        concept   =I9
        ~retrieval>
    """)

    #In case the second formula is a universal formula, this rules labels that formula as derived.
    #Due to the formal difference between universal and non-universal formula chunks, this rule has a counterpart which does the same thing for a non-universal formula.
    aBoxCon.productionstring(name="Component 3, Rule 3b(u): label second conjunct, universal found", string="""
        =g>
        isa       goal
        state     label_conjuncts
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
        mainconnective universal
        relation  =R3
        subformula1 =R4
        subformula2 =R5
        derived   =R6
        concept   =R7
        =imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =R2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   =I8
        concept   =I9
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjuncts
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
        mainconnective universal
        relation  =R3
        subformula1 =R4
        subformula2 =R5
        derived   yes
        concept   =R7
        count     =G2
        relation1 none
        relation2 none
        relation3 none
        relation4 none
        relation5 none
        relation6 none
        relation7 none
        relation8 none
        relation9 none
        +imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =R2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   =I8
        concept   =I9
        ~retrieval>
    """)

    #If the first conjunct is atomic, this rule can fire to look for an atomic formula that clashes with it.
    aBoxCon.productionstring(name="Component 3, Rule 4a: finalise inference and move on to find a clash on first conjunct", string="""
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     free
        =imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =I3
        mainconnective  ~conjunction
        mainconnective  ~disjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~none
        mainconnective  =I4
        subformula1  =I5
        subformula2  =I6
        subformula3  =I7
        relation  =I8
        derived   yes
        concept   =I9
        =imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =I3
        mainconnective =IA3
        subformula1  =IA4
        subformula2  =IA5
        subformula3  =IA6
        relation  =IA7
        derived   yes
        concept   =IA8
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
        isa       clash_list
        thing     clash_list
        form      =I2
        element   =I3
        mainconnective =I4
        relation  =I8
        subformula1 =I5
        subformula2 =I6
        concept   =I9
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
        ~retrieval>
        ~imaginal_action>
    """)

    #If the second conjunct is atomic, this rule can fire to look for an atomic formula that clashes with it.
    aBoxCon.productionstring(name="Component 3, Rule 4b: finalise inference and move on to find a clash on second conjunct", string="""
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     free
        =imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =I3
        mainconnective =I4
        subformula1  =I5
        subformula2  =I6
        subformula3  =I7
        relation  =I8
        derived   yes
        concept   =I9
        =imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =I3
        mainconnective  ~conjunction
        mainconnective  ~disjunction
        mainconnective  ~existential
        mainconnective  ~universal
        mainconnective  ~none
        mainconnective  =IA3
        subformula1  =IA4
        subformula2  =IA5
        subformula3  =IA6
        relation  =IA7
        derived   yes
        concept   =IA8
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
        isa       clash_list
        thing     clash_list
        form      =IA2
        element   =I3
        mainconnective =IA3
        relation  =IA7
        subformula1 =IA4
        subformula2 =IA5
        concept   =IA8
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
        ~retrieval>
        ~imaginal_action>
    """)

    #If no conjunct is atomic, this rule invokes module 2 to look for a new formula to apply the syntax expansion rules to.
    aBoxCon.productionstring(name="Component 3, Rule 4c: no concept or negation derived, so move on to derive new formula", string="""
        =g>
        isa       goal
        state     retrieve_conjuncts
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        ?retrieval>
        state     free
        =imaginal>
        isa       proposition
        thing     =I1
        form      =I2
        element   =I3
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective =I4
        subformula1  =I5
        subformula2  =I6
        subformula3  =I7
        relation  =I8
        derived   yes
        concept   =I9
        =imaginal_action>
        isa       proposition
        thing     =IA1
        form      =IA2
        element   =I3
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        mainconnective  =IA3
        subformula1  =IA4
        subformula2  =IA5
        subformula3  =IA6
        relation  =IA7
        derived   yes
        concept   =IA8
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
        +retrieval>
        isa       storelist
        thing     storelist
        form      =G1
        ~imaginal_action>
        ~imaginal>
    """)
