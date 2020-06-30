import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Please enter the URL")

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

#script to parse XML data
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
sum1 =0
for i in range(len(results)):
    sum1 += int((results[i].find('count').text))
    
print(sum1)