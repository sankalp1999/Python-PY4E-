import json
import urllib.request, urllib.parse, urllib.error
import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter location')
if len(address) < 1:
    pass
parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
# opening
uh = urllib.request.urlopen(url, context=ctx)
# decoding because it might be in utf - 8 
data = uh.read().decode()
data2 = json.loads(data)
print(data2["results"][0]["place_id"])
# for i in data2:
    # print(i)
    # print(data2[i][0])