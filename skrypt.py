# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:30:02 2022

@author: alaja
"""


import numpy
data=numpy.loadtxt(fname="data/inflammation-01.csv", delimiter=",")

import matplotlib.pyplot as plt

maksimum=data.max()
minimum=data.min()
fig=plt.figure()
ax=[]
for i in range(1,4):
    ax.append(fig.add_subplot(1,3,i))
    ax[i-1].set_ylim([minimum, maksimum])
ax[0].plot(data.min(axis=0))
ax[1].plot(data.mean(axis=0))
ax[2].plot(data.max(axis=0))

ax[1].set_yticklabels([])
ax[2].set_yticklabels([])

fig.suptitle("Wykres potrójny")
ax[0].set_title("MIN")
ax[1].set_title("MEAN")
ax[2].set_title("MAX")

ax[0].set_ylabel("Liczba")
ax[1].set_xlabel("Dzień")
plt.show()
