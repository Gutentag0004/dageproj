# import bs4
# import requests
# import json
# import re
# import SpiderSerachForEachCitySubway
# import time
#
# cook = {"Cookie":"SINAGLOBAL=4531959546150.666.1537891697896; UM_distinctid=16a07f7a6f2c-0f68bc3bf3bca1-7a1437-144000-16a07f7a6f541c; _s_tentry=www.baidu.com; Apache=9459268180019.918.1554911831940; ULV=1554911831963:11:2:1:9459268180019.918.1554911831940:1554051693954; login_sid_t=02e2438c046ca37adb5bfff24e1fd783; cross_origin_proto=SSL; UOR=tech.ifeng.com,widget.weibo.com,login.sina.com.cn; YF-V5-G0=bc033c7c7d5164aa92fea9d75cc6f127; wb_cmtLike_5307882410=1; TC-V5-G0=f88ad6a0154aa03e3d2a393c93b76575; wb_view_log_5307882410=1536*8641.25; TC-Page-G0=7a922a70806a77294c00d51d22d0a6b7|1555171409|1555171249; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; WBtopGlobal_register_version=2019041400; SCF=AqBTzk8Jtd6eJ6OYrGuY2l3_VZm9-5VHDhNdEKf3xiq_qtmbfPDYW5MV08lGnCdC_-E3eTeYrdsZvSe0Ox9oM8E.; ALF=1586708980; SUB=_2A25xtn4pDeRhGeNN61UZ-CzIyjyIHXVSwujhrDV8PUJbmtBeLXetkW9NSc33qCB_MJIHeuMrcjq_dI5gSVjQuuqy; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWI5Z0d0eAwO1eYfZ7F39B25NHD95Qfe05N1hnESh27Ws4Dqcj_i--fiKyWi-27i--Xi-iFiK.pi--ci-8siKysi--fi-z7iKysi--ciK.Ni-zc; SUHB=02MvBTygjM0k1l; SSOLoginState=1555172986; YF-Page-G0=416186e6974c7d5349e42861f3303251|1555174122|1555174052; webim_unReadCount=%7B%22time%22%3A1555174124621%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"}
# # def searchForContentofEachURL():
# #     url="https://weibo.com/bjsubway?is_search=0&visible=0&is_all=1&pagebar=1&is_tag=0&profile_ftype=1&page=2#feedtop"
# #     page=requests.get(url,cookies=cook)
# #     print(page.status_code)
# #     soup=bs4.BeautifulSoup(page.content,"html.parser")
# #     print(soup)
# #     tag_a=soup.find("a",class_="page S_txt1")
# #     print(tag_a)
# head="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
#
#
#
# def  reloadContent(theTarget, currentpage,city):
#     url = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100106&profile_ftype=1&is_all=1&pagebar={bar}&pl_name=Pl_Official_MyProfileFeed__25&id=1001062778292197&script_uri=/{target}&feed_type=0&page={current}&pre_page=1&domain_op=100106&__rnd=1555079765246"
#
#     table = requests.get(url.format(bar="0",target=str(theTarget),current=str(currentpage)),cookies=cook)
#     cellFunction(table)
#     time.sleep(1)
#     table = requests.get(url.format(bar="1", target=str(theTarget), current=str(currentpage)), cookies=cook)
#     cellFunction(table)
#     time.sleep(1)
#
# # print(url.format(bar="0",target=str(theTarget),current=str(currentpage)))
# def cellFunction(table,city):
#     data = json.loads(table.text)
#     strs = data.get("data")
#     m = bs4.BeautifulSoup(strs, "html.parser")
#     all_class = m.find_all("div", class_="WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like ")
#     for t in all_class:
#         tmp = str(t)
#         tmphtml = bs4.BeautifulSoup(tmp, "html.parser")
#         st = tmphtml.find("div", class_="WB_from S_txt2")
#         t = str(st)
#         mf = re.search(r'title=\"(.*?)\"', t)
#         contents=[]
#         acontent = tmphtml.find("a", class_="a_topic")
#         if (acontent is not None):
#             tt = str(acontent)
#             afind = re.search(r'>(.*?)</a>', tt)
#             print(afind.group()[1:-4])
#             contents.append(afind.group()[1:-4])
#         content = tmphtml.find("div", class_="WB_text W_f14")
#         contenttxt = str(content)
#         mt = re.search(r"</a>(.*?)<", contenttxt)
#
#         if (mt is not None):
#             print(mt.group()[4:-1])
#         print(mf.group()[7:-1])
#         contents.append(mt.group()[4:-1]+mf.group()[7:-1])
#         SpiderSerachForEachCitySubway.FileReadandWrite(city,contents)
#
# def gettheCountPage(theTarget):
#
#     url = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100106&profile_ftype=1&is_all=1&pagebar={bar}&pl_name=Pl_Official_MyProfileFeed__25&id=1001062778292197&script_uri=/{target}&feed_type=0&page={current}&pre_page=1&domain_op=100106&__rnd=1555079765246"
#     table = requests.get(url.format(bar="1", target=str(theTarget), current=str(1)), cookies=cook)
#     data = json.loads(table.text)
#     strs = data.get("data")
#     m = bs4.BeautifulSoup(strs, "html.parser")
#     all_class = m.find("a", class_="page S_txt1")
#     countStr = str(all_class)
#     result=re.search(r"countPage=(.*?)\"",countStr)
#     return result.group()[10:-1]
#
#
#
#
# def SpiderStart(theTarget,city):
#     firstPageUrl="https://weibo.com/"+theTarget+"?is_all=1&page=1"
#     theCountPage= int(gettheCountPage(theTarget))
#     print(theCountPage)
#
#     for page in range(theCountPage):
#         TestSpider(theTarget,page+1,city)
#
#         reloadContent(theTarget,page+1,city)
#
# # SpiderStart("bjsubway")
#
#
# def TestSpider(thetarget,pages,city):
#     url = "https://weibo.com/{target}?pids=Pl_Official_MyProfileFeed__25&profile_ftype=1&is_all=1&ajaxpagelet=1&ajaxpagelet_v6=1&page={page}"
#     html = requests.get(url.format(target=thetarget,page=(str(pages))),cookies=cook)
#     print(html.text)
#     m = re.search("<script>parent.FM.view\((.*?)\)</script>",html.text)
#     result = m.group()[23:-10]
#     t = json.loads(result)
#     soup = bs4.BeautifulSoup(t.get("html"))
#     all_class = soup.find_all("div", class_="WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like ")
#     for eachclass in all_class:
#         tmp = str(eachclass)
#         tmphtml = bs4.BeautifulSoup(tmp, "html.parser")
#         st = tmphtml.find("div", class_="WB_from S_txt2")
#         t = str(st)
#         mf = re.search(r'title=\"(.*?)\"', t)
#         acontent = tmphtml.find("a", class_="a_topic")
#         contents = []
#         if (acontent is not None):
#             tt = str(acontent)
#             afind = re.search(r'>(.*?)</a>', tt)
#             print(afind.group()[1:-4])
#             contents.append(afind.group()[1:-4])
#         content = tmphtml.find("div", class_="WB_text W_f14")
#         contenttxt = str(content)
#         mt = re.search(r"</a>(.*?)<", contenttxt)
#
#         if (mt is not None):
#             print(mt.group()[4:-1])
#         print(mf.group()[7:-1])
#         contents.append(mt.group()[4:-1]+mf.group()[7:-1])
#         print(content)
#         FileReadandWrite(city,content)
#
#
# ##改造截取算法
#
#
# def SearchForEachCitySubway():
#     citiesList = readCSV_Util()
#     target_URL_prefix = "https://s.weibo.com/user?q="
#     target_URL_suffix="&Refer=SUer_box"
#
#
#     for city in citiesList:
#         print(city)
#         url_for_search =target_URL_prefix+urllib.parse.quote(city)+target_URL_suffix
#         tempurl=getTheTargetWebPage(url_for_search)
#         URl_for_each_Station= "https:/"+tempurl
#         print(URl_for_each_Station)
#         print(tempurl[11:-1])
#         theTarget=tempurl[11:-1]
#         SearchforContent.SpiderStart(theTarget,city)
#         time.sleep(1)
#
# SearchForEachCitySubway()
















