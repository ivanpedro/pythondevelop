

import os
import urllib.request
import urllib
import urllib.parse




#os.chdir(r"C:\Users\Ivan\Documents\Phyton")
#movie_file is in the same folder. if it is not add the location in open('address')

def manage_file():
    
   quotes =open("movie_file.txt")
   content_of_file = quotes.read()
   #print(content_of_file)
   quotes.close()
   content_of_file = content_of_file.split()
   for i in content_of_file:
       check_profinity(str(i))


def check_profinity(text_to_check):

    url = "http://www.wdylike.appspot.com/?q=" + text_to_check
    #encode your data to be process by the  search engine
    values = {'q' : text_to_check}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    # get around the security 
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    #values = {'q' : text_to_check}
    #data = urllib.parse.urlencode(values)
    #data = data.encode('utf-8') # data should be bytes
    #req = urllib.request.Request(url, data)
    #resp = urllib.request.urlopen(req)
    #respData = resp.read()
    #connection =  urllib.request.urlopen(url + text_to_check)
        
    output = str(respData)
    #print(output)
    #connection.close()
    resp.close()

    if "true" in output:
        print("Profinity Alert ")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("It could not scan the document properly")



try:
    manage_file()

except Exception as e:
    print(str(e))