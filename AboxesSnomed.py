import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

aboxes_from_snomed = ['a:(A&(B&/Er.C))',
'a:(A&(B&(C&(/Er.D&(/Es.E&(/Et.F&(/Eu.G&/Ev.H)))))))',
'a:(A&(B&(/Er.C&(/Es.D&(/Et.E&/Eu.F)))))',
'a:(A&(B&(/Er.C&(/Es.D&/Et.E))))',
'a:(A&(/Er.C&(/Es.D&/Et.E)))',
'a:(A&(B&(C&(/Er.D&/Es.E))))',
'a:(A&(B&(/Er.C&/Es.D)))',
'a:(A&(B&(C&(D&(/Er.E&/Es.F)))))',
'a:(A&(/Er.E&/Es.F))',
'a:(A&(B&(C&(/Er.E&(/Es.F&(/Et.G&/Eu.H))))))',
'a:(A&(/Er.E&(/Es.F&(/Et.G&/Eu.H))))',
'a:(A&/Er.E)',
'a:(A&(B&(C&(D&(J&(K&(/Er.E&(/Es.F&(/Et.G&(/Eu.H&(/Ev.I&/Ew.L)))))))))))',
'a:(A&(B&(C&(D&(J&(/Er.E&/Es.F))))))',
'a:(A&(B&(C&(/Er.E&(/Es.F&/Et.G)))))',
'a:(A&(B&(C&(D&(/Er.E&(/Es.F&(/Et.G&/Eu.H)))))))',
'a:(A&(B&(C&(D&(/Er.E&(/Es.F&(/Et.G&(/Eu.H&(/Ev.I&/Ew.L)))))))))',
'a:(A&B)',
'a:(A&(B&C))',
'a:(A&(B&(/Er.E&(/Es.F&(/Et.G&(/Eu.H&(/Ev.I&/Ew.L)))))))',
'a:(A&(B&(C&(/Er.E&(/Es.F&(/Et.G&(/Eu.H&(/Ev.I&/Ew.L))))))))',
'a:(A&(B&(C&(D&/Er.E))))',
'a:(A&(B&(C&(D&(/Er.E&(/Es.F&(/Et.G&/Eu.H)))))))']
