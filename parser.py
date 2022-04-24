from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from array import *

def search(search_name, names):
	check = 0
	match = []
	for i in range(len(names)):
		if search_name in names[i]:
			check = 1
			match.append(i)
	if check==0:
		return -1
	else:
		return match

def main():
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome(options=chrome_options)
	url = "https://coinmarketcap.com/"
	driver.get(url)
	driver.execute_script("window.scrollTo(0,1300);")

	data = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')[0:25]

	names = []
	prices = []
	market_caps = []

	for i, rows in enumerate(data):
		name = rows.find_elements_by_tag_name('p')[1].text
		names.append(name)

		price = rows.find_elements_by_tag_name('span')[2].text
		prices.append(price)
		
		market_cap = rows.find_elements_by_tag_name('span')[8].text
		market_caps.append(market_cap)

	table = ["#", "Name", "Price", "Market cap"]
	print("%4s|%20s|%20s|%20s" %(table[0], table[1], table[2], table[3]))
	for i in range(67):
		print("-", end="")
	print("")
	for i in range(len(names)):
		print ("%4d|%20s|%20s|%20s" %(i+1, names[i], prices[i], market_caps[i]))

	driver.close()

	while True:
		search_name = input("\nEnter the name of the currency: ")
		res = search(search_name, names)
		if res==-1:
			print ("No results")
		else:
			for i in range(len(res)):
				print ("%4d|%20s|%20s|%20s" %(res[i]+1, names[res[i]], prices[res[i]], market_caps[res[i]]))

if __name__ == '__main__':
	main()