import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import urllib.request

one_file_name = "test1.htm"
#print("parsing: " + one_file_name)

f = open(one_file_name,"r", encoding ="utf8")

soup = BeautifulSoup(f.read(), 'html.parser')
currencies_table = soup.find('table', {"class": "cmc-table-striped"})
#print ("table = ", currencies_table)
	#print ("id = ", currencies_table)

currencies_tbody = currencies_table.find("tbody")
	#print(currencies_tbody)
currencies_rows = currencies_tbody.find_all("tr")

for r in currencies_rows:
	#if r.find("th") == None:
	#	p = r.find("th")
	#	print("FFFFFF", p)
	p = r.find("th").get_text()
	p = p.replace("\r","")
	p = p.replace("\n","")
	#print("Right =",p,type(p))
	
	if (p == "Market Cap"):
		print (p)
		#q = findall('span',data-usd = True)['data-usd']
		#print ("q = ", q)
		#openvalue = q[0]
		#closevalue = q[1]
		#print (openvalue, closevalue)
	elif (p == "24 Hour Volume"):
		print (p)

	elif (p == "Yesterday's High / Low"):
		print (p)

	elif (p == "Yesterday's Open / Close"):
		print (p)




	#if (p == None):
	#print("FFFFFF", p)

