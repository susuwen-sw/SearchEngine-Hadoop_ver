import requests
import urllib.request
from bs4 import BeautifulSoup
import re
import os
import time

def get_URLs(url,head):
    
    request=urllib.request.Request(url=url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Cookie': 'll="108296"; bid=_xFIRNVTmTs; _vwo_uuid_v2=D865A692C555BB55A5DCC2609E054448E|c2409dd345c8de8cb52bfb6f62b9323e; gr_user_id=72bfcafc-2db4-418f-bd60-efbd7c3f3b9e; __gads=ID=82436f2e6b7b8466-22d4c8a156d200a4:T=1650377969:RT=1650377969:S=ALNI_MZ6xUl8hH9ky1D0xLkk1_nndEeEYQ; vtd-d="1"; viewed="7047153_19982539"; ap_v=0,6.0; __utma=30149280.637538036.1651233662.1651233662.1651233662.1; __utmz=30149280.1651233662.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmz=223695111.1651233662.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmb=223695111.0.10.1651233662; __utma=223695111.1455219369.1645023386.1645023386.1651233662.2; _pk_ses.100001.4cf6=*; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1651233663%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Di7sD3aL3Ytw-BL076AImIeMD3wnwe0L-Mbgi401RNjG9MGMlcWFGyIViArT7HCkM%26wd%3D%26eqid%3Da23edf7f000c523100000003626bd374%22%5D; __utmt=1; __utmb=30149280.6.10.1651233662; __gpi=UID=0000051502bb5722:T=1651233844:RT=1651233844:S=ALNI_Mb2nKxRaGkb9hQ-ObFaqo0aTccOlQ; _pk_id.100001.4cf6=7030a229b165e812.1645023385.2.1651233899.1645023385.'
}


re_url = re.compile('<a href="(.*?)">(.*?)</a>')

for num in range(0,8240,20):
    db_url = "https://movie.douban.com/subject/1291546/reviews?start="+str(num)
    html = get_URLs(db_url,head)
    soup = BeautifulSoup(html,"html.parser")
    for i in soup.find_all('div',class_=['main-bd']):
        i = str(i)
        url = re.findall(re_url,i)
        if(len(url)>0):
            url,url_title = url[0]
            with open('db_review_url_film2.txt','a',encoding='utf-8') as f:
                f.write("%s\t%s"%(url,url_title))
                f.write('\n')
    print('----','page',str(num),'finish','----')
    time.sleep(0.2)
