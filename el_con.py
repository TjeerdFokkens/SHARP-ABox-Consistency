import pyactr as actr

aBoxCon = actr.ACTRModel(
    automatic_visual_search=False,
    motor_prepared=True,
 #   subsymbolic=True,
    utility_noise=0.2,
    partial_matching=False,
 #   utility_learning=True,
 #   production_compilation=True,
    activation_trace=True,
    retrieval_threshold=0,
    decay=0
)

aBoxCon.goals = {}
aBoxCon.set_goal("g")
aBoxCon.set_goal("imaginal")
aBoxCon.set_goal("imaginal_action")

actr.chunktype("goal", "state")
actr.chunktype("proposition", "thing, form, element, mainconnective, relation, subformula1, inferred1, subformula2, inferred2, derived")
actr.chunktype("checklist", "thing, form, element, mainconnective, relation, subformula1, subformula2, form2, form3, form4, form5, form6, form7, form8")
actr.chunktype("storelist", "thing, form, element, mainconnective, relation, subformula1, subformula2, derived, inferred1, inferred2, form2, form3, form4, form5, form6, form7, form8, form9, form10, form11, form12, form13, form14, form15")

dm = aBoxCon.decmem
goal = aBoxCon.goals["g"]
imaginal = aBoxCon.goals["imaginal"]
imaginal_action = aBoxCon.goals["imaginal_action"]
retrieval = aBoxCon.retrieval
production = aBoxCon.productions

aBoxCon.goals["g"].add(actr.makechunk(typename="goal", state="start"))
aBoxCon.goals["imaginal"].add(actr.makechunk(typename="checklist", thing="checklist"))


# In[121]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A&/Es.F", element="a", mainconnective="conjunction", subformula1="a:A", subformula2="a:/Es.F", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:/As.(nF%nB)", element="a", mainconnective="universal", relation="s", subformula1="b:nF%nB", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:B", element="b", mainconnective="concept", subformula1="B", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,b):s", mainconnective="relation", relation="s", subformula1="a", subformula2="b", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,c):r", mainconnective="relation", relation="r", subformula1="a", subformula2="c", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:C&/Es.D", element="c", mainconnective="conjunction", subformula1="c:C", subformula2="c:/Es.D", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A", element="a", mainconnective="concept", subformula1="A", derived="no"))
#dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:F", element="x", mainconnective="concept", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nF%nB", element="b", mainconnective="disjunction", subformula1="b:nF", subformula2="b:nB", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nF", element="b", mainconnective="negation", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:/Es.F", element="a", mainconnective="existential", relation="s", subformula1="x:F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(a,x):s", mainconnective="relation", relation="s", subformula1="a", subformula2="x", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nF%nB", element="x", mainconnective="disjunction", subformula1="x:nF", subformula2="x:nB", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nB", element="x", mainconnective="negation", subformula1="B", derived="no"))
#dm.add(actr.makechunk(typename="proposition", thing="proposition", form="b:nB", element="b", mainconnective="negation", subformula1="B", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="x:nF", element="x", mainconnective="negation", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:C", element="c", mainconnective="concept", subformula1="C", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="c:/Es.D", element="c", mainconnective="existential", relation="s", subformula1="y:D", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="y:D", element="y", mainconnective="concept", subformula1="D", derived="no"))
#5,95 #7,66


