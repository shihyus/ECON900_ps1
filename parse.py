import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name,"r", encoding ="utf8")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()

	currencies_table = soup.find("table", {"id": "currencies"})
	currencies_tbody = currencies_table.find("tbody")
	currencies_rows = currencies_tbody.find_all("tr")

	for r in currencies_rows:
		currency_short_name = r.find("td", {"class": "currency-name"}).find("span", {"class": "currency-symbol"}).find("a").text
		currency_name = r.find("td", {"class":"currency-name"}).find("a",{"class":"currency-name-container"}).text
		currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		currency_price = r.find("a", {"class": "price"}).text
		currency_volume = r.find("a", {"class": "volume"}).text
		link = r.find

		newcoin = open(link)
		newcoin_table

		#print(currency_short_name)
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