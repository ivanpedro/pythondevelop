# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:03:00 2017

@author: Ivan
writting to a CSV fie
"""
import csv
import pandas as pd


#variable
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco',
         'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)

#==============================================================================
#forename = input("Enter Forename: ")
#surname = input("Enter surname: ")
#score1 = input ("Score 1: ")
#score2 = input ("Score 2: ")
#score3 = input ("Score 3: ")
#==============================================================================

#with open('car.csv', 'r') as file:
#    readfile = csv.reader(file)
#    filelist = []
#    
#    for row in file:
#        if len(row) != 0:
#            filelist += [row]
#            
#    file.close()
    
    
with open('car.csv', 'w') as file:
    fileWrite = csv.writer(file)
    #write the each list in a column in firt row
    #fileWrite.writerow([names, dr,cpc])
    fileWrite.writerow(list(dict.keys()))
    
    for i in range (len(names)):
        #you need a list
        fileWrite.writerow([names[i],dr[i],cpc[i]])
#        fileWrite.writerow([dict.get('country')[i],
#                            dict.get('drives_right')[i],
#                            dict.get('cars_per_cap')[i]])
    
    file.close()
    
#with open('car.csv', 'a') as file:
#    fileWrite = csv.writer(file)
#    #write the each list in a column in firt row
#    
#    fileWrite.writerow([forename,surname,score1,score2,score3])
#    
#    
#    
#    file.close()
