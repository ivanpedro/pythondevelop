# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:13:05 2017

@author: Ivan

Bessel function of first kind
special.jv(nu,z) or special jn(nu,z)
"""

from scipy import special
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from pylab import *

"""
working example of bessel first funsion

k = np.r_[0:1.2:.2]
k= np.linspace(0,1,6)

kth_zero = special.jv(1 , k)

print(kth_zero)
"""


#k.real
#k.imag

X = np.r_[0:20:0.1]
J = np.zeros((5,200))

for i in range(0,4):
    J[i+1, :] = special.jv(i,X)
    
#graphics

fig , axes =  plt.subplots( figsize=(12, 6))

#axes = fig.add_axes([0, 0, 1, 1]) # left, bottom, width, height (range 0 to 1)

axes.plot(X, special.jv(0,X), label = 'J_0', linewidth=1.5)
axes.plot(X, special.jv(1,X), label = 'J_1', linewidth=1.5)
axes.plot(X, special.jv(2,X), label = 'J_2', linewidth=1.5)
axes.plot(X, special.jv(3,X), label = 'J_3', linewidth=1.5)
axes.plot(X, special.jv(4,X), label = 'J_4', linewidth=1.5)

axes.set_ylim([-0.5, 1])
axes.set_xlim([0, 20])

axes.set_xlabel('X', fontsize=18)
axes.set_ylabel('Jv(X)', fontsize=18)

axes.legend(loc=0) 

axes.set_title('Bessel Funtion of the Fisrt Kind for v = 0,1,2,3,4,5', fontsize=20)
plt.grid()
plt.show()
 
"""

fig, ax = subplots()

ax.plot(x, x**2, 'b', label="y = x**2")
ax.plot(x, x**3, 'r', label="y = x**3")
ax.plot(x, 4 *x**2 + 6*x, 'y' ,label = " 4 *x**2 + 6x")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Title')
ax.legend(loc=2); # upper left corner

"""

"""
Bessel Functions
    ----------------
    
    .. autosummary::
       :toctree: generated/
    
       jv       -- Bessel function of the first kind of real order and complex argument.
       jn       -- Bessel function of the first kind of real order and complex argument
       jve      -- Exponentially scaled Bessel function of order `v`.
       yn       -- Bessel function of the second kind of integer order and real argument.
       yv       -- Bessel function of the second kind of real order and complex argument.
       yve      -- Exponentially scaled Bessel function of the second kind of real order.
       kn       -- Modified Bessel function of the second kind of integer order `n`
       kv       -- Modified Bessel function of the second kind of real order `v`
       kve      -- Exponentially scaled modified Bessel function of the second kind.
       iv       -- Modified Bessel function of the first kind of real order.
       ive      -- Exponentially scaled modified Bessel function of the first kind
       hankel1  -- Hankel function of the first kind
       hankel1e -- Exponentially scaled Hankel function of the first kind
       hankel2  -- Hankel function of the second kind
       hankel2e -- Exponentially scaled Hankel function of the second kind
    
    The following is not an universal function:
    
    .. autosummary::
       :toctree: generated/
    
       lmbda -- [+]Jahnke-Emden Lambda function, Lambdav(x).
    
    Zeros of Bessel Functions
    ^^^^^^^^^^^^^^^^^^^^^^^^^
    
    These are not universal functions:
    
    .. autosummary::
       :toctree: generated/
    
       jnjnp_zeros -- [+]Compute zeros of integer-order Bessel functions Jn and Jn'.
       jnyn_zeros  -- [+]Compute nt zeros of Bessel functions Jn(x), Jn'(x), Yn(x), and Yn'(x).
       jn_zeros    -- [+]Compute zeros of integer-order Bessel function Jn(x).
       jnp_zeros   -- [+]Compute zeros of integer-order Bessel function derivative Jn'(x).
       yn_zeros    -- [+]Compute zeros of integer-order Bessel function Yn(x).
       ynp_zeros   -- [+]Compute zeros of integer-order Bessel function derivative Yn'(x).
       y0_zeros    -- [+]Compute nt zeros of Bessel function Y0(z), and derivative at each zero.
       y1_zeros    -- [+]Compute nt zeros of Bessel function Y1(z), and derivative at each zero.
       y1p_zeros   -- [+]Compute nt zeros of Bessel derivative Y1'(z), and value at each zero.
    
    Faster versions of common Bessel Functions
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    .. autosummary::
       :toctree: generated/
    
       j0  -- Bessel function of the first kind of order 0.
       j1  -- Bessel function of the first kind of order 1.
       y0  -- Bessel function of the second kind of order 0.
       y1  -- Bessel function of the second kind of order 1.
       i0  -- Modified Bessel function of order 0.
       i0e -- Exponentially scaled modified Bessel function of order 0.
       i1  -- Modified Bessel function of order 1.
       i1e -- Exponentially scaled modified Bessel function of order 1.
       k0  -- Modified Bessel function of the second kind of order 0, :math:`K_0`.
       k0e -- Exponentially scaled modified Bessel function K of order 0
       k1  -- Modified Bessel function of the second kind of order 1, :math:`K_1(x)`.
       k1e -- Exponentially scaled modified Bessel function K of order 1
    
    Integrals of Bessel Functions
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    .. autosummary::
       :toctree: generated/
    
       itj0y0     -- Integrals of Bessel functions of order 0
       it2j0y0    -- Integrals related to Bessel functions of order 0
       iti0k0     -- Integrals of modified Bessel functions of order 0
       it2i0k0    -- Integrals related to modified Bessel functions of order 0
       besselpoly -- [+]Weighted integral of a Bessel function.
    
    Derivatives of Bessel Functions
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    .. autosummary::
       :toctree: generated/
    
       jvp  -- Compute nth derivative of Bessel function Jv(z) with respect to `z`.
       yvp  -- Compute nth derivative of Bessel function Yv(z) with respect to `z`.
       kvp  -- Compute nth derivative of real-order modified Bessel function Kv(z)
       ivp  -- Compute nth derivative of modified Bessel function Iv(z) with respect to `z`.
       h1vp -- Compute nth derivative of Hankel function H1v(z) with respect to `z`.
       h2vp -- Compute nth derivative of Hankel function H2v(z) with respect to `z`.
    
    Spherical Bessel Functions
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    .. autosummary::
       :toctree: generated/
    
       spherical_jn -- Spherical Bessel function of the first kind or its derivative.
       spherical_yn -- Spherical Bessel function of the second kind or its derivative.
       spherical_in -- Modified spherical Bessel function of the first kind or its derivative.
       spherical_kn -- Modified spherical Bessel function of the second kind or its derivative.
    
    Riccati-Bessel Functions
    ^^^^^^^^^^^^^^^^^^^^^^^^
    
    These are not universal functions:
    
    .. autosummary::
       :toctree: generated/
    
       riccati_jn -- [+]Compute Ricatti-Bessel function of the first kind and its derivative.
       riccati_yn -- [+]Compute Ricatti-Bessel function of the second kind and its derivative.
    
"""