import bs4
import urllib.parse
import urllib3.request
import requests
import re
import os
import csv
import time
import json

cook = {"Cookie":"SINAGLOBAL=4531959546150.666.1537891697896; UM_distinctid=16a07f7a6f2c-0f68bc3bf3bca1-7a1437-144000-16a07f7a6f541c; _s_tentry=www.baidu.com; Apache=9459268180019.918.1554911831940; TC-V5-G0=9183dd4bc08eff0c7e422b0d2f4eeaec; ULV=1554911831963:11:2:1:9459268180019.918.1554911831940:1554051693954; login_sid_t=02e2438c046ca37adb5bfff24e1fd783; cross_origin_proto=SSL; Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; WBtopGlobal_register_version=edef3632d17f5fb3; UOR=tech.ifeng.com,widget.weibo.com,login.sina.com.cn; wb_cmtLike_5307882410=1; SCF=AqBTzk8Jtd6eJ6OYrGuY2l3_VZm9-5VHDhNdEKf3xiq_qtmbfPDYW5MV08lGnCdC_-E3eTeYrdsZvSe0Ox9oM8E.; ALF=1586708980; SUB=_2A25xtn4pDeRhGeNN61UZ-CzIyjyIHXVSwujhrDV8PUJbmtBeLXetkW9NSc33qCB_MJIHeuMrcjq_dI5gSVjQuuqy; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWI5Z0d0eAwO1eYfZ7F39B25NHD95Qfe05N1hnESh27Ws4Dqcj_i--fiKyWi-27i--Xi-iFiK.pi--ci-8siKysi--fi-z7iKysi--ciK.Ni-zc; SUHB=02MvBTygjM0k1l; SSOLoginState=1555172986; wvr=6; wb_view_log_5307882410=1536*8641.25; TC-Page-G0=7a922a70806a77294c00d51d22d0a6b7|1555252326|1555252326; webim_unReadCount=%7B%22time%22%3A1555252348622%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"}
head="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

