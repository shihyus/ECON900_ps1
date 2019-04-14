import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
import urllib.request

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()


def openlink(link):
	#f = open("https://coinmarketcap.com/" + link + ".html","wb")
	#link = "https://coinmarketcap.com/" + link
	response = urllib.request.urlopen("https://coinmarketcap.com/" + link) #encodint="utf-8"
	html = response.read()
	html = html.decode("utf-8")
	html = BeautifulSoup(html, 'html.parser')
	currencies_table = soup.find("table")
	#print ("table = ", currencies_table)
	#print ("id = ", currencies_table)
	currencies_tbody = currencies_table.find("tbody")
	#print(currencies_tbody)
	currencies_rows = currencies_tbody.find_all("tr")

	for r in currencies_rows:
		
		if r.find("th",{"scope": "row"}) == True:
			print("Rows = r = ",r)
			currency_name = r.find("th",{"scope": "row"}).text
			print(currency_name)
		
		
	#f.write(html) 
	#f.close()
	#return html

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
		currency_volume = r.find("a", {"class": "volume"}).text
		currency_link = r.find("td", {"class":"currency-name"}).find('a',href = True)['href']
		# print(currency_link)
		#print(currency_link)
		newcoin = openlink(currency_link)
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
			'volume': currency_volume,
			#'supply': currency_supply,
			#'24H_change': currency_change
			}, ignore_index=True)




df.to_csv("parsed_results/coinmarketcap_dataset.csv")