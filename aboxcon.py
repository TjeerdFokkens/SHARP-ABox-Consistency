
import pyactr as actr
import simpy
import re
import parser

environment = actr.Environment(focus_position=(50,130))
aBoxCon = actr.ACTRModel(
 #   environment=environment,
 #   automatic_visual_search=False,
 #   motor_prepared=True,
    subsymbolic=False,
   # utility_noise=10,
    partial_matching=False,
    utility_learning=False,
    production_compilation=False,
 #   activation_trace=True,
    #retrieval_threshold=0
)

aBoxCon.goals = {}
aBoxCon.set_goal("g")
aBoxCon.set_goal("imaginal")
aBoxCon.set_goal("imaginal_action")

actr.chunktype("goal", "state")
actr.chunktype("proposition", "thing, form, element, mainconnective, relation, subformula1, inferred1, subformula2, inferred2, derived")
actr.chunktype("checklist", "form, element, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
actr.chunktype("storelist", "form, element, mainconnective, relation, subformula1, subformula2, derived, inferred1, inferred2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")

dm = aBoxCon.decmem
goal = aBoxCon.goals["g"]
imaginal = aBoxCon.goals["imaginal"]
imaginal_action = aBoxCon.goals["imaginal_action"]
retrieval = aBoxCon.retrieval
production = aBoxCon.productions

aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="start"))
aBoxCon.goals["imaginal"].add(actr.makechunk(typename="checklist"))


aBoxCon.productionstring(name="find first formula", string="""
    =g>
    isa     goal
    state   start
    =imaginal>
    isa     checklist
    ?retrieval>
    state   free
    ==>
    =g>
    isa     goal
    state   store
    +retrieval>
    isa     proposition
    thing   proposition
    derived yes
    mainconnective ~disjunction
    mainconnective ~conjunction
    mainconnective ~relation
    mainconnective ~existential
    mainconnective ~universal
""")

aBoxCon.productionstring(name="skip then derive first formula", string="""
    =g>
    isa     goal
    state   store
    =imaginal>
    isa     checklist
    ?retrieval>
    state   error
    ==>
    =g>
    isa      goal
    state    module2
    ~retrieval>
""")

aBoxCon.productionstring(name="store first formula", string="""
    =g>
    isa     goal
    state   store
    =imaginal>
    isa     checklist
    =retrieval>
    isa     proposition
    thing   proposition
    form    =U
    element  =X
    mainconnective =Y
    subformula1 =Z
    ==>
    =g>
    isa     goal
    state   find_clash
    +imaginal>
    isa     checklist
    form    =U
    element =X
    mainconnective =Y
    subformula1 =Z
""")

aBoxCon.productionstring(name="find clash 1", string="""
    =g>
    isa     goal
    state   find_clash
    =imaginal>
    isa     checklist
    element =X
    mainconnective concept
    subformula1 =Y
    form    =Z
    form2   =A
    form3   =B
    form4   =C
    form5   =D
    form6   =E
    form7   =F
    ?retrieval>
    state   free
    ==>
    =g>
    isa     goal
    state   signal_clash
    +imaginal>
    isa     checklist
    element =X
    mainconnective concept
    subformula1 =Y
    form    =Z
    form2   =A
    form3   =B
    form4   =C
    form5   =D
    form6   =E
    form7   =F
    +retrieval>
    isa     proposition
    thing   proposition
    element  =X
    mainconnective negation
    subformula1 =Y
    derived  yes
""")

aBoxCon.productionstring(name="show clash 1", string="""
    =g>
    isa     goal
    state   signal_clash
    =imaginal>
    isa     checklist
    element =X
    mainconnective concept
    subformula1 =Y
    =retrieval>
    isa     proposition
    thing   proposition
    element  =X
    mainconnective negation
    subformula1 =Y
    ?manual>
    state   free
    ==>
    =g>
    isa     goal
    state   select
    +manual>
    isa     _manual
    cmd     press_key
    key     C
""")