# In[68]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="fredrik:teacher&supervisor", element="fredrik", mainconnective="conjunction", subformula1="fredrik:teacher", subformula2="fredrik:supervisor", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:student", element="tjeerd", mainconnective="concept", subformula1="student", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:teacher&(supervisor&headofresearch)", element="graham", mainconnective="conjunction", subformula1="graham:teacher", subformula2="graham:supervisor&headofresearch", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(tjeerd,fredrik):supervisedby", mainconnective="relation", relation="supervisedby", subformula1="tjeerd", subformula2="fredrik", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:student&employee", element="tjeerd", mainconnective="conjunction", subformula1="tjeerd:student", subformula2="tjeerd:employee", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="fredrik:teacher", element="fredrik", mainconnective="concept", subformula1="teacher", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="fredrik:supervisor", element="fredrik", mainconnective="concept", subformula1="supervisor", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:teacher", element="graham", mainconnective="concept", subformula1="teacher", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:supervisor&headofresearch", element="graham", mainconnective="conjunction", subformula1="graham:supervisor", subformula2="graham:headofresearch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:supervisor", element="graham", mainconnective="concept", subformula1="supervisor", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:headofresearch", mainconnective="concept", subformula1="headofresearch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:student", element="tjeerd", mainconnective="concept", subformula1="student", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:employee", element="tjeerd", mainconnective="concept", subformula1="employee", derived="no"))
#16,35


# In[40]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="fredrik:teacher&supervisor", element="fredrik", mainconnective="conjunction", subformula1="fredrik:teacher", subformula2="fredrik:supervisor", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:student", element="tjeerd", mainconnective="concept", subformula1="student", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:teacher&(supervisor&headofresearch)", element="graham", mainconnective="conjunction", subformula1="graham:teacher", subformula2="graham:supervisor&headofresearch", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="(tjeerd,fredrik):supervisedby", mainconnective="relation", relation="supervisedby", subformula1="tjeerd", subformula2="fredrik", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:student&employee", element="tjeerd", mainconnective="conjunction", subformula1="tjeerd:student", subformula2="tjeerd:employee", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:nheadofresearch", element="graham", mainconnective="negation", subformula1="headofresearch", derived="yes"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="fredrik:teacher", element="fredrik", mainconnective="concept", subformula1="teacher", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="fredrik:supervisor", element="fredrik", mainconnective="concept", subformula1="supervisor", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:teacher", element="graham", mainconnective="concept", subformula1="teacher", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:supervisor&headofresearch", element="graham", mainconnective="conjunction", subformula1="graham:supervisor", subformula2="graham:headofresearch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:supervisor", element="graham", mainconnective="concept", subformula1="supervisor", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="graham:headofresearch", element="graham", mainconnective="concept", subformula1="headofresearch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:student", element="tjeerd", mainconnective="concept", subformula1="student", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="tjeerd:employee", element="tjeerd", mainconnective="concept", subformula1="employee", derived="no"))
#9,5 #35,36


# In[4]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:(austrian&logician)&(Einsteinsfriend&incomplete)", element="godel", mainconnective="conjunction", subformula1="godel:austrian&logician", subformula2="godel:Einsteinsfriend&incomplete", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:austrian&(logician&(Einsteinsfriend&incomplete))", element="godel", mainconnective="conjunction", subformula1="godel:austrian", subformula2="godel:logician&(Einsteinsfriend&incomplete)", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:austrian&((logician&Einsteinsfriend)&incomplete)", element="godel", mainconnective="conjunction", subformula1="godel:austrian", subformula2="godel:(logician&Einsteinsfriend)&incomplete", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:(austrian&(logician&Einsteinsfriend))&incomplete", element="godel", mainconnective="conjunction", subformula1="godel:austrian&(logician&Einsteinsfriend)", subformula2="godel:incomplete", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:austrian&logician", element="godel", mainconnective="conjunction", subformula1="godel:austrian", subformula2="godel:logician", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:Einsteinsfriend&incomplete", element="godel", mainconnective="conjunction", subformula1="godel:Einsteinsfriend", subformula2="godel:incomplete", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:austrian", element="godel", mainconnective="concept", subformula1="austrian", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:logician", element="godel", mainconnective="concept", subformula1="logician", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:Einsteinsfriend", element="godel", mainconnective="concept", subformula1="Einsteinsfriend", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:incomplete", element="godel", mainconnective="concept", subformula1="incomplete", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:logician&(Einsteinsfriend&incomplete)", element="godel", mainconnective="conjunction", subformula1="godel:logician", subformula2="godel:Einsteinsfriend&incomplete", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:(logician&Einsteinsfriend)&incomplete", element="godel", mainconnective="conjunction", subformula1="godel:logician&Einsteinsfriend", subformula2="godel:incomplete", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:austrian&(logician&Einsteinsfriend)", element="godel", mainconnective="conjunction", subformula1="godel:austrian", subformula2="godel:logician&Einsteinsfriend", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="godel:logician&Einsteinsfriend", element="godel", mainconnective="conjunction", subformula1="godel:logician", subformula2="godel:Einsteinsfriend", derived="no", inferred1="no", inferred2="no"))
#32,85


