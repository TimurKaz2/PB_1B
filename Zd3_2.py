import random 
import numpy as np
import matplotlib.pyplot as plt


n=3 
X=[] 
Y=[]
q=1000 

for i in range(n):
    
    x=np.linspace(0, 10, q)
    y=(np.exp(-5+x))/(1+np.exp(-5+x)) 
    Y.extend(y)
    
   
    y=np.exp(-1/2*x) 
    y[0]=Y[-1] 
    y[1]=Y[-2]
    
    Y.extend(y)

    x=np.linspace(i*10*2, (i+1)*20, 2*q)
    
    X.extend(x)

#plt.plot(X,Y)
#plt.show()

K=0.854
R=0.07
l = 133*0.001

Vyzkost = 0.5
pi=3.14

x0=(8*Vyzkost*l)/(pi*R**4)

Pcict=np.exp([x/(K*x0) for x in Y])

Qcict=Pcict/x0


#plt.plot(X,Qcict)
#plt.show()


from scipy import integrate
Q=(1/x0)*(integrate.simpson(Pcict, X))
print(Q)

