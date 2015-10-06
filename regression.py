import math
import random
import numpy as np
import matplotlib.pyplot as plt

#generate data with gaussion noise. E.x. sin(2*pi*x)+gaussian noise.
#n: number of data points.
def generate_data(n):
  data=np.zeros((n,2))
  for i in range(n):
    data[i,0]=random.uniform(0.0,math.pi)
    data[i,1]=math.sin(data[i,0])+ np.random.normal(0.0,.1,1)
  return data;
  
data=generate_data(20)
print "Data Generated."
plt.plot(data[:,0],data[:,1],'ro')
plt.axis([0, 4, 0, 2])
plt.show()
