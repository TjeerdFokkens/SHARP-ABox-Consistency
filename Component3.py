#Overview
#This Component makes derivations from a conjunction concept assignment.
#It derives concept assignments for both the conjuncts.

#Some rules in the following come in pairs, as they are designed to be symmetric regarding both conjuncts, i.e. either conjunct can be derived first and can be selected first for further inferences.
#Moreover, some rules come in pairs on top of that, as there is a formal distinction between universal and non-universal formula chunks, i.e. rules that do the same thing in principle are different because of the different forms of those formula chunks.


def component3(aBoxCon):
    #This rule takes the conjunct values of the conjunction chunk and stores the first of them in the imaginal and the second of them in the imaginal_action buffers, so that the respective chunks can be retrieved later.
    aBoxCon.productionstring(name="Component 3, Rule 1: conjunction found, put empty conjunct chunks in imaginal and imaginal_action buffers", string="""
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
        isa       used_list
        thing     used_list
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
        state     retrieve_conjunct1
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
        state     retrieve_conjunct1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        derived   ~yes
        concept   =I10
        =imaginal_action>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        derived   ~yes
        concept   =IA9
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjunct1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        state     retrieve_conjunct1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        derived   ~yes
        concept   =I10
        =imaginal_action>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        derived   ~yes
        concept   =IA9
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjunct1
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        state     label_conjunct1
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
        mainconnective ~universal
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
        derived   ~yes
        concept   =IA9
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjunct2
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
        state     label_conjunct1
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   =R7
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
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
        derived   ~yes
        concept   =IA9
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjunct2
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   yes
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
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
        state     label_conjunct1
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
        derived   ~yes
        concept   =I9
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjunct2
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
        state     label_conjunct1
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   =R7
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
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
        derived   ~yes
        concept   =I9
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     retrieve_conjunct2
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   yes
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
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

    #After the first conjunct is found to be a non-universal formula, the second conjunct is retrieved.
    aBoxCon.productionstring(name="Component 3, Rule 4a(n): retrieve second conjunct after non-universal", string="""
        =g>
        isa       goal
        state     retrieve_conjunct2
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
        mainconnective =I3
        mainconnective ~universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   yes
        concept   =I9
        =imaginal_action>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        thing     =IA1
        form      =IA2
        element   =I2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        derived   ~yes
        concept   =IA9
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        form      =IA2
        element   =I2
        mainconnective ~none
        +imaginal>
        isa       proposition
        thing     proposition
        form      =I1
        element   =I2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   yes
        concept   =I9
        ~imaginal_action>
    """)

    #After the first conjunct is found to be a universal formula, the second conjunct is retrieved.
    aBoxCon.productionstring(name="Component 3, Rule 4a(u): retrieve second conjunct after universal", string="""
        =g>
        isa       goal
        state     retrieve_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       uproposition
        thing     uproposition
        form      =I1
        element   =I2
        concept   =I3
        mainconnective universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        derived   yes
        count     =I7
        relation1 =I8
        relation2 =I9
        relation3 =I10
        relation4 =I11
        relation5 =I12
        relation6 =I13
        relation7 =I14
        relation8 =I15
        relation9 =I16
        =imaginal_action>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        thing     =IA1
        form      =IA2
        element   =I2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   =IA8
        derived   ~yes
        concept   =IA9
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        form      =IA2
        element   =I2
        mainconnective ~none
        +imaginal>
        isa       uproposition
        thing     uproposition
        form      =I1
        element   =I2
        concept   =I3
        mainconnective universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        derived   yes
        count     =I7
        relation1 =I8
        relation2 =I9
        relation3 =I10
        relation4 =I11
        relation5 =I12
        relation6 =I13
        relation7 =I14
        relation8 =I15
        relation9 =I16
        ~imaginal_action>
    """)

    #After the second conjunct is found to be a non-universal formula, the first conjunct is retrieved.
    aBoxCon.productionstring(name="Component 3, Rule 4b(n): retrieve first conjunct after non-universal", string="""
        =g>
        isa       goal
        state     retrieve_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        derived   =I8
        concept   =I9
        =imaginal_action>
        isa       proposition
        thing     proposition
        form      =IA1
        element   =IA2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   yes
        concept   =IA8
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        form      =I2
        element   =I3
        mainconnective ~none
        +imaginal_action>
        isa       proposition
        thing     proposition
        form      =IA1
        element   =IA2
        mainconnective =IA3
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   yes
        concept   =IA8
        ~imaginal>
    """)

    #After the second conjunct is found to be a universal formula, the first conjunct is retrieved.
    aBoxCon.productionstring(name="Component 3, Rule 4b(u): retrieve first conjunct after universal", string="""
        =g>
        isa       goal
        state     retrieve_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        =imaginal>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
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
        derived   =I8
        concept   =I9
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        concept   =IA3
        mainconnective universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        derived   yes
        count     =IA7
        relation1 =IA8
        relation2 =IA9
        relation3 =IA10
        relation4 =IA11
        relation5 =IA12
        relation6 =IA13
        relation7 =IA14
        relation8 =IA15
        relation9 =IA16
        ?retrieval>
        state     free
        ==>
        =g>
        isa       goal
        state     label_conjunct2
        form      =G1
        count1    =G2
        count2    =G3
        mainconnective =G4
        role      =G5
        derivenew =G6
        +retrieval>
        isa       proposition
        thing     ~clash_list
        thing     ~used_list
        thing     ~universal_list
        thing     ~goal
        thing     ~count_order
        thing     ~role_list
        form      =I2
        element   =I3
        mainconnective ~none
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        concept   =IA3
        mainconnective universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        derived   yes
        count     =IA7
        relation1 =IA8
        relation2 =IA9
        relation3 =IA10
        relation4 =IA11
        relation5 =IA12
        relation6 =IA13
        relation7 =IA14
        relation8 =IA15
        relation9 =IA16
        ~imaginal>
    """)

    #After the first conjunct is found to be a non-universal formula, the second conjunct, also found to be a non-universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5a(nn): label second conjunct after non-universal, non-universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        mainconnective ~universal
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   =R8
        concept   =R9
        =imaginal>
        isa       proposition
        thing     proposition
        form      =I2
        element   =R2
        mainconnective =I3
        mainconnective ~universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   yes
        concept   =I8
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        thing     proposition
        form      =I2
        element   =R2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   yes
        concept   =I8
        ~retrieval>
    """)

    #After the first conjunct is found to be a non-universal formula, the second conjunct, found to be a universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5a(nu): label second conjunct after non-universal, universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   =R7
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        =imaginal>
        isa       proposition
        thing     proposition
        form      =I2
        element   =R2
        mainconnective =I3
        mainconnective ~universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   yes
        concept   =I8
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   yes
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        +imaginal>
        isa       proposition
        thing     proposition
        form      =I2
        element   =R2
        mainconnective =I3
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        subformula3 =I7
        derived   yes
        concept   =I8
        ~retrieval>
    """)

    #After the first conjunct is found to be a universal formula, the second conjunct, found to be a non-universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5a(un): label second conjunct after universal, non-universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        mainconnective ~universal
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   =R8
        concept   =R9
        =imaginal>
        isa       uproposition
        thing     uproposition
        form      =I1
        element   =I2
        concept   =I3
        mainconnective universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        derived   =I7
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
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        isa       uproposition
        thing     uproposition
        form      =I1
        element   =I2
        concept   =I3
        mainconnective universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        derived   yes
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
        ~retrieval>
    """)

    #After the first conjunct is found to be a universal formula, the second conjunct, also found to be a universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5a(uu): label second conjunct after universal, universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   =R7
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        =imaginal>
        isa       uproposition
        thing     uproposition
        form      =I1
        element   =I2
        concept   =I3
        mainconnective universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        derived   yes
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
        ?imaginal_action>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   yes
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        +imaginal>
        isa       uproposition
        thing     uproposition
        form      =I1
        element   =I2
        concept   =I3
        mainconnective universal
        relation  =I4
        subformula1 =I5
        subformula2 =I6
        derived   yes
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
        ~retrieval>
    """)

    #After the second conjunct is found to be a non-universal formula, the first conjunct, also found to be a non-universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5b(nn): label first conjunct after non-universal, non-universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        mainconnective ~universal
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   =R8
        concept   =R9
        =imaginal_action>
        isa       proposition
        thing     proposition
        form      =IA1
        element   =R2
        mainconnective =IA2
        mainconnective ~universal
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        subformula3 =IA6
        derived   yes
        concept   =IA7
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   yes
        concept   =R9
        +imaginal_action>
        isa       proposition
        thing     proposition
        form      =IA1
        element   =R2
        mainconnective =IA2
        relation  =IA3
        subformula1 =IA4
        subformula2 =IA5
        subformula3 =IA6
        derived   yes
        concept   =IA7
        ~retrieval>
    """)

    #After the second conjunct is found to be a non-universal formula, the first conjunct, found to be a universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5b(nu): label first conjunct after non-universal, universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   =R7
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        =imaginal_action>
        isa       proposition
        thing     =IA1
        thing     ~uproposition
        form      =IA2
        element   =R2
        mainconnective =IA3
        mainconnective ~universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        subformula3 =IA7
        derived   yes
        concept   =IA8
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   yes
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
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
        derived   yes
        concept   =IA8
        ~retrieval>
    """)

    #After the second conjunct is found to be a universal formula, the first conjunct, found to be a non-universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5b(un): label first conjunct after universal, non-universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        mainconnective ~universal
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   =R8
        concept   =R9
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        concept   =IA3
        mainconnective universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        derived   =IA7
        count     =IA8
        relation1 =IA9
        relation2 =IA10
        relation3 =IA11
        relation4 =IA12
        relation5 =IA13
        relation6 =IA14
        relation7 =IA15
        relation8 =IA16
        relation9 =IA17
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        subformula1  =R4
        subformula2  =R5
        subformula3  =R6
        relation  =R7
        derived   yes
        concept   =R9
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        concept   =IA3
        mainconnective universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        derived   yes
        count     =IA8
        relation1 =IA9
        relation2 =IA10
        relation3 =IA11
        relation4 =IA12
        relation5 =IA13
        relation6 =IA14
        relation7 =IA15
        relation8 =IA16
        relation9 =IA17
        ~retrieval>
    """)

    #After the second conjunct is found to be a universal formula, the first conjunct, also found to be a universal, is labelled as derived.
    aBoxCon.productionstring(name="Component 3, Rule 5b(uu): label first conjunct after universal, universal found", string="""
        =g>
        isa       goal
        state     label_conjunct2
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   =R7
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        =imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        concept   =IA3
        mainconnective universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        derived   yes
        count     =IA8
        relation1 =IA9
        relation2 =IA10
        relation3 =IA11
        relation4 =IA12
        relation5 =IA13
        relation6 =IA14
        relation7 =IA15
        relation8 =IA16
        relation9 =IA17
        ?imaginal>
        state     free
        ==>
        =g>
        isa       goal
        state     conjunction_finish
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
        concept   =R3
        mainconnective universal
        relation  =R4
        subformula1 =R5
        subformula2 =R6
        derived   yes
        count     =R8
        relation1 =R9
        relation2 =R10
        relation3 =R11
        relation4 =R12
        relation5 =R13
        relation6 =R14
        relation7 =R15
        relation8 =R16
        relation9 =R17
        +imaginal_action>
        isa       uproposition
        thing     uproposition
        form      =IA1
        element   =IA2
        concept   =IA3
        mainconnective universal
        relation  =IA4
        subformula1 =IA5
        subformula2 =IA6
        derived   yes
        count     =IA8
        relation1 =IA9
        relation2 =IA10
        relation3 =IA11
        relation4 =IA12
        relation5 =IA13
        relation6 =IA14
        relation7 =IA15
        relation8 =IA16
        relation9 =IA17
        ~retrieval>
    """)

    #If the first conjunct is atomic, this rule can fire to look for an atomic formula that clashes with it.
    aBoxCon.productionstring(name="Component 3, Rule 6a: finalise inference and move on to find a clash on first conjunct", string="""
        =g>
        isa       goal
        state     conjunction_finish
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
        derived   yes
        element   =I3
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
    aBoxCon.productionstring(name="Component 3, Rule 6b: finalise inference and move on to find a clash on second conjunct", string="""
        =g>
        isa       goal
        state     conjunction_finish
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
        derived   yes
        element   =I3
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
    aBoxCon.productionstring(name="Component 3, Rule 7: no concept or negation derived, so move on to derive new formula", string="""
        =g>
        isa       goal
        state     conjunction_finish
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
        element   =I3
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        derived   yes
        =imaginal_action>
        isa       proposition
        element   =I3
        mainconnective  ~concept
        mainconnective  ~negation
        mainconnective  ~none
        derived   yes
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
        isa       used_list
        thing     used_list
        form      =G1
        ~imaginal_action>
        ~imaginal>
    """)
