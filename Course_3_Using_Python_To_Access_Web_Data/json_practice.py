import json
import urllib.request

url = input("Please enter the url.")
fhand = urllib.request.urlopen(url)
data = fhand.read().decode()
info = json.loads(data)
sum1 = 0
for i in info["comments"] :
    sum1 += i["count"]
print(sum1)