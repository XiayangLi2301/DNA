import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
plt.tick_params(axis='both',which='major',labelsize=14)
x = np.linspace(1,10,2000)
#从1到10随机产生200个值
y2 = 1 - (1-3*x*10**(-3))**(15)*(16-15*(1-3*x*10**(-3)))
x3 = []
for i in range(10):
    x3.append((i+1))
x3 = np.array(x3)
y3 = [0.000375,0.00111,0.001708333,0.004593333,0.006450641,0.010508416,0.011867654,0.016778053,0.02043009,0.025957798]
def f_fit(x,y_fit):
    a,b,c=y_fit.tolist()
    return a*x**2+b*x+c
y_fit=np.polyfit(x3,y3,2)
y4 = f_fit(x3,y_fit)
#plt.tick_params 参数及其用法
#axis 参数axis的值为'x','y','both',分别代表设置x轴,y轴或同时设置,默认值为both
#which 的值为'major','minor','both',分别代表设置主刻度线,副刻度线,或同时设置
#direction 的值为'in','out','inout',分别代表刻度线显示在内测,外侧,或·同时显示.
#labelsize 设置为标签的大小
plt.xlabel('$P_s = P_d = P_i(\\times 10^{-3})$',fontsize = 9)
#设置x轴标签的名称,以及字体的大小
plt.ylabel('Block Error Rate',fontsize = 9)
#设置y轴标签的名称,以及字体的大小
ax = plt.gca()
x_major_locator = MultipleLocator(1)
y_major_locator = MultipleLocator(2*10**(-2))
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=9)
plt.xlim(1,10)
#设置x轴范围
plt.ylim(0,0.5)
#设置y周范围
l2, = plt.plot(x,y2)
l3, = plt.plot(x3,y4)
plt.legend(handles = [l2,l3] ,labels = ['DNA-XL','DNA-LC'],loc = 'best')
plt.title('message = 18 bits')
# 'best'：自动选择最佳位置。

# 'upper right'：将图例放在右上角。

# 'upper left'：将图例放在左上角。

# 'lower left'：将图例放在左下角。

# 'lower right'：将图例放在右下角。

# 'right'：将图例放在右边。

# 'center left'：将图例放在左边居中的位置。

# 'center right'：将图例放在右边居中的位置。

# 'lower center'：将图例放在底部居中的位置。

# 'upper center'：将图例放在顶部居中的位置。

# 'center'：将图例放在中心
plt.grid()
plt.show()