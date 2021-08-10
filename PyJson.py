import json
from urllib.request import urlopen

def getCountry(ipaddress):
    response = urlopen("http://freegeoip.net/json/"+ipaddress).read().decode('utf-8')
    responseJson = json.getloads(response)
    return responseJson.get("country_code")

print(getCountry("50.78.253.58"))