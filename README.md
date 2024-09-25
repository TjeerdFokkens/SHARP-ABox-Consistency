# SHARP: ABox-Consistency
SHARP simulates the reasoning process that a human user might perform in deciding whether a given ABox (in the description logic 𝒜ℒℰ) is consistent.
The simulation results can then be used to estimate the cognitively adequate complexity of this task.
Below follows a brief explanation; for in-depth information, please refer to the short paper:

J.T. Fokkens and F. Engström, 'Cognitively adequate complexity of reasoning in a description logic: extended abstract',
https://ceur-ws.org/Vol-3548/paper6.pdf

Or, for even more detail, this thesis:
J.T.Fokkens, 'Modelling the logical mind - Using the cognitive architecture ACT-R to model human symbolic reasoning in the description logic 𝒜ℒℰ',
https://gupea.ub.gu.se/handle/2077/74797


# SHARP in brief
SHARP performs the ABox consistency algorithm (restricted to 𝒜ℒℰ) from page 75 from the book 'An Introduction to Description Logic', by F. Baader, I. Horrocks, C. Lutz and U. Sattler, as if it were run on a human brain.
It does this by using the cognitive architecture ACT-R, into which the algorithm is implemented.
For more info on ACT-R, please refer to: J. Whitehill, 'Understanding act-r - an outsider’s perspective', https://doi.org/10.48550/arXiv.1306.0125.

The algorithm is a tableaux-style algorithm and applies so-called syntax expansion rules to the formulas in the given ABox until no such rule can be applied anymore.

The formulas that the algorithm works with are implemented as chunks, and the syntax expansion rules are implemented as production rules.
The code of the model is naturally distributed over 5 components that each perform their own subroutine.
Component 1 looks for a clash among atomic concept assignments; a clash is a set of two formulas that assign conflicting concepts to the same element.
Component 2 randomly selects a formula (either a given one or one already derived) that allows for an inference to be made.
Component 3 derives concept assignments with the respective conjuncts from a conjunction concept assignment.
Component 4 derives a relation and a concept assignment from a concept assigment the main connective of which is an existential restriction.
Component 5 derives a concept assignment from both a relation and a concept assignment the main connective of which is a universal restriction.
Visual overviews of both the model as a whole and of the components separately can be found in the folder VisualExplanation.

Because ACT-R does not allow for directly parsing strings, the process of 'deriving' generally works like this:
1. before the simulation starts, all strings that could possible be derived from the given ABox are loaded into ACT-R's declarative memory
2. in case a formula with some specified characteristics needs to be derived, a search is made in ACT-R's declarative memory
3. a formula that satisfies the criteria is then retrieved from the declarative memory (randomly in case multiple formulas qualify)
4. the found formula is labelled as derived, making it impossible to be derived again


# Notation
The model uses a notation different from the standard description logic notation.
Negation/complement, usually written ¬A is written in SHARP as -A
Conjunction/intersection, usually written (A⊓B) is written in SHARP as (A&B)
Universal restriction, usually written ∀𝑟.A is written in SHARP as /Ar.A
Existential restriction, usually written ∃𝑟.A is written in SHARP as /Er.A


# Files
The Component1-5.py files contain the production rules of the ACT-R system.

parser.py contains code that takes an ABox and feeds it - in the appropriate form - into SHARP.

GenerateData is a file that runs the simulations to generate data.
It can be directly executed in Python to perform these simulations on a testset of ABoxes that is given in the file.
Alternatively, this testset can be replaced by a set of ABoxes of choice.


# Dependencies
The following packages are necessary to run this code.
Numpy: https://numpy.org/doc/stable/index.html
Pandas: https://pandas.pydata.org
Pyactr: https://github.com/jakdot/pyactr
Lark: https://lark-parser.readthedocs.io/en/stable/


