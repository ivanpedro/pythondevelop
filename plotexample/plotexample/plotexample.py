
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:22:03 2017

@author: Ivan
"""


from pylab import *
import numpy as np
from numpy import *

x = linspace(0, 10, 10)
y = x ** 2

"""
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

"""

subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-')
show()