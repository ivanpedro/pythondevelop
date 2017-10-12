# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:33:08 2017

@author: Ivan
"""

import string
import os


def rename_files():
     #(get file's names from a given folder)
    listfiles =os.listdir(r"C:\Users\Ivan\Documents\Phyton\prank")
    
    #rename files step
    #change directory
    os.chdir(r"C:\Users\Ivan\Documents\Phyton\prank")
    print(os.getcwd())
    
    for name in listfiles: 
        
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        #filename.translate(translation_table)
        
        print("Old name: " + name)
        print("New name: " + name.translate(translation_table))
        
        os.rename(name, name.translate(translation_table))
            #x= str.maketrans("", i)
            #os.rename(name, name.translate(x))
   
        
rename_files()
