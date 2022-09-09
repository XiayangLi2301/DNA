import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

x = np.arange(10,151,10)

y1 = np.array([1]*15) - np.array([0.9982, 0.9956, 0.9898, 0.9843, 0.9755, 0.9666, 0.9540, 0.9417, 0.9284, 0.9123,0.8927,0.8814,0.8605,0.8401,0.8236])
y0 = 1-(1-3*5*10**(-3))**(x)

l1, = plt.plot(x,y1,marker='D', color='pink')
l2, = plt.plot(x,y0,marker='8', color='b')
plt.yscale('log')
plt.legend(handles = [l1,l2] ,labels = ['DNA-LC','Uncoded'],loc = 'best')
plt.xlabel('The length of DNA squence',fontsize = 9)
#设置x轴标签的名称,以及字体的大小
plt.ylabel('Error Rate',fontsize = 9)
plt.savefig('len_var.png', dpi=1000)
plt.show() 