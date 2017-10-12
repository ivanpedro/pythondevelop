
"""
import os

curdir = os.getcwd()
print(curdir)
"""
#os.mkdir('ivan') 

#os.rename('ivan', 'pedro')

#import time

#time.sleep(2)

#os.rmdir('pedro')

"""
#import sys

#sys.stderr.write('This is stderr text \n')


#sys.stderr.flush()

#sys.stdout.write('This is stdout text \n')

#print (sys.argv)


if len(sys.argv)  > 1 :
    print (float(sys.argv[1]) + 5 )
"""
"""    
def main(arg):
    print(arg)
    
main(sys.argv[1])

"""
import urllib.request
import urllib.parse

#x = urllib.request.urlopen('http://inecsoft.co.uk')


#print(x.read())

"""
url  ='http://inecsoft.co.uk'

values  = {'s': 'basic',
           'submit':'search'
           }

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print (respData)

"""

try:
    x = urllib.request.urlopen('https://www.google.com/search?q = test')

    print(x.read())
    
except Exception as e:
    print (str(e))
    

try:
    url = 'https://www.google.com/search?q=test'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
   
    saveFile.close()
    
except Exception as e:
    print(str(e))
  