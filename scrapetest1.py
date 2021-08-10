from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except (HTTPError, URLError) as e :
    print(e)
try:
    bsObj = BeautifulSoup(html.read())
    nameList = bsObj.findAll("span",{"class":"green"})
    for name in nameList:
        print(name.get_text())
except AttributeError as e:
    print(e)