aBoxCon.productionstring(name="no clash 1", string="""
    =g>
    isa     goal
    state   signal_clash
    =imaginal>
    isa     checklist
    form    =Z
    element =X
    mainconnective concept
    subformula1 =Y
    form2   =A
    form3   =B
    form4   =C
    form5   =D
    form6   =E
    form7   =F
    ?retrieval>
    state   error
    ==>
    =g>
    isa     goal
    state   find_next_formula
    +imaginal>
    isa     checklist
    form2   =Z
    form3   =A
    form4   =B
    form5   =C
    form6   =D
    form7   =E
    form8   =F
    ~retrieval>
""")

aBoxCon.productionstring(name="find clash 2", string="""
    =g>
    isa     goal
    state   find_clash
    =imaginal>
    isa     checklist
    element =X
    mainconnective negation
    subformula1 =Y
    ?retrieval>
    state   free
    ==>
    =g>
    isa     goal
    state   signal_clash
    +retrieval>
    isa     proposition
    thing   proposition
    element  =X
    mainconnective concept
    subformula1 =Y
    derived  yes
""")

aBoxCon.productionstring(name="show clash 2", string="""
    =g>
    isa     goal
    state   signal_clash
    =imaginal>
    isa     checklist
    element =X
    mainconnective negation
    subformula1 =Y
    =retrieval>
    isa     proposition
    thing   proposition
    element  =X
    mainconnective concept
    subformula1 =Y
    ?manual>
    state   free
    ==>
    =g>
    isa     goal
    state   select
    +manual>
    isa     _manual
    cmd     press_key
    key     C
""")

aBoxCon.productionstring(name="no clash 2", string="""
    =g>
    isa     goal
    state   signal_clash
    =imaginal>
    isa     checklist
    form    =Z
    element =X
    mainconnective negation
    subformula1 =Y
    form2   =U1
    form3   =U2
    form4   =U3
    form5   =U4
    form6   =U5
    form7   =U6
    ?retrieval>
    state   error
    ==>
    =g>
    isa     goal
    state   find_next_formula
    +imaginal>
    isa     checklist
    form2   =Z
    form3   =U1
    form4   =U2
    form5   =U3
    form6   =U4
    form7   =U5
    form8   =U6
    ~retrieval>
""")

aBoxCon.productionstring(name="find next formula", string="""
    =g>
    isa     goal
    state   find_next_formula
    =imaginal>
    isa     checklist
    form2   =U0
    form3   =U1
    form4   =U2
    form5   =U3
    form6   =U4
    form7   =U5
    form8   =U6
    ?retrieval>
    state   free
    ==>
    =g>
    isa     goal
    state   decide
    +retrieval>
    isa     proposition
    thing   proposition
    derived yes
    form    ~=U0
    form    ~=U1
    form    ~=U2
    form    ~=U3
    form    ~=U4
    form    ~=U5
    form    ~=U6
    mainconnective ~disjunction
    mainconnective ~conjunction
    mainconnective ~relation
    mainconnective ~existential
    mainconnective ~universal
""")

aBoxCon.productionstring(name="repeat", string="""
    =g>
    isa     goal
    state   decide
    =retrieval>
    isa     proposition
    thing   proposition
    element =X
    mainconnective =Y
    subformula1 =Z
    form    =U
    =imaginal>
    isa     checklist
    form2   =U0
    form3   =U1
    form4   =U2
    form5   =U3
    form6   =U4
    form7   =U5
    form8   =U6
    ==>
    =g>
    isa     goal
    state   find_clash
    +imaginal>
    isa     checklist
    element =X
    mainconnective =Y
    subformula1 =Z
    form    =U
    form2   =U0
    form3   =U1
    form4   =U2
    form5   =U3
    form6   =U4
    form7   =U5
    form8   =U6
    ~retrieval>
""")

aBoxCon.productionstring(name="move on", string="""
    =g>
    isa     goal
    state   decide
    ?retrieval>
    state   error
    ==>
    =g>
    isa     goal
    state   module2
    ~retrieval>
""")


# In[6]:


aBoxCon.productionstring(name="find formula to apply rule to", string="""
    =g>
    isa      goal
    state    module2
    ?retrieval>
    state   free
    ==>
    =g>
    isa     goal
    state   find_rule
    +retrieval>
    isa     proposition
    thing   proposition
    mainconnective  conjunction
    derived  yes
""")

aBoxCon.productionstring(name="conjunction found, first conjunct inferred? 1", string="""
    =g>
    isa      goal
    state    find_rule
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    first_conjunct_inferred1
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    inferred1  no
    subformula2  =Z
    inferred2  no
    derived  yes
    ~retrieval>
""")

aBoxCon.productionstring(name="conjunction found, first conjunct inferred? 2", string="""
    =g>
    isa      goal
    state    first_conjunct_inferred1
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    inferred1  no
    subformula2  =Z
    inferred2  no
    derived  yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    first_conjunct_inferred2
    +retrieval>
    isa      proposition
    thing    proposition
    form     =X
    mainconnective conjunction
    inferred1 yes
""")

aBoxCon.productionstring(name="label first conjunct as inferred", string="""
    =g>
    isa      goal
    state    first_conjunct_inferred2
    ?retrieval>
    state    error
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    retrieve_first_conjunct
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred1  yes
    ~retrieval>
""")

aBoxCon.productionstring(name="retrieve first conjunct", string="""
    =g>
    isa      goal
    state    retrieve_first_conjunct
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred1  yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    label_first_conjunct
    +retrieval>
    isa      proposition
    thing    proposition
    form     =Y
""")

aBoxCon.productionstring(name="label first conjunct as derived", string="""
    =g>
    isa      goal
    state    label_first_conjunct
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    prepare_module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
""")

aBoxCon.productionstring(name="proceed to module 3", string="""
    =g>
    isa      goal
    state    prepare_module3
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    module3
""")

aBoxCon.productionstring(name="second conjunct inferred?", string="""
    =g>
    isa      goal
    state    first_conjunct_inferred2
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    mainconnective conjunction
    inferred1 yes
    ==>
    =g>
    isa      goal
    state    infer_second_conjunct_after_first
    +retrieval>
    isa      proposition
    thing    proposition
    form     =X
    mainconnective conjunction
    inferred1 yes
    inferred2 yes
""")

aBoxCon.productionstring(name="store in list 1", string="""
    =g>
    isa      goal
    state    infer_second_conjunct_after_first
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    inferred1 yes
    inferred2 yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    store_in_list
    +imaginal>
    isa      storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
""")

aBoxCon.productionstring(name="label second conjunct as inferred after first", string="""
    =g>
    isa      goal
    state    infer_second_conjunct_after_first
    ?retrieval>
    state    error
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    retrieve_second_conjunct_after_first
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred1 yes
    inferred2 yes
    ~retrieval>
""")

aBoxCon.productionstring(name="retrieve second conjunct after first", string="""
    =g>
    isa      goal
    state    retrieve_second_conjunct_after_first
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred1 yes
    inferred2 yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    label_second_conjunct_after_first
    +retrieval>
    isa      proposition
    thing    proposition
    form     =Z
""")

aBoxCon.productionstring(name="label second conjunct as derived after first", string="""
    =g>
    isa      goal
    state    label_second_conjunct_after_first
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    prepare_module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
""")


#--------------------------------------------------------------------------------------------------


aBoxCon.productionstring(name="conjunction found, second conjunct inferred? 1", string="""
    =g>
    isa      goal
    state    find_rule
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    second_conjunct_inferred1
    ~retrieval>
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    inferred1  no
    subformula2  =Z
    inferred2  no
    derived  yes
""")

