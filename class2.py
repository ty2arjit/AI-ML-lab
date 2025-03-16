import numpy as np
import matplotlib.pyplot as plt
x=np.random.rand(5)
y=np.random.rand(5)
max1=0
for i in x:
    max1=max(max1,i)
if i<0.5:
    plt.scatter(x,y,color="red")
else:
    plt.scatter(x,y,color="blue")
plt.show()



