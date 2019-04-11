import bs4
import urllib.parse
import urllib3.request
import requests
import re
def SearchForEachCitySubway():
    citiesList = readCSV_Util()
    target_URL_prefix = "https://s.weibo.com/user?q="
    target_URL_suffix="&Refer=SUer_box"
    for city in citiesList:
        url_for_search =target_URL_prefix+urllib.parse.quote(city)+target_URL_suffix
        tempurl=getTheTargetWebPage(url_for_search)
        URl_for_each_Station= "https:/"+tempurl
        print(URl_for_each_Station)

import csv
def readCSV_Util():
    citiesList=[]
    with  open("cities.txt","r") as cities:
        for line in cities:
            citiesList.append(line.strip())
    return citiesList


import bs4
def getTheTargetWebPage(TargetURL):
    page = requests.get(TargetURL)
    print(page.status_code)
    soup= bs4.BeautifulSoup(page.content,"html.parser")
    div = soup.find_all("div",class_="avator")[0]
    div_str=str(div)
    groups=re.search(r'href=\"(.*?)\"',div_str)
    return groups.group()[7:-1]


SearchForEachCitySubway()
