
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:23:48 2017

@author: Ivan
3D 
"""


#from mpl_toolkits.mplot3d.axes3d import Axes3D
from pylab import *
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from math import pi
from matplotlib import cm



X = np.linspace(0,10,6)
Y = X**3
Z = 2

fig = plt.figure(figsize=(4,4))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*pi, cmap=cm.coolwarm)

ax.set_xlim3d(-pi, 2*pi);
ax.set_ylim3d(0, 3*pi);
ax.set_zlim3d(-pi, 2*pi);


#plot