# In[8]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:logician&(Enayatsfriend&(dutch&funny))", element="visser", mainconnective="conjunction", subformula1="visser:logician", subformula2="visser:Enayatsfriend&(dutch&funny)", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:logician&(Enayatsfriend&(dutch&nfunny))", element="visser", mainconnective="conjunction", subformula1="visser:logician", subformula2="visser:Enayatsfriend&(dutch&nfunny)", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:logician", element="visser", mainconnective="concept", subformula1="logician", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:Enayatsfriend&(dutch&nfunny)", element="visser", mainconnective="conjunction", subformula1="visser:Enayatsfriend", subformula2="visser:dutch&nfunny", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:Enayatsfriend", element="visser", mainconnective="concept", subformula1="Enayatsfriend", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:dutch&nfunny", element="visser", mainconnective="conjunction", subformula1="visser:dutch", subformula2="visser:nfunny", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:dutch", element="visser", mainconnective="concept", subformula1="dutch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:nfunny", element="visser", mainconnective="negation", subformula1="funny", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:dutch&funny", element="visser", mainconnective="conjunction", subformula1="visser:dutch", subformula2="visser:funny", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:funny", element="visser", mainconnective="concept", subformula1="funny", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="visser:Enayatsfriend&(dutch&funny)", element="visser", mainconnective="conjunction", subformula1="visser:Enayatsfriend", subformula2="visser:dutch&funny", derived="no", inferred1="no", inferred2="no"))
#15,2


# In[40]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:dutch", element="giacomo", mainconnective="concept", subformula1="dutch", derived="yes", relation="none", inferred1="none", subformula2="none", inferred2="none"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:ndutch&(logician&footballplayer)", element="giacomo", mainconnective="conjunction", subformula1="giacomo:ndutch", subformula2="giacomo:logician&footballplayer", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:ndutch", element="giacomo", mainconnective="negation", subformula1="dutch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:logician&footballplayer", element="giacomo", mainconnective="conjunction", subformula1="giacomo:logician", subformula2="giacomo:footballplayer", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:logician", element="giacomo", mainconnective="concept", subformula1="logician", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:footballplayer", element="giacomo", mainconnective="concept", subformula1="footballplayer", derived="no"))
#1,45 #2,5


# In[49]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:nfootballplayer", element="giacomo", mainconnective="negation", subformula1="footballplayer", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:ndutch&(logician&footballplayer)", element="giacomo", mainconnective="conjunction", subformula1="giacomo:ndutch", subformula2="giacomo:logician&footballplayer", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:ndutch", element="giacomo", mainconnective="negation", subformula1="dutch", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:logician&footballplayer", element="giacomo", mainconnective="conjunction", subformula1="giacomo:logician", subformula2="giacomo:footballplayer", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:logician", element="giacomo", mainconnective="concept", subformula1="logician", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="giacomo:footballplayer", element="giacomo", mainconnective="concept", subformula1="footballplayer", derived="no"))
#4,8 #6.44


