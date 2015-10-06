import math
import random
import numpy as np
import matplotlib.pyplot as plt

#generate data with gaussion noise. E.x. sin(2*pi*x)+gaussian noise.
#n: number of data points.
def generate_data(n):
  data=np.zeros((n,2))
  for i in range(n):
    data[i,0]=random(0.0,math.pi)
    data[i,1]=math.sin(data[i,0])+ numpy.random.normal(0.0,.2,1)
  return data;
  
  data=generate_data(20)
  plt.plot(x[:,0],x[:,1],'ro')
  plt.axis([-1, 4, -1, 2])
  plt.show()
