# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:47:26 2017

@author: Ivan
That code will just output the problem and fixed code to the console. Now, let's actually convert the file!

C:\Python\Python36\Tools\scripts\2to3.py -w python2script.py
"""

import urllib2

try:
    x = urllib2.urlopen("http://pythonprogramming.net").read()
	print x
except Exception, e:
    print str(e)

