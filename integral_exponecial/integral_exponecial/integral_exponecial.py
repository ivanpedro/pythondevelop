# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
sumatoria desde -1 hasta 1 de a *e( **-(x -b)**2 /c) dx
"""

import numpy as np
from scipy import integrate 
from scipy.integrate import quad

inf0 = -1
inf1 = 1
a,b,c = 1,2,3

def f (x,a,b,c):    
    return a * np.exp(-((x-b)/c)**2)

val , err = np.integrate.quad(f, inf0, inf1 , args =(a,b,c))
