import requests
from bs4 import BeautifulSoup
import lxml

all_links = BeautifulSoup(requests.get("https://avtoelon.uz").text, "lxml").find("ul", class_="links-list links-list--column-count-6 js-links-list").find_all("li", class_="links-list__item")

for link in all_links:

	try:
		
		url_category = "https://avtoelon.uz" + link.find("a", class_="links-list__link").get("href")
		name_machine = link.find("a", class_="links-list__link").text
		all_automobils = BeautifulSoup(requests.get(url_category).text, "lxml").find_all("span", class_="a-el-info-title")
		
		for auto_link in all_automobils:
		
			link_level_3 = "https://avtoelon.uz" + auto_link.find("a").get("href")
			automobil = BeautifulSoup(requests.get(link_level_3).text, "lxml")
			price = automobil.find("span", class_="a-price__text").text

			all_attributes = automobil.find_all("dd", class_="value clearfix")

			city = all_attributes[0].text
			year = all_attributes[1].text
			engine_volume = all_attributes[2].text
			body = all_attributes[3].text
			mileage = all_attributes[4].text
			transmission = all_attributes[5].text
			drive_unit = all_attributes[6].text
			
	except Exception as e:
		continue
