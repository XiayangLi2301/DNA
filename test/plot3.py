import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from pylab import xticks,yticks,np
from matplotlib import pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
xticks(np.linspace(1,5,5))
yticks(np.linspace(0,1,3))
n = 4
X = np.arange(n)+2
Y1 = [1.000,0.993,0.966,0.897]
Y2 = [0.955,0.9170,0.8420,0.7150]
xticks
plt.xlim(1.55,5.45,2)
l1 = plt.bar(X-0.17,Y1,width = 0.34,facecolor = 'red',edgecolor = 'white')
l2 = plt.bar(X+0.17,Y2,width = 0.34,facecolor = 'blue',edgecolor = 'white')
plt.legend(handles = [l1,l2] ,labels = ['DNA-LC','HEDGES'],loc = 'best')
plt.title('inconsecutive deletions')
for x,y in zip(X-0.46,Y1):
  plt.text(x+0.3, y+0.02, '%.3f' % y, ha='center', va= 'bottom')
  
for x,y in zip(X-0.43,Y2):
  plt.text(x+0.6, y+0.02, '%.3f' % y, ha='center', va= 'bottom')
plt.ylim(0,+2)
plt.ylabel('Probability of success')
plt.savefig('deletions.png',dpi=1000)


plt.subplot(2, 1, 2)
xticks(np.linspace(1,5,5))
yticks(np.linspace(0,1,3))
Y3 = [0.971,0.904,0.773,0.589]
Y4 = [0.966,0.923,0.840,0.740]
xticks
plt.xlim(1.55,5.45,2)
l1 = plt.bar(X-0.17,Y3,width = 0.34,facecolor = 'red',edgecolor = 'white')
l2 = plt.bar(X+0.17,Y4,width = 0.34,facecolor = 'blue',edgecolor = 'white')
plt.legend(handles = [l1,l2] ,labels = ['DNA-LC','HEDGES'],loc = 'best')
plt.title('deletions')
for x,y in zip(X-0.46,Y3):
  plt.text(x+0.3, y+0.02, '%.3f' % y, ha='center', va= 'bottom')
  
for x,y in zip(X-0.43,Y4):
  plt.text(x+0.6, y+0.02, '%.3f' % y, ha='center', va= 'bottom')
plt.ylim(0,+2)
plt.ylabel('Probability of success')
plt.savefig('deletions.png',dpi=1000)
plt.show()