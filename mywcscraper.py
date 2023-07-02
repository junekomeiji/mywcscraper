import re
import requests
from bs4 import BeautifulSoup

URL = "https://mywc.kpkt.gov.my/toilet/tandas-awam-kpkt/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#find name of toilet
h2 = str(soup.find_all("h2", class_="text-3xl font-extrabold text-gray-900"))
name = re.findall("<h2[^>]*>([^<]+)</h2>", h2)

print(name)

#find address of toilet
p = str(soup.findAll("p", class_="text-sm text-gray-500 truncate mb-2 uppercase flex flex-row"))
address = re.findall("<span[^>]*>([^<]+)</span>", p)
address[1] = address[1].capitalize()
print(''.join(address))

#find lat and long of toilet
script = str(soup.find_all("script"))
location = re.findall(".+?(?<=setView\(\[)(.\d*\.?\d*)\,(..\d*\.?\d*)", script)
print(location)

#rating
span = str(soup.find_all("span", class_="text-sm"))
rating = re.findall("\((.+?)\)", span)
print(rating)

#facilities
repg = str(soup.find_all("span", class_="px-2"))
facilities = re.findall("<span[^>]*>([^<]+)</span>", repg)
print(facilities)



