import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

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


#Make the graph showing the exponential increase in run time with the input size.
x = [5,9,12,16,19]
y = [x/10 for x in [38.201,90.531,213.17,564.818,1274.268]]
xdata = np.linspace(2,20,50)
def func(x,a,b):
    return a * np.exp(b * x)
popt,pcov = curve_fit(func, x, y)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')
print(popt)
li = [func(i, *popt) for i in x]
a = li
for i in range(len(li)):
    a[i] = (y[i]-li[i])**2
y_mean = sum(y)/len(y)
y_dif = [(i-y_mean)**2 for i in y]
R2=1-sum(a)/sum(y_dif)
print(R2)
plt.scatter(x, y)
plt.xlabel('Size of ABox')
plt.ylabel('Run time (s)')
plt.title('Run time scales exponentially with ABox size')
plt.savefig('ExponentialIncrease.png', transparent=True, dpi=1200)
plt.show()
