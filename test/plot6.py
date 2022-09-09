import matplotlib.pyplot as plt
import numpy as np
 
fig = plt.figure()
 
x = np.arange(10,51,10)

y1 = [1,1.33,1.74,2.29,3.00]
y0 = [7.28,16.95,31.07,63.38,126.27]
 
 
left, bottom, width, height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
l1, = ax1.plot(x,y1,marker='D',color='pink')
l2, = ax1.plot(x,y0,marker='8', color='b')
ax1.legend(handles = [l1,l2] ,labels = ['DNA-LC','HEDGES'],loc = 'best')
ax1.set_xlim(5,55,10)
ax1.set_ylabel("time cost")
 
left, bottom, width, height = 0.4,0.6,0.25,0.25
plt.axes([left,bottom,width,height])
plt.xlim(5,55,10)
plt.yscale('log')
l1, = plt.plot(x,y1,marker='D', color='pink')
l2, = plt.plot(x,y0,marker='8', color='b')
plt.savefig('time_cost.png', dpi=1000)
plt.show()