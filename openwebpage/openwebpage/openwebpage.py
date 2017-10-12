# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:26:10 2017

@author: Ivan
"""
"""
open a webbrowser with a video every 10 sec three time. webbrower is not working
"""

import time
import webbrowser


print ("Tis program started on " + str (time.ctime()))

end= 3
wait = 0

while(wait <end):    
    time.sleep(10)
    webbrowser.open("http://inecsoft.co.uk")
    wait += 1


