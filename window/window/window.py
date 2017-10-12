# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:29:27 2017

@author: Ivan
"""

from tkinter import *

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
root =Tk()
app =Window(root)
root.mainloop()