def FileReadandWrite(name,content):
    rootpath = "C:\\Users\\GPH‘s\\PycharmProjects\\dageproj\\result"
    file=open(rootpath+"\\"+name+".csv","a+",newline='',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(content)#content为列表包括时间和内容
    file.close()


# 获得每个查询目标的url以及查找name

def readCSV_Util():
    citiesList=[]
    with  open("cities.txt","r") as cities:
        for line in cities:
            citiesList.append(line.strip())

    return citiesList

def getTheTargetWebPage(TargetURL):
    page = requests.get(TargetURL)
    print(page.status_code)
    soup= bs4.BeautifulSoup(page.content,"html.parser")
    div = soup.find_all("div",class_="avator")[0]
    div_str=str(div)
    groups=re.search(r'href=\"(.*?)\"',div_str)
    return groups.group()[7:-1]

def TestSpider(thetarget,pages,city):
    print("TestSpider,{},{},{}",thetarget,pages,city)
    url = "https://weibo.com/{target}?pids=Pl_Official_MyProfileFeed__25&profile_ftype=1&is_all=1&ajaxpagelet=1&ajaxpagelet_v6=1&page={page}"
    print(url.format(target=thetarget,page=(str(pages))))
    time.sleep(5)
    html = requests.get(url.format(target=thetarget,page=(str(pages))),cookies=cook)
    m = re.search("<script>parent.FM.view\((.*?)\)</script>",html.text)
    result = m.group()[23:-10]
    # print("result"+result)
    t = json.loads(result)
    # print(t)

    soup = bs4.BeautifulSoup(t.get("html"))
    all_class = soup.find_all("div", class_="WB_detail")
    print(all_class.__len__())
    for eachclass in all_class:
        tmp = str(eachclass)
        tmphtml = bs4.BeautifulSoup(tmp, "html.parser")
        st = tmphtml.find("div", class_="WB_from S_txt2")
        t = str(st)
        mftime = re.search(r'title=\"(.*?)\"', t)
        acontent = tmphtml.find("a", class_="a_topic")
        contents = []
        contents.append(mftime.group()[7:-1])
        # print(mftime.group()[7:-1])
        if (acontent is not None):
            tt = str(acontent)
            afind = re.search(r'>(.*?)</a>', tt)
            # print(afind.group()[1:-4])
            contents.append(afind.group()[1:-4])
        content = tmphtml.find("div", class_="WB_text W_f14")
        contenttxt = str(content)
        mt = re.search(r"</a>(.*?)<", contenttxt)

        if (mt is not None):
            # print(mt.group()[4:-1])
            contents.append(mt.group().strip()[4:-1])


        # print(contents)

        FileReadandWrite(city,contents)




def  reloadContent(theTarget, currentpage,city):
    print("reloadContent+{},{},{}",theTarget,currentpage,city)
    url = "https://weibo.com/{target}"
    ttt = requests.get(url.format(target=theTarget), cookies=cook)
    p = ttt.text
    domain_id = re.search(r"CONFIG\['page_id'\]=(.*?);", p).group()[19:-2]
    domain = re.search(r"CONFIG\['domain'\]=(.*?);", p).group()[18:-2]
    url2 = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain={thedomain}&profile_ftype=1&is_all=1&pagebar={bar}&pl_name=Pl_Official_MyProfileFeed__25&id={domainid}&script_uri=/{target}&feed_type=0&page={current}&pre_page={current}&domain_op={thedomain}"
    table = requests.get(url2.format(bar="0",domainid=domain_id,target=str(theTarget),thedomain=domain,current=str(currentpage)),cookies=cook)
    cellFunction(table,city)

    table = requests.get(url2.format(bar="1",domainid=domain_id,target=str(theTarget),thedomain=domain,current=str(currentpage)), cookies=cook)
    cellFunction(table,city)


# print(url.format(bar="0",target=str(theTarget),current=str(currentpage)))
def cellFunction(table,city):

    print("cellfunction")
    data = json.loads(table.text)
    strs = data.get("data")
    # print(strs)
    m = bs4.BeautifulSoup(strs, "html.parser")
    all_class = m.find_all("div", class_="WB_detail")
    print(all_class.__len__())

    for t in all_class:
        tmp = str(t)
        tmphtml = bs4.BeautifulSoup(tmp, "html.parser")
        st = tmphtml.find("div", class_="WB_from S_txt2")
        t = str(st)
        mftime = re.search(r'title=\"(.*?)\"', t)
        contents=[]
        # print(mftime.group()[7:-1])
        contents.append(mftime.group()[7:-1])
        acontent = tmphtml.find("a", class_="a_topic")
        if (acontent is not None):
            tt = str(acontent)
            afind = re.search(r'>(.*?)</a>', tt)
            # print(afind.group()[1:-4])
            contents.append(afind.group()[1:-4])
        content = tmphtml.find("div", class_="WB_text W_f14")
        contenttxt = str(content)
        mt = re.search(r"</a>(.*?)<", contenttxt)

        if (mt is not None):
            # print(mt.group()[4:-1])
            contents.append(mt.group()[4:-1])

        FileReadandWrite(city,contents)
def gettheCountPage(theTarget):

    url = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100106&profile_ftype=1&is_all=1&pagebar={bar}&pl_name=Pl_Official_MyProfileFeed__25&id=1001062778292197&script_uri=/{target}&feed_type=0&page={current}&pre_page=1&domain_op=100106&__rnd=1555079765246"
    table = requests.get(url.format(bar="1", target=str(theTarget), current=str(1)), cookies=cook)
    data = json.loads(table.text)
    strs = data.get("data")
    m = bs4.BeautifulSoup(strs, "html.parser")
    all_class = m.find("a", class_="page S_txt1")
    countStr = str(all_class)
    result=re.search(r"countPage=(.*?)\"",countStr)
    return result.group()[10:-1]


def SpiderStart(theTarget,city):
    print("SpiderStart,{},{}",theTarget,city)
    theCountPage= int(gettheCountPage(theTarget))
    print(theCountPage)

    for page in range(theCountPage):
        print(page,page,page,page,page,page,page,page,page,page,page,page,page)
        TestSpider(theTarget,page+1,city)
        reloadContent(theTarget,page+1,city)


def SearchForEachCitySubway():

    citiesList = readCSV_Util()
    target_URL_prefix = "https://s.weibo.com/user?q="
    target_URL_suffix="&Refer=SUer_box"


    for city in citiesList:
        print(city)
        url_for_search =target_URL_prefix+urllib.parse.quote(city)+target_URL_suffix
        print(url_for_search)
        tempurl=getTheTargetWebPage(url_for_search)
        print("tempurl="+tempurl)
        URl_for_each_Station= "https:/"+tempurl
        print("URL_for_each_Station="+URl_for_each_Station)
        print(tempurl[11::])
        theTarget=tempurl[11::]
        print(theTarget)
        SpiderStart(theTarget,city)
        time.sleep(6)


# SearchForEachCitySubway()

url = "https://weibo.com/{target}?pids=Pl_Official_MyProfileFeed__25&profile_ftype=1&is_all=1&ajaxpagelet=1&ajaxpagelet_v6=1&page={page}"
m=requests.get(url.format(target="bjsubway",page="1",),cookies=cook)
mxt=m.text
mtxt= re.search("<script>parent.FM.view\((.*?)\)</script>",mxt)
result = mtxt.group()[23:-10]
jr1 = json.loads(result).get("html")
url2 = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain={thedomain}&profile_ftype=1&is_all=1&pagebar={bar}&pl_name=Pl_Official_MyProfileFeed__25&id={domainid}&script_uri=/{target}&feed_type=0&page={current}&pre_page={current}&domain_op={thedomain}"
t = requests.get(url2.format(target="bjsubway",thedomain="100106",bar="1",domainid="1001062778292197",current="1"),cookies=cook)
ttxt= t.text
jr2= json.loads(ttxt).get("data")
url3="https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100106&profile_ftype=1&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__25&id=1001062778292197&script_uri=/bjsubway&feed_type=0&page=1&pre_page=1&domain_op=100106&__rnd=1555258322261"
t3 = requests.get(url3,cookies=cook)
ttxt3= t3.text
jr3= json.loads(ttxt3).get("data")
print(1)
print(url2.format(target="bjsubway",thedomain="100106",bar="1",domainid="1001062778292197",current="1"))
print(url3)





















