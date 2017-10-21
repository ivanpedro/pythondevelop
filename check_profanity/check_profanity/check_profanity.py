

import os
import urllib.request
import urllib
import requests


#os.chdir(r"C:\Users\Ivan\Documents\Phyton")
#movie_file is in the same folder. if it is not add the location in open('address')

def manage_file():
    
   quotes =open("movie_file.txt")
   content_of_file = quotes.read()
   print(content_of_file)
   quotes.close()
   check_profinity(content_of_file)

def check_profinity(text_to_check):
    url = "http://www.wdylike.appspot.com/?q="
    connection =  requests.get(url + text_to_check)
        
    output = str(connection.read())
    print(output)
    connection.close()

    if "true" in output:
        print("Profinity Alert ")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("It could not scan the document properly")

manage_file()