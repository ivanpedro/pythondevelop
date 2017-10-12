# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:23:05 2017

@author: Ivan
"""
 #speed 250 m/s
 #angle = 65 degrees
 #win_speed = 65
 
from math import sin, cos, pi
from pylab import *
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

angle = 65
#win_speed = 30

#inicial position
x0, y0 , z0 = 3000 , 0 , 0
v0 = 250
g = 9.81
vx = -30


v0y = v0 *cos (angle*pi/180)
v0z = v0 * sin (angle*pi/180)
t = v0z/g

"""
vz = v0z - g*t
z = z0 + v0z *t - 1/2* g* t**2

x = x0 + vx * t
y = y0 + v0y * t

"""

#plot

tplot= np.linspace (0,t,100)

z = z0 + v0z * tplot -0.5* g * tplot**2
y = y0 + v0y * tplot
x = x0 + vx * tplot

xnowind = np.linspace(1, len(y)) 

fig = plt.figure()
ax = Axes3D(fig)

ax.set_title('3D Projectil')

ax.set_xlim3d(6000, 0)
ax.set_ylim3d(0, 8000)
ax.set_zlim3d(0, 3000)

plt.xticks(np.arange(0,7000,1000 ), [str (i)+'k' for i in range(7)])
plt.yticks(np.arange(0,9000,1000 ), [str (i)+'k' for i in range(9)])
#plt.zticks(np.arange(0,3000,1000 ), [str (i)+'k' for i in range(4)])

ax.plot3D(x,y,z)
#ax.plot3D(xnowind,y,z)
ax.set_xlabel('X(m)')
ax.set_ylabel('Y(m)')
ax.set_zlabel('Z(m)')
#ax.legend(loc=0)
plt.show()






