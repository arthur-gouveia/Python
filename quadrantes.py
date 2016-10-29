# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 09:08:02 2016

@author: arthu
"""

import numpy as np
import matplotlib.pylab as plt


def setquadrants(dt):
    data = dt.copy()

    # Identifying limits for the quadrants
    high_quality = data[:, 0] > 85
    high_satisfaction = data[:, 1] > 0.8

    data[(high_quality) & (high_satisfaction), 3] = 1  # Quadrant 1
    data[~(high_quality) & (high_satisfaction), 3] = 2  # Quadrant 2
    data[(high_quality) & ~(high_satisfaction), 3] = 3  # Quadrant 3
    data[~(high_quality) & ~(high_satisfaction), 3] = 4  # Quadrant 4

    return data


def gendata(N=15):
    data = np.vstack((np.random.uniform(0, 100, N),
                      np.random.uniform(0, 1, N),
                      np.random.uniform(100, 3000, N),
                      np.zeros(N)))
    return data.transpose()

data = gendata(10)

data = setquadrants(data)

colors = {1: 'g', 2: 'y', 3: 'r', 4: '#7030A0'}

plt.scatter(data[:, 1], data[:, 0], s=data[:, 2], facecolors='none',
            edgecolor=[colors[i] for i in data[:, 3]])
plt.xlabel('Satisfação')
plt.ylabel('Qualidade')
plt.title('Satisfação x Qualidade x Demanda')
plt.xlim([-0.2, 1.2])
plt.ylim([-20, 120])
plt.xticks(np.linspace(-0.2, 1.2, 8),
           ['-20%', '0%', '20%', '40%', '60%', '80%', '100%', '120%'])
plt.plot((-0.2, 1.2), (85, 85), 'k',
         linewidth=0.5, linestyle='--')  # Horizontal line
plt.plot((0.8, 0.8), (-20, 120), 'k',
         linewidth=0.5, linestyle='--')  # Vertical line
plt.show()
