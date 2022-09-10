import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

x = np.arange(0.1,1.1,0.1)

y1 = np.array([1]*10) - np.array([0.9992, 0.9965, 0.9934, 0.9903, 0.9844, 0.9767, 0.9668, 0.9563, 0.9477, 0.9386])
y0 = 1 - (1-3*x*10**(-2))**(24)*(25-24*(1-3*x*10**(-2)))
y2 = np.array([1]*10) - np.array([0.9959, 0.9920, 0.9850, 0.9810, 0.9751, 0.9684, 0.9611, 0.9552, 0.9436, 0.9380])
y3 = np.array([1]*10) - np.array([0.9985, 0.9970, 0.9935, 0.9922, 0.9880, 0.9839, 0.9812, 0.9747, 0.9690, 0.9640])

l1, = plt.plot(x,y1,marker='D', color='pink')
l2, = plt.plot(x,y0,marker='8', color='b')
l3, = plt.plot(x,y2,marker='+', color='y')
l4, = plt.plot(x,y3,marker='x', color='g')
plt.yscale('log')
plt.legend(handles = [l1,l2,l3,l4] ,labels = ['DNA-LC','DNA-XL','HEDGES with 1 runout byte','HEDGES with 2 runout bytes'],loc = 'best')
plt.xlabel('$P_s = P_d = P_i(\\times 10^{-2})$',fontsize = 9)
plt.ylabel('Error Rate',fontsize = 9)
plt.savefig('different_1.png', dpi=1000)
plt.show() 
