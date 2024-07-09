# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
counter = 0

def retrieve_tag():
    global url
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser') 
    tags = soup('a')
    tags_list = list()

    for tag in tags:
        tag = tag.get('href', None)
        tags_list.append(tag)
        
    url = (tags_list[position - 1])
    
while counter <= count:
    print('Retrieving:', url)
    retrieve_tag()
    counter += 1