aBoxCon.productionstring(name="conjunction found, second conjunct inferred? 2", string="""
    =g>
    isa      goal
    state    second_conjunct_inferred1
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    inferred1  no
    subformula2  =Z
    inferred2  no
    derived  yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    second_conjunct_inferred2
    +retrieval>
    isa      proposition
    thing    proposition
    form     =X
    mainconnective conjunction
    inferred2 yes
""")

aBoxCon.productionstring(name="label second conjunct as inferred", string="""
    =g>
    isa      goal
    state    second_conjunct_inferred2
    ?retrieval>
    state    error
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    retrieve_second_conjunct
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred2  yes
    ~retrieval>
""")

aBoxCon.productionstring(name="retrieve second conjunct", string="""
    =g>
    isa      goal
    state    retrieve_second_conjunct
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred2  yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    label_second_conjunct
    +retrieval>
    isa      proposition
    thing    proposition
    form     =Z
""")

aBoxCon.productionstring(name="label second conjunct as derived", string="""
    =g>
    isa      goal
    state    label_second_conjunct
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    prepare_module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
""")

aBoxCon.productionstring(name="first conjunct inferred?", string="""
    =g>
    isa      goal
    state    second_conjunct_inferred2
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    mainconnective conjunction
    inferred2 yes
    ==>
    =g>
    isa      goal
    state    infer_first_conjunct_after_second
    +retrieval>
    isa      proposition
    thing    proposition
    form     =X
    mainconnective conjunction
    inferred1 yes
    inferred2 yes
""")

aBoxCon.productionstring(name="store in list 2", string="""
    =g>
    isa      goal
    state    infer_first_conjunct_after_second
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    inferred1 yes
    inferred2 yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    store_in_list
    +imaginal>
    isa      storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
""")

aBoxCon.productionstring(name="label first conjunct as inferred after second", string="""
    =g>
    isa      goal
    state    infer_first_conjunct_after_second
    ?retrieval>
    state    error
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    ==>
    =g>
    isa      goal
    state    retrieve_first_conjunct_after_second
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred1 yes
    inferred2 yes
    ~retrieval>
""")

aBoxCon.productionstring(name="retrieve first conjunct after second", string="""
    =g>
    isa      goal
    state    retrieve_first_conjunct_after_second
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective conjunction
    subformula1  =Y
    subformula2  =Z
    derived  yes
    inferred1 yes
    inferred2 yes
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    label_first_conjunct_after_second
    +retrieval>
    isa      proposition
    thing    proposition
    form     =Y
""")

aBoxCon.productionstring(name="label first conjunct as derived after second", string="""
    =g>
    isa      goal
    state    label_first_conjunct_after_second
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    prepare_module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
""")


# In[7]:


aBoxCon.productionstring(name="do we need to check for a clash? concept found", string="""
    =g>
    isa      goal
    state    module3
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective concept
    subformula1  =Y
    derived  yes
    ==>
    =g>
    isa      goal
    state    find_clash
    +imaginal>
    isa      checklist
    mainconnective concept
    element  =U
    subformula1 =Y
    form     =X
    ~retrieval>
""")

aBoxCon.productionstring(name="do we need to check for a clash? negation found", string="""
    =g>
    isa      goal
    state    module3
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective negation
    subformula1  =Y
    derived  yes
    ==>
    =g>
    isa      goal
    state    find_clash
    +imaginal>
    isa      checklist
    mainconnective negation
    element  =U
    subformula1 =Y
    form     =X
    ~retrieval>
""")
    
aBoxCon.productionstring(name="do we need to derive something new?", string="""
    =g>
    isa      goal
    state    module3
    =imaginal>
    isa      proposition
    thing    proposition
    element  =X
    subformula1 =Y
    form     =Z
    mainconnective ~concept
    mainconnective ~negation
    ==>
    =g>
    isa      goal
    state    module2
    ~imaginal>
    ~retrieval>
""")


# In[8]:


aBoxCon.productionstring(name="retrieve the next proposition to store in the list", string="""
    =g>
    isa      goal
    state    store_in_list
    =imaginal>
    isa      storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    form2    =T1
    form3    =T2
    form4    =T3
    form5    =T4
    form6    =T5
    form7    =T6
    form8    =T7
    form9    =T8
    form10   =T9
    form11   =T10
    form12   =T11
    form13   =T12
    form14   =T13
    form15   =T14
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    store_in_list2
    +retrieval>
    isa      proposition
    thing    proposition
    form     ~=X
    form     ~=T1
    form     ~=T2
    form     ~=T3
    form     ~=T4
    form     ~=T5
    form     ~=T6
    form     ~=T7
    form     ~=T8
    form     ~=T9
    form     ~=T10
    form     ~=T11
    form     ~=T12
    form     ~=T13
    form     ~=T14
    derived  yes
    inferred1 yes
    inferred2 yes
""")

aBoxCon.productionstring(name="store the next proposition in the list", string="""
    =g>
    isa      goal
    state    store_in_list2
    =imaginal>
    isa      storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    form2    =T1
    form3    =T2
    form4    =T3
    form5    =T4
    form6    =T5
    form7    =T6
    form8    =T7
    form9    =T8
    form10   =T9
    form11   =T10
    form12   =T11
    form13   =T12
    form14   =T13
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X2
    derived  yes
    inferred1 yes
    inferred2 yes
    element  =Y2
    mainconnective =Z2
    relation =U2
    subformula1 =V2
    subformula2 =W2
    ==>
    =g>
    isa      goal
    state    store_in_list
    +imaginal>
    isa      storelist
    element  =Y2
    mainconnective =Z2
    relation =U2
    subformula1 =V2
    subformula2 =W2
    form     =X2
    form2    =X
    form3    =T1
    form4    =T2
    form5    =T3
    form6    =T4
    form7    =T5
    form8    =T6
    form9    =T7
    form10   =T8
    form11   =T9
    form12   =T11
    form13   =T11
    form14   =T12
    form15   =T13
    derived  yes
    inferred1 yes
    inferred2 yes
""")

aBoxCon.productionstring(name="use the list to select the next formula", string="""
    =g>
    isa      goal
    state    store_in_list2
    =imaginal>
    isa      storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    form2    =T1
    form3    =T2
    form4    =T3
    form5    =T4
    form6    =T5
    form7    =T6
    form8    =T7
    form9    =T8
    form10   =T9
    form11   =T10
    form12   =T11
    form13   =T12
    form14   =T13
    ?retrieval>
    state    error
    ==>
    =g>
    isa     goal
    state   find_rule
    +retrieval>
    isa     proposition
    thing   proposition
    form     ~=X
    form     ~=T1
    form     ~=T2
    form     ~=T3
    form     ~=T4
    form     ~=T5
    form     ~=T6
    form     ~=T7
    form     ~=T8
    form     ~=T9
    form     ~=T10
    form     ~=T11
    form     ~=T12
    form     ~=T13
    mainconnective  conjunction
    derived  yes
""")

aBoxCon.productionstring(name="confirm consistency", string="""
    =g>
    isa      goal
    state    find_rule
    ?retrieval>
    state    error
    ==>
    =g>
    isa     goal
    state   stop
    +manual>
    isa     _manual
    cmd     press_key
    key     N
""")

aBoxCon_sim = aBoxCon.simulation(realtime=False,gui=False,trace=False,
    environment_process=environment.environment_process,
    triggers='space',
    times=2)

parser.AddAboxFromFile("abox.txt",dm.add)

while True:
    try:
        aBoxCon_sim.step()
    except simpy.core.EmptySchedule:
        break
    if re.match("^RULE FIRED:.*derived",aBoxCon_sim.current_event.action):
        for x in imaginal:
            print("FOCUS: " + str(x.form))
        for x in retrieval:
            print("DERIVED: "+ str(x.form) + "\n")

print("DONE")