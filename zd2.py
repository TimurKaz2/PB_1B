import random 
import numpy as np
import matplotlib.pyplot as plt


n=0
b=[]
l=int(input('L - '))
sum=0
Xx=0
Yy=0
while sum<l:
    a=random.randint(0,10)
    n=n+1
    if sum+a>l:
        a=l-sum
    sum=sum+a
    b.append(a)
    Alfa=random.randint(1,89)
    R=random.randint(0,3)
    Q=Alfa*3.1413/180
    X=np.cos(Q)*a
    Y=np.sin(Q)*a
    if R==0:
        Xx=Xx+X
        Yy=Yy+Y
    if R==1:
        Xx=Xx-X
        Yy=Yy+Y
    if R==2:
        Xx=Xx-X
        Yy=Yy-Y
    if R==3:
        Xx=Xx+X
        Yy=Yy-Y
    plt.plot(Xx, Yy,'ro')

    print(sum/l*100,'%')
    
    

plt.grid(True)
#print(b)
#print(n)
plt.show()




