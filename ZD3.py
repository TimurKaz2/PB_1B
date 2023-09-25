import random 
import numpy as np
import matplotlib.pyplot as plt


n=3 #Количество циклов
X=[] 
Y=[]
q=1000 #Количество точек на каждом отрезке

for i in range(n):
    
    x=np.linspace(0, 10, q)
    y=(np.exp(-5+x))/(1+np.exp(-5+x)) #Логарифмический закон. Взято из интернета, возможна замена
    Y.extend(y)
    
   
    y=np.exp(-1/2*x) #Экспоненциальный закон. Подобрал для красоты, требуется замена
    y[0]=Y[-1]  #Убирает пики при переходе  одного графика в другой (Бесило пзд)
    y[1]=Y[-2]
    
    Y.extend(y)

    x=np.linspace(i*10*2, (i+1)*20, 2*q)
    
    X.extend(x)

   


plt.plot(X,Y)
plt.show()


