import requests
import re
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('turtle.db')

cursor = conn.cursor()
#cursor.execute('drop table articles')
cursor.execute('create table articles (id INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL, page Integer, date Date , name varchar(30), url varchar(200))')

url1 = "http://blog.sina.com.cn/s/articlelist_36667063_2_"
url2 = 0
url3 = ".html"

while url2 < 27: 
    url2 += 1
    r = requests.get(url1 + str(url2) + url3)
    #####################
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    result = soup.body.find_all('div',class_ = 'articleCell SG_j_linedot1')
    dict = {}
    for item in result:
        a = item.find('a')
        t = re.sub('.{4}年.{1,2}月.{1,2}日\xa0','',a.text)
        if t in dict:
            pass
            dict[t][0].append(a.get('href'))
            dict[t][1].append(item.find('span', class_ = 'atc_tm SG_txtc').text)
        else:
            dict.setdefault(t,[])
            dict[t].append('')
            dict[t].append('')
            dict[t][0] = []
            dict[t][0].append(a.get('href'))
            dict[t][1] = []
            dict[t][1].append(item.find('span', class_ = 'atc_tm SG_txtc').text)
    	
    for key in dict:
        i = 0
        while i < len(dict[key][0]):
            # key
            # dict[key][0][i]
            # dict[key][1][i]
            #cursor.execute('insert into articles ( date, name, url) values    (\'' + dict[key][1][0] + '\' ,\'' + key + '\',\'' + key,dict[key][0][i] + '\')')
            # 'insert into articles ( date, name, url) values    (\'' + dict[key][1][i] + '\' ,\'' + key + '\',\'' + dict[key][0][i] + '\')'
            cursor.execute('insert into articles ( page, date, name, url) values    (\''+ str(url2)+ '\' ,\'' + dict[key][1][i] + '\' ,\'' + key + '\',\'' + dict[key][0][i] + '\')')
            i += 1
cursor.close()
conn.commit()
conn.close()