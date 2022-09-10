import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

x = np.arange(0.1,1.1,0.1)

y1 = np.array([1]*10) - np.array([0.9995, 0.9994, 0.9989, 0.9982, 0.9972, 0.9961, 0.9953, 0.9933, 0.9911, 0.9881])
y0 = 1 - (1-2*x*10**(-2))**(24)*(25-24*(1-2*x*10**(-2)))
y2 = np.array([1]*10) - np.array([0.9984, 0.9944, 0.9910, 0.9865, 0.9816, 0.9800, 0.9759, 0.9713, 0.9665, 0.9602])
y3 = np.array([1]*10) - np.array([0.9994, 0.9979, 0.9961, 0.9946, 0.9925, 0.9903, 0.9879, 0.9852, 0.9827, 0.9787])

l1, = plt.plot(x,y1,marker='D', color='pink')
l2, = plt.plot(x,y0,marker='8', color='b')
l3, = plt.plot(x,y2,marker='+', color='y')
l4, = plt.plot(x,y3,marker='x', color='g')
plt.yscale('log')
plt.legend(handles = [l1,l2,l3,l4] ,labels = ['DNA-LC','DNA-XL','HEDGES with 1 runout byte','HEDGES with 2 runout bytes'],loc = 'best')
plt.xlabel('$P_s = 0, P_d = P_i(\\times 10^{-2})$',fontsize = 9)
plt.ylabel('Error Rate',fontsize = 9)
plt.savefig('different_2.png', dpi=1000)
plt.show() 