import math
import random
import numpy as np
import matplotlib.pyplot as plt
from pylab import rand,plot,show,norm
from numpy.linalg import inv

#generate data with gaussion noise. E.x. sin(2*pi*x)+gaussian noise.
#n: number of data points.
def generate_data(n):
  data=np.zeros((n,2))
  for i in range(n):
    data[i,0]=random.uniform(0.0,math.pi)
    data[i,1]=math.sin(data[i,0])+ np.random.normal(0.0,.1,1)
  return data;

class Regression:
  def __init__(self,M=1,lamb=.5):
    self.M=M
    self.w=rand(M+1)*2-1
    self.lamb=lamb;

  def y(self,x):
    s=0
    for i in range(self.M+1):
      s+=w[i]*(x**i)
    return s;

  def training(self,data):
    n=data.shape[0]
    X=np.zeros((n,self.M+1))
    for i in range(n):
      for j in range(self.M+1):
        X[i,j]=data[i,0]**j
    XTX_inv=inv((X.T).dot(X) + self.lamb*np.identity(self.M+1))
    XTY=(X.T).dot(data[:,1])
    self.w=XTX_inv.dot(XTY)
    
data=generate_data(20)
Reg=Regression(10,.5);
Reg.training(data)
w=Reg.w;
print w;
print "Data Generated."
plt.plot(data[:,0],data[:,1],'ro')
plt.axis([0, 4, 0, 2])
#plt.show()

x = np.linspace(0, 4, 200)
#y1 = (w[0] + w[1]*x + w[2]*x**2+w[3]*x**3+w[4]*x**4+w[5]*x**5)
y=Reg.y(x)
#plt.figure()
plt.plot(x, y)
plt.show()
