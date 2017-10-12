# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:49:57 2017

@author: Ivan
"""

from pylab import *
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 20)
y = x ** 2

#grafic object
"""
#example 1
fig = plt.figure()

axes = fig.add_axes([0, 0, 1, 1]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Title')
show()

"""
"""
#example 2
fig, axes = plt.subplots()

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

"""
"""
#example 3

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
   
    ax.plot(x, y, 'b', )
    ax.legend(["curve1", "curve2"])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title');
    
"""

"""

#Example 4

#fig = plt.figure()
#ax = fig.add_axes([0, 0, 1, 1])
#or 
fig , ax = plt.subplots()

ax.plot(x, x**2, 'b', label="y = x**2",linewidth=1)
ax.plot(x, x**3, 'r', label="y = x**3",linewidth=0.80)
ax.plot(x, 4 *x**2 + 6*x +2, 'g' , label = "y = 4 *x**2 + 6*x +2" , linewidth=0.45)
ax.set_xlabel('x',fontsize=18)
ax.set_ylabel('y' ,fontsize=18)
ax.set_title('Title')
ax.legend(loc=2); # upper left corner
"""

"""

#Example 5
fig, ax = subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.set_xlabel(r'$\alpha$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.set_title('title')
ax.legend(loc=2); # upper left corner

"""

#Example 6 plot range
fig, axes = plt.subplots(2, 2, figsize=(12, 7))

axes[0,0].plot(x, x**2, x, x**3)
axes[0,0].set_title("default axes ranges")

axes[0,1].plot(x, x**2, x, x**3)
axes[0,1].axis('tight')
axes[0,1].set_title("tight axes")

axes[1,0].plot(x, x**2, x, x**3)
axes[1,0].set_ylim([0, 60])
axes[1,0].set_xlim([2, 5])
axes[1,0].set_title("custom axes range");

axes[1,1].plot(x, x**2, x, x**3)
axes[1,1].set_ylim([0, 80])
axes[1,1].set_xlim([0, 8])
axes[1,1].set_title("custom axes range");

