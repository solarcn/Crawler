# coding:utf-8
import requests
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='response.log', level=logging.DEBUG, format=LOG_FORMAT)


from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random
import re


url = ''
while(not url):
    url = input("请输入网址:").strip()

def get_encoding(soup):
    encod = soup.meta.get(re.compile("^charset$", re.I))
    logging.debug(encod)
    if encod == None:
        encod = soup.meta.get(re.compile("^content-type$", re.I))
        logging.debug(encod)
        if encod == None:
#            content = soup.meta.get('content')
            meta = soup.head.find('meta',attrs={'http-equiv':re.compile("^content-type$", re.I)})
            if meta: 
                content = meta.get('content')
                match = re.search('charset=(.*)', content)
                if match:
                    encod = match.group(1)
                    logging.debug("get_encoding()得到" + encod)
                else:
                    raise ValueError('unable to find encoding')
    return encod

def get_next_page_url(url,soup): 
    next_page = ''
    logging.debug("Trying to get next page link from soup")
    encoding = get_encoding(soup)
    urls = soup.find_all('a', href=True)
    
    for u in urls:
            if u.text.strip() == '下一章' or u.text == '下一页'.strip():
                next_page = urljoin(url,u['href'])
                logging.debug("Getting next page url = " + next_page)
                break
    return next_page

def convertQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
        rstring += chr(inside_code)
    return rstring

def convertB2Q(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x0020:
            inside_code = 0x3000
        else:
            if not (0x0021 <= inside_code and inside_code <= 0x7e):
                rstring += uchar
                continue
            inside_code += 0xfee0
        rstring += chr(inside_code)
    return rstring

def getHeaders(url):
    user_agents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]
    agent = random.choice(user_agents)  # 每次随机抽取一个伪装的客户端浏览器版本号
    headers = {'content-type': 'application/json',
               'Referer': url,
               'User-Agent': agent}
    return headers

def getContent(url):
    result = ''
    title = ''
    nextPage = ''
    logging.info('Sending request to: ' + url)
    r = requests.get(url, headers=getHeaders(url))
    if(r.status_code != 200):
        print("错误代码: " + str(r.status_code))
        print("错误原因: " + r.reason)
        logging.error("错误代码: " + str(r.status_code));
        logging.error("错误原因: " + r.reason)
        quit()
     
    #options lxml(faster) html5lib
    soup = BeautifulSoup(r.text, 'html5lib') 
    encoding = get_encoding(soup)
    if(encoding != None):
        r.encoding = encoding;
        soup = BeautifulSoup(r.text, 'html5lib')
    # result += soup.find('title').text
    urls = soup.find_all('a', href=True)
    nextPage = get_next_page_url(url, soup)
    novelContent = ''
    if(soup.find('div', id='content')):
        novelContent = soup.find('div', id='content')
    else:
        # 如果最后找不到,就把body列出来
        novelContent = soup.body
    if novelContent:
        for br in soup.find_all("br"):
            br.replace_with("\n")  # 替换换行标签
        result += novelContent.text
    if soup.title:
        title = soup.title.text
    return result, nextPage, title

result, not_used, title = getContent(url)
fileName = title[0:title.find('_')] + '.txt'
logging.info('保存为文件名： ' + fileName)
file = open(fileName, 'w+', encoding='utf-8')

i = 0
while 'html' in url and not url.endswith('index.html'):
    result, url, title = getContent(url)
    result = result[0:result.find('http://www.shuquge.com')]
    result = title.split('_')[1].strip() + '\n' + result
    #################################################################
    # 处理result
    #################################################################
    result = result.replace('!', '')
    result = result.replace('?', '')
    result = result.replace('"', '')
    result = result.replace('！', '')
    result = result.replace('？', '')
    result = result.replace('”', '')
    file.write(result)
    i += 1
    logging.info('保存了' + str(i) + '章:  ' + title)
 
file.close()