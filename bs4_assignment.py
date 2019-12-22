from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
#Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter -")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of the table
tags = soup('a')
# print(tags)
# p =soup.find_all('span')
sum1 = 0
l = []
urls = []
for i in range(7):
	urls = []
	names = []
	for tag in tags:
		urls.append(tag.get('href'))
		names.append(tag.contents[0])
	print(names[17])	
	url = urls[17]
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup('a')

