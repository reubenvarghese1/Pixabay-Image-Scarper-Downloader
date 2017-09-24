import json
from pprint import pprint
import urllib2
import sys    #Importing the System Library

from urllib2 import Request,urlopen
from urllib2 import URLError, HTTPError
k=0
m=0
with open('data.json') as data_file:    
    data = json.load(data_file)
    for hello in data["hits"]:
    	image=hello
    	lal=hello
    	imageuri=lal["previewURL"]
    	imageuri = imageuri.replace(' ', '')[:-8].upper()
    	temp="_960_720.jpg"
    	imageuri=imageuri+temp
    	imageuri=imageuri.lower()
    	print(imageuri)
    	req = Request(imageuri, headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
    	response = urlopen(req,None,15)
    	k=k+1
    	m=m+1
    	output_file = open(str(k)+".jpg",'wb')
    	data = response.read()
    	output_file.write(data)
    	response.close()
print(len(data["hits"]))
