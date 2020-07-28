from requests import *
from bs4 import BeautifulSoup

headers = "Chrome"
url = input("URL:")
url2 =  get(url)
kaynak = BeautifulSoup(url2.content)
versiyon = kaynak.find_all("meta",{"name","generator"})
deneme = kaynak.find_all("meta",{"name":"generator"})
for x in deneme:
    print(x.get("content"))