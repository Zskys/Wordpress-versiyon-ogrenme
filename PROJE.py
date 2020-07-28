from requests import *
from bs4 import BeautifulSoup
user_agent = {'User-agent': 'Mozilla/5.0'}
url = input("URL:")
url2  = get(url, headers = user_agent)
kaynak = BeautifulSoup(url2.content)
versiyon = kaynak.find_all("meta",{"name","generator"})
deneme = kaynak.find_all("meta",{"name":"generator"})
for x in deneme:
    print(x.get("content"))
