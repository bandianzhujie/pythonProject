from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import datetime
import random
import json
import re


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll('a',
                                                          href=re.compile("^(/wiki/)((?!:).)*"))

def getHistoryIPs(pageUrl):
    pageurl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl+"&action=history"
    print("hostory url is: "+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    ipAddresses = bsObj.findAll('a',{"class":"mw-userlink mw-anonuselink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipaddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipaddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.getloads(response)
    return responseJson.get("country_code")

#print(getCountry("50.78.253.58"))

links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('-----------------------')
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+" is from " + country)
    newlink = links[random.randint(0, len(links) - 1)].attrs['href']
    links = getLinks(newlink)


