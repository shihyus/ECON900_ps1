import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import urllib.request
import time


def openlink(link):
	#f = open("https://coinmarketcap.com/" + link + ".html","wb")
	link = "https://coinmarketcap.com" + link
	print ("link =", link)
	response = urllib.request.urlopen(link) #encodint="utf-8"
	#print (response.info())
	html = response.read().decode("utf-8")

	html = BeautifulSoup(html, 'html.parser')

	currencies_table = html.find('table', {"class": "cmc-table-striped"})
	#print ("table = ", currencies_table)
	#print ("id = ", currencies_table)
	currencies_tbody = currencies_table.find("tbody")
	#print(currencies_tbody)
	currencies_rows = currencies_tbody.find_all("tr")

	for r in currencies_rows:
		p = r.find("th").get_text()
		p = p.replace("\r","")
		p = p.replace("\n","")
		#print("Right =",p,type(p))

		#if (p == "Market Cap"):
		#	q = r.find_all('span',{'data-currency-value':""})
		#	marketCap = q
			#print (p , q[1].text)
			#openvalue = q[0]
			#closevalue = q[1]
			#print (openvalue, closevalue)
		if (p == "24 Hour Volume"):
			q = r.find_all('span',{'data-currency-value':""})
			#print (p, q[1].text)
			dayVolume = q[1].text

		elif (p == "Yesterday's High / Low"):
			q = r.find_all('span',{'data-currency-value':""})
			high = q[1].text
			low = q[4].text
			#print("High =", high, "Low =", low)

		elif (p == "Yesterday's Open / Close"):
			q = r.find_all('span',{'data-currency-value':""})
			openPrice = q[1].text
			closePrice = q[4].text
			#print("Open price =", openPrice, "Close price =", closePrice)

	time.sleep(10)
	return dayVolume, high, low, openPrice, closePrice


if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

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
		currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		currency_price = r.find("a", {"class": "price"}).text
		#currency_volume = r.find("a", {"class": "volume"}).text
		currency_link = r.find("td", {"class":"currency-name"}).find('a',href = True)['href']
		# print(currency_link)
		#print(currency_link)
		dayVolume, high, low, openPrice, closePrice = openlink(currency_link)
		#newcoin_table
		#coinpage = openlink(currency_link)
		
		#print(currency_name)
		#print(currency_market_cap)
		#print(currency_price)
		#print(currency_volume)
		df = df.append({
			'scrapping_time': scrapping_time, 
			'short_name': currency_short_name,
			'name': currency_name,
			'market_cap': currency_market_cap,
			'price': currency_price,
			'volume': dayVolume,
			#'marketCap' : marketCap,
			#'dayVolume' : dayVolume,
			'high' : high,
			'low' : low,
			'openPrice' : openPrice,
			'closePrice' : closePrice,
			#'supply': currency_supply,
			#'24H_change': currency_change
			}, ignore_index=True)
		print ("length of df =", len(df))
		if len(df) > 3:
			break



df.to_csv("parsed_results/coinmarketcap_dataset.csv")