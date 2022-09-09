import matplotlib.pyplot as plt
import numpy as np
X = [-0.14,-0.127,-0.12,-0.11,-0.10,-0.09,-0.08,-0.07,-0.06,-0.05,-0.04]
Y1 = [1-0.9524, 1-0.9579, 1-0.9653, 1-0.9725, 1-0.9751, 1-0.9813, 1-0.9847, 1-0.9880, 1-0.9890, 1-0.9903, 1-0.9903]
Y2 = [21.314, 21.771, 22.004, 22.846, 23.569, 26.131, 30.244, 40.870, 57.226, 103.748, 134.145]
fig, ax1 = plt.subplots()
p1 = ax1.plot(X,Y2,color='r',marker = '+', label = 'Time Cost')
ax1.set_ylim((10,500))
ax1.tick_params(axis='y',colors='r')
ax1.set_ylabel('Time Cost',color = 'r')
ax1.set_xlabel('$p_{ok}$')
plt.yscale('log')
plt.axvline(-0.07,c='grey',ls='--')
ax2 = ax1.twinx()
p2 = ax2.plot(X,Y1,color='b',marker='D',label = 'Error Rate')
ax2.set_ylim((0.005,0.1))
ax2.tick_params(axis='y',colors='b')
ax2.set_ylabel('Error Rate',color = 'b')
# fig.legend(loc='upper right',bbox_to_anchor=(1,1),bbox_transform=ax1.transAxes)
lines = p1 + p2
labels = [line.get_label() for line in lines]
plt.legend(lines, labels)
plt.yscale('log')
plt.savefig('tune_p_ok', dpi=1000)