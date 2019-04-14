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
	if r.find("th",{"scope": "row"}) == True:
			print("Rows = r = ",r)
			currency_name = r.find("th",{"scope": "row"}).text
			print(currency_name)
			
	p = r.find("th").get_text()
	p = p.replace("\r","")
	p = p.replace("\n","")
	#print("Right =",p,type(p))
	
	if (p == "Market Cap"):
		q = r.find_all('span',{'data-currency-value':""})
		print (p , q[1].text)
		#openvalue = q[0]
		#closevalue = q[1]
		#print (openvalue, closevalue)
	elif (p == "24 Hour Volume"):
		q = r.find_all('span',{'data-currency-value':""})
		print (p, q[1].text)

	elif (p == "Yesterday's High / Low"):
		q = r.find_all('span',{'data-currency-value':""})
		high = q[1].text
		low = q[4].text
		print("High =", high, "Low =", low)

	elif (p == "Yesterday's Open / Close"):
		q = r.find_all('span',{'data-currency-value':""})
		openprice = q[1].text
		closevalue = q[4].text
		print("Open price =", openprice, "Close price =", closevalue)





	#if (p == None):
	#print("FFFFFF", p)