# In[42]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A", element="a", mainconnective="concept", subformula1="A", derived="yes"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A&(B&C)", element="a", mainconnective="conjunction", subformula1="a:A", subformula2="a:B&C", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A&(D&E)", element="a", mainconnective="conjunction", subformula1="a:A", subformula2="a:D&E", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:A&(F&G)", element="a", mainconnective="conjunction", subformula1="a:A", subformula2="a:F&G", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:B", element="a", mainconnective="concept", subformula1="B", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:C", element="a", mainconnective="concept", subformula1="C", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:B&C", element="a", mainconnective="conjunction", subformula1="a:B", subformula2="a:C", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:D", element="a", mainconnective="concept", subformula1="D", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:E", element="a", mainconnective="concept", subformula1="E", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:D&E", element="a", mainconnective="conjunction", subformula1="a:D", subformula2="a:E", derived="no", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:F", element="a", mainconnective="concept", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:G", element="a", mainconnective="concept", subformula1="G", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:F&G", element="a", mainconnective="conjunction", subformula1="a:F", subformula2="a:G", derived="no", inferred1="no", inferred2="no"))
#21,75


# In[51]:


dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:B&C", element="a", mainconnective="conjunction", subformula1="a:B", subformula2="a:C", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:D&E", element="a", mainconnective="conjunction", subformula1="a:D", subformula2="a:E", derived="yes", inferred1="no", inferred2="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:F&G", element="a", mainconnective="conjunction", subformula1="a:F", subformula2="a:G", derived="yes", inferred1="no", inferred2="no"))

dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:B", element="a", mainconnective="concept", subformula1="B", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:C", element="a", mainconnective="concept", subformula1="C", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:D", element="a", mainconnective="concept", subformula1="D", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:E", element="a", mainconnective="concept", subformula1="E", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:F", element="a", mainconnective="concept", subformula1="F", derived="no"))
dm.add(actr.makechunk(typename="proposition", thing="proposition", form="a:G", element="a", mainconnective="concept", subformula1="G", derived="no"))
#12,45


# In[122]:


aBoxCon.productionstring(name="find first formula", string="""
    =g>
    isa     goal
    state   start
    =imaginal>
    isa     checklist
    thing   checklist
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

aBoxCon.productionstring(name="skip and derive first formula", string="""
    =g>
    isa     goal
    state   store
    =imaginal>
    isa     checklist
    thing   checklist
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
    thing   checklist
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
    thing   checklist
    form    =U
    element =X
    mainconnective =Y
    subformula1 =Z
    relation none
    subformula2 none
    form2   none
    form3   none
    form4   none
    form5   none
    form6   none
    form7   none
    form8   none
""")

aBoxCon.productionstring(name="find clash 1", string="""
    =g>
    isa     goal
    state   find_clash
    =imaginal>
    isa     checklist
    thing   checklist
    element =X
    mainconnective concept
    relation =G
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
    thing   checklist
    element =X
    mainconnective concept
    subformula1 =Y
    relation =G
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
    thing   checklist
    element =X
    form    =X1
    mainconnective concept
    subformula1 =Y
    relation =Z1
    subformula2 =Z2
    form2   =Z3
    form3   =Z4
    form4   =Z5
    form5   =Z6
    form6   =Z7
    form7   =Z8
    form8   =Z9
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
    state   stop
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
    thing   checklist
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
    form8   =G
    relation =Z1
    subformula2 =Z2
    ?retrieval>
    state   error
    ==>
    =g>
    isa     goal
    state   find_next_formula
    +imaginal>
    isa     checklist
    thing   checklist
    form    none
    element none
    mainconnective none
    subformula1 none
    subformula2 none
    relation none
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
    thing   checklist
    element =X
    mainconnective negation
    subformula1 =Y
    relation =G
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
    thing   checklist
    element =X
    mainconnective negation
    subformula1 =Y
    relation =G
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
    thing   checklist
    element =X
    form    =X1
    mainconnective negation
    subformula1 =Y
    relation =Z1
    subformula2 =Z2
    form2  =Z3
    form3  =Z4
    form4  =Z5
    form5  =Z6
    form6  =Z7
    form7  =Z8
    form8  =Z9
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
    state   stop
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
    thing   checklist
    form    =Z
    element =X
    mainconnective negation
    subformula1 =Y
    form2   =A
    form3   =B
    form4   =C
    form5   =D
    form6   =E
    form7   =F
    form8   =G
    relation =Z1
    subformula2 =Z2
    ?retrieval>
    state   error
    ==>
    =g>
    isa     goal
    state   find_next_formula
    +imaginal>
    isa     checklist
    thing   checklist
    form    none
    element none
    mainconnective none
    subformula1 none
    subformula2 none
    relation none
    form2   =Z
    form3   =A
    form4   =B
    form5   =C
    form6   =D
    form7   =E
    form8   =F
    ~retrieval>
""")

aBoxCon.productionstring(name="find next formula", string="""
    =g>
    isa     goal
    state   find_next_formula
    =imaginal>
    isa     checklist
    thing   checklist
    form    =X1
    mainconnective =X2
    subformula1 =X3
    subformula2 =X4
    relation =X5
    element =X6
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
    form    ~=X1
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
    =imaginal>
    isa     checklist
    thing   checklist
    form    =X1
    mainconnective =X2
    subformula1 =X3
    subformula2 =X4
    relation =X5
    element =X6
    form2   =U0
    form3   =U1
    form4   =U2
    form5   =U3
    form6   =U4
    form7   =U5
    form8   =U6
""")

aBoxCon.productionstring(name="repeat", string="""
    =g>
    isa     goal
    state   decide
    =retrieval>
    isa     proposition
    element =X
    mainconnective =Y
    subformula1 =Z
    form    =U
    thing   proposition
    =imaginal>
    isa     checklist
    thing   checklist
    form    none
    element none
    mainconnective none
    subformula1 none
    subformula2 none
    relation none
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
    thing   checklist
    form    =U
    element =X
    mainconnective =Y
    subformula1 =Z
    subformula2 none
    relation none
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


# In[123]:


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
    relation none
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
    relation none
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
    relation none
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
    relation none
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
    inferred2  none
    relation   none
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
    ~imaginal>
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
    state    module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
    relation none
    inferred1 none
    inferred2 none
""")

aBoxCon.productionstring(name="second_conjunct_inferred_a", string="""
    =g>
    isa      goal
    state    first_conjunct_inferred2
    ?retrieval>
    buffer   full
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 yes
    subformula2 =V
    inferred2 =W
    derived   =Z
    relation none
    ?imaginal>
    state    free
    =imaginal>
    isa      proposition
    thing    proposition
    form     =T1
    element  =T2
    mainconnective conjunction
    subformula1  =T3
    inferred1  no
    subformula2  =T4
    inferred2  no
    derived  yes
    relation none
    ==>
    =g>
    isa      goal
    state    pre_infer_second_conjunct_after_first
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 yes
    subformula2 =V
    inferred2 =W
    derived   =Z
    relation  none
    ~retrieval>
""")

aBoxCon.productionstring(name="second_conjunct_inferred_b", string="""
    =g>
    isa      goal
    state    pre_infer_second_conjunct_after_first
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 yes
    subformula2 =V
    inferred2 =W
    derived   =Z
    relation none
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    infer_second_conjunct_after_first
    +retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 yes
    subformula2 =V
    inferred2 yes
    derived   =Z
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 yes
    subformula2 =V
    inferred2 =W
    derived   =Z
    relation  none
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
    thing    storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    derived  none
    inferred1 none
    inferred2 none
    form2    none
    form3    none
    form4    none
    form5    none
    form6    none
    form7    none
    form8    none
    form9    none
    form10   none
    form11   none
    form12   none
    form13   none
    form14   none
    form15   none
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
    relation none
    inferred1 =S1
    inferred2 =S2
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
    relation  none
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
    relation  none
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
    element  =U
    derived  no
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
    relation  none
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
    relation  =S
    inferred1  =S1
    inferred2  =S2
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
    relation  =S
    inferred1 =S1
    inferred2 =S2
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
    relation none
    ~retrieval>
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
    relation none
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
    relation none
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
    relation none
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
    inferred1  none
    relation   none
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
    state    module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
    relation  none
    inferred1 none
    inferred2 none
""")

aBoxCon.productionstring(name="first_conjunct_inferred_a", string="""
    =g>
    isa      goal
    state    second_conjunct_inferred2
    ?retrieval>
    buffer   full
    ?retrieval>
    state    free
    =retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 =W
    subformula2 =V
    inferred2 yes
    derived   =Z
    relation none
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    pre_infer_first_conjunct_after_second
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 =W
    subformula2 =V
    inferred2 yes
    derived   =Z
    relation  none
    ~retrieval>
""")

aBoxCon.productionstring(name="first_conjunct_inferred_b", string="""
    =g>
    isa      goal
    state    pre_infer_first_conjunct_after_second
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 =W
    subformula2 =V
    inferred2 yes
    derived   =Z
    relation  none
    ?retrieval>
    state    free
    ==>
    =g>
    isa      goal
    state    infer_first_conjunct_after_second
    +retrieval>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 yes
    subformula2 =V
    inferred2 yes
    derived   =Z
    =imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =Y
    mainconnective conjunction
    subformula1 =U
    inferred1 =W
    subformula2 =V
    inferred2 yes
    derived   =Z
    relation  none
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
    thing    storelist
    form     =X
    element  =Y
    mainconnective =Z
    relation =U
    subformula1 =V
    subformula2 =W
    derived  none
    inferred1  none
    inferred2  none
    form2    none
    form3    none
    form4    none
    form5    none
    form6    none
    form7    none
    form8    none
    form9    none
    form10   none
    form11   none
    form12   none
    form13   none
    form14   none
    form15   none
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
    relation none
    inferred1 =S1
    inferred2 =S2
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
    relation  none
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
    relation  none
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
    derived  no
    element  =U
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
    relation  none
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
    relation  =S
    inferred1  =S1
    inferred2  =S2
    ?imaginal>
    state    free
    ==>
    =g>
    isa      goal
    state    module3
    +imaginal>
    isa      proposition
    thing    proposition
    form     =X
    element  =U
    mainconnective =V
    subformula1  =Y
    subformula2  =Z
    derived  yes
    relation   =S
    inferred1  =S1
    inferred2  =S2
""")


# In[124]:


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
    thing    checklist
    form     =X
    mainconnective concept
    element  =U
    subformula1 =Y
    relation none
    subformula2 none
    form2    none
    form3    none
    form4    none
    form5    none
    form6    none
    form7    none
    form8    none
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
    thing    checklist
    mainconnective negation
    element  =U
    subformula1 =Y
    form     =X
    relation none
    subformula2 none
    form2    none
    form3    none
    form4    none
    form5    none
    form6    none
    form7    none
    form8    none
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


# In[125]:


aBoxCon.productionstring(name="retrieve the next proposition to store in the list", string="""
    =g>
    isa      goal
    state    store_in_list
    =imaginal>
    isa      storelist
    thing    storelist
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
    derived  =S1
    inferred1 =S2
    inferred2 =S3
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
    thing    storelist
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
    derived   =S1
    inferred1 =S2
    inferred2 =S3
    form15    =S4
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
    thing    storelist
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
    thing    storelist
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
    derived   =S1
    inferred1 =S2
    inferred2 =S3
    form15    =S4
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
    form     ~=S4
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


# In[126]:


aBoxCon_sim = aBoxCon.simulation(realtime=False,gui=False)


# In[127]:


aBoxCon_sim.run(40)


# In[71]:


dm


# In[76]:


retrieval


# In[133]:


goal


# In[86]:


imaginal


# In[87]:


imaginal_action


# In[35]:


production


# In[165]:


aBoxCon.MODEL_PARAMETERS

