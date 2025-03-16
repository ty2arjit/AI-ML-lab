import matplotlib.pyplot as plp
import numpy as np
import pandas as pan
x=[]
for i in range(51):
    temp=np.random.randint(50)
    x.append(temp)
y=[]
for i in range(51):
    temp=np.random.randint(50)
    y.append(temp)
for i in range(51):
    print((x[i]+y[i])/2)
plp.scatter(x,y,color="red")
plp.legend("x")
plp.show()
