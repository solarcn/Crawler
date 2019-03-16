import requests
import re
from bs4 import BeautifulSoup
import sqlite3
from stringConvert import convertB2Q
conn = sqlite3.connect('turtle.db')

cursor = conn.cursor()
cursor.execute("select *  from turtle_real order by date limit 300 offset 0")
result = cursor.fetchall()
file = open('temp0000001.txt', 'w', encoding="utf-8")


for item in result:
    file.write("/////////////////////////////////////////////////////////////////\n")
    file.write(item[2])
    print("Processing: " + item[4])
    r = requests.get(item[4])
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'lxml')
    div = soup.body.find('div', id = 'sina_keyword_ad_area2')

    contents = []
    for item in div.find_all(True):
        if item.name == 'p':
                contents.append([])
                index = len(contents) -1
                contents[index] = item.text
        if item.name == 'table':
                contents.append([])
                index = len(contents) - 1
                # contents[index] = []
                for row in item.find_all('tr'):
                    contents[index].append([])
                    j = len(contents[index]) - 1
                    for cell in row.find_all('td'):
                        contents[index][j].append(cell.text.strip())
        if item.name == 'a':
                contents.append([])
                index = len(contents) -1
                contents[index] = item.text
    for item in contents:
        if(type(item) != type('')) :
            for row in item:
                for cell in row:
                    file.write("{0:<8}".format(cell,'x'))
                    #file.write(cell.ljust(8))
                file.write('\n')            

        else :
            file.write(item + '\n')
    file.flush()
    
file.close()