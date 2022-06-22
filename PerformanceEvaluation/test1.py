import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0,0,1,1])
# ypoints = np.array([0,1,0,1])
x1 = np.array([-1,1])
y1 = np.array([0.5,-0.5])
# x2 = np.array([0,1])
# y2 = np.array([0.5,0])
# plt.plot(xpoints,ypoints,'o',x1,y1,'-',x2,y2,'-')
# #'o' 表示生成了4个点,表示一个实心圈标记,这样就可以避免生成一条线。此时在图形上将呈现(0,0),(0,1),(1,0),(1,1)四个点
# plt.show()
xpoints = np.array([0,0,1,1])
ypoints = np.array([0,1,0,1])
x1 = np.linspace(-10,10,500)
y1 = (-0.5) * x1
y2 = (-0.5) * x1 + 4
y3 = (-0.5) * x1 + 1
y4 = (-0.5) * x1 + 1.5
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.plot(xpoints,ypoints,'o',x1,y1,'-.',x1,y2,'-.',x1,y3,'-.',x1,y4,'-.')
plt.show()