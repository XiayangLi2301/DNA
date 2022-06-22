import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
plt.style.use('seaborn')
plt.tick_params(axis='both',which='major',labelsize=14)

x = np.array([10,20,30,40,50,60,70,80,90,100])
y = np.array([0.95155,0.95145,0.95405,0.9554,0.95785,0.9603,0.96395,0.9628,0.96655,0.96705])

#设置x轴标签的名称,以及字体的大小
plt.ylabel('Error Correction Rate',fontsize = 9)
#设置y轴标签的名称,以及字体的大小
ax = plt.gca()
x_major_locator = MultipleLocator(10)
y_major_locator = MultipleLocator(2*10**(-2))
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=9)
plt.xlim(5,105)
#设置x轴范围
plt.ylim(0.8,1)
#设置y周范围
plt.bar(x,y,width=4)
plt.hlines(0.95, 6, 104, colors = "grey", linestyles = "dashed")
plt.savefig('Figure_4.png', dpi=1000)
plt.show()
plt.title('varied by length')