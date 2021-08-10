from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e :
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
        print(e)
    return title
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title is not found")
else:
    print(title)
