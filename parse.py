import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import urllib.request
import time



def openlink(link):
	#f = open("https://coinmarketcap.com/" + link + ".html","wb")
	link = "https://coinmarketcap.com" + link
	#ink = "https://coinmarketcap.com/currencies/ofcoin/"
	#link = "https://coinmarketcap.com/currencies/aencoin/"
	print ("link =", link)
	response = urllib.request.urlopen(link) #encodint="utf-8"
	#print (response.info())
	html = response.read().decode("utf-8")
	html = BeautifulSoup(html, 'html.parser')

	dayVolume = "None"
	price = "None"
	marketCap = "None"
	high = "None" 
	low = "None" 
	openPrice = "None"
	closePrice = "None"

	price_find = html.find('span', {"id": "quote_price"})
	price = price_find.find('span', {"class": "text-semi-bold"}).text
	#print(price)

	currencies_table = html.find('table', {"class": "cmc-table-striped"})
	currencies_tbody = currencies_table.find("tbody")
	currencies_rows = currencies_tbody.find_all("tr")

	for r in currencies_rows:
		p = r.find("th").get_text()
		p = p.replace("\r","")
		p = p.replace("\n","")
		p = p.replace(" ","")
		#print("Right =",p,type(p))

		#if (p == "Market Cap"):
			#q = r.find_all('span',{'data-currency-value':""})par
			#marketCap = q[1].text
			#print (p , q[1].text)
			#openvalue = q[0]
			#closevalue = q[1]
			#print (openvalue, closevalue)
		if (p == "24HourVolume"):
			if (r.find_all('span',{'data-currency-value':""} )):
				#print (type(q[0]))
				q = r.find_all('span',{'data-currency-value':""} )
				#print (p, q[1].text)
				dayVolume = q[1].text
			else:
				dayVolume = "None"

		# elif (p == blank+"Price"):
		# 	q = r.find_all('span',{'data-currency-value':""})
		# 	price = q[1].text

		elif (p == "MarketCap"):
			if (r.find_all('span',{'data-currency-value':""} )):
				q = r.find_all('span',{'data-currency-value':""})
				#print (p, q[1].text)
				marketCap = q[1].text
			else:
				marketCap = "None"

		elif (p == "Yesterday'sHigh/Low"):
			if (r.find_all('span',{'data-currency-value':""})):
				q = r.find_all('span',{'data-currency-value':""})
				#print (p, q[1].text)
				#print (p, q[4].text)
				high = q[1].text
				low = q[4].text
			else:
				high = "None"
				low = "None"

		elif (p == "Yesterday'sOpen/Close"):
			if (r.find_all('span',{'data-currency-value':""})):
				q = r.find_all('span',{'data-currency-value':""})
				#print (p, q[1].text)
				#print (p, q[4].text)
				openPrice = q[1].text
				closePrice = q[4].text
			else:
				openPrice = "None"
				closePrice = "None"
			#print("Open price =", openPrice, "Close price =", closePrice)
	l = [dayVolume, price, marketCap, high, low, openPrice, closePrice]
	#print ("l = ", l)
	time.sleep(7.2)
	#print(dayVolume, price, marketCap, high, low, openPrice, closePrice)
	#for i in l:
		#if (i == "None"):
			#print ("error result = ", l, currencies_rows)
	return dayVolume, price, marketCap, high, low, openPrice, closePrice


if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

#df = pd.DataFrame({})

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name,"r", encoding ="utf8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()

	currencies_table = soup.find("table", {"id": "currencies-all"})
	#print ("id = ", currencies_table)
	currencies_tbody = currencies_table.find("tbody")
	#print(currencies_tbody)
	currencies_rows = currencies_tbody.find_all("tr")

	for r in currencies_rows:
		currency_short_name = r.find("td", {"class": "currency-name"}).find("span", {"class": "currency-symbol"}).find("a").text
		#print(currency_short_name)
		currency_name = r.find("td", {"class":"currency-name"}).find("a",{"class":"currency-name-container"}).text
		# blank = currency_name.replace(" ","")
		# print (blank)
		#currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		#currency_price = r.find("a", {"class": "price"}).text
		#currency_volume = r.find("a", {"class": "volume"}).text
		currency_link = r.find("td", {"class":"currency-name"}).find('a',href = True)['href']
		# print(currency_link)
		#print(currency_link)
		#if (currency_link == "/currencies/ofcoin/"):
		dayVolume, price, marketCap, high, low, openPrice, closePrice = openlink(currency_link)

		df = pd.DataFrame({
			'Scrapping_time': scrapping_time, 
			'Short_name': currency_short_name,
			'Name': currency_name,
			'Market_cap': marketCap,
			'Price': price,
			'Volume': dayVolume,
			#'marketCap' : marketCap,
			#'dayVolume' : dayVolume,
			'High' : high,
			'Low' : low,
			'OpenPrice' : openPrice,
			'ClosePrice' : closePrice},index=[0])

		#df = df.update(dfnew)
		print (df)
		with open('parsed_results/coinmarketcap_dataset.csv', 'a') as f:
			df.to_csv(f,header=f.tell()==0)
		#df.to_csv("parsed_results/coinmarketcap_dataset.csv", header=f.tell()==0, index = True)

		#newcoin_table
		#coinpage = openlink(currency_link)
		
		#print(currency_name)
		#print(currency_market_cap)
		#print(currency_price)
		#print(currency_volume)
		
		# #print ("length of df =", len(df))
		# if len(df) > 10:
		# 	break



#df.to_csv("parsed_results/coinmarketcap_dataset.csv", header=f.tell()==0)