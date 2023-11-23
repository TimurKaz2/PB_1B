import numpy as np
import matplotlib.pyplot as plt
#---------------------------------------------------
mu,sigma,Ex=0.08 , 0.02 , 2.718
x = np.linspace(0, 100, 1000)
norm=(1/(sigma*((2*3.14)**0.5)))*Ex**(-((x-mu)**2/(25)**2))
#----------------------------------------------------
f=[]
f.extend(norm[::-1])
f.extend(norm)
x = np.linspace(0, 200, 2000)
plt.plot(x,f)
#-------------------------------------------------------
def diff(x):
    xN=[]
    xN.append(x[0])
    for i in range(1,len(x)-1):
        xN.append(((x[i+1] - x[i]*2 + x[i-1] + x[i])/1.2))
    xN.append(x[-1])
    return xN
#-------------------------------------------------------

k=10
for i in range(k):
    F=diff(f)
    f=F
    x = np.linspace(0, 200, 2000)
    plt.plot(x,f)
plt.show()


