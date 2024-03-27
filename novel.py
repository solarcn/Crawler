# coding:utf-8
import logging
import time

LOG_FORMAT = "%(asctime)s  %(levelname)s  %(message)s"
logging.basicConfig(filename='aaaa.log', level=logging.DEBUG, format=LOG_FORMAT,filemode='w')

import requests
import random
import re


from encoding import get_encoding
from getGeneticNextPage import get_next_page_url
from bs4 import BeautifulSoup 
from stringConvert import convertQ2B
 
pattern = re.compile(r'www.{1,20}com.?】')
# patternBQG = re.compile(r'笔趣阁')

# 笔趣阁 biquke.com
# 八一中文 81xsw.com


url = input("请输入网址:").strip()
if url == '':
    url = 'http://www.81xsw.com/0_169/10088024.html'
fileName = input("请输入要保存的文件名,默认novel_temp.txt:")
if fileName == '':
    fileName = 'novel_temp.txt'
elif fileName[-4:] != '.txt':
    fileName = fileName + '.txt'


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
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',   # my computer
        'Mozilla/5.0 (Linux; Android 6.0;Nexus 5 Build/MRA58N) AppleWebKit/537.36(KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
        "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
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
    try:
        r = requests.get(url, headers=getHeaders(url))
    except requests.exceptions.ConnectionError:
        logging.error("ConnectionError")
        r = requests.get(url, headers=getHeaders(url))

    if (r.status_code != 200):
        print("错误代码: " + str(r.status_code))
        print("错误原因: " + r.reason)

        logging.error("错误代码: " + str(r.status_code));
        logging.error("错误原因: " + r.reason)
        quit()
    #     logging.debug(r.headers.getparam('charset'))
    #    r.encoding = 'gbk'
    #     r.encoding = 'utf-8'
    #lxml更快
    soup = BeautifulSoup(r.text, 'html5lib')
    encoding = get_encoding(soup)
    if (encoding != None):
        r.encoding = encoding;
        soup = BeautifulSoup(r.text, 'html5lib')

    result += soup.find('title').text

    urls = soup.find_all('a', href=True)
    nextPage = get_next_page_url(url, soup)
    novelContent = ''

    if (soup.find('div', id='content')):
        novelContent = soup.find('div', id='content')
    elif (soup.find('div', id='contents')):
        novelContent = soup.find('div', id='contents')
    elif (soup.find('div', id='BookText')):
        novelContent = soup.find('div', id='BookText')
    elif (soup.find('div', id='nr_content')):
        novelContent = soup.find('div', id='nr_content')
    elif (soup.find('dd', id='contents')):
        novelContent = soup.find('dd', id='contents')

    elif (soup.find('div', class_='article-con')):
        novelContent = soup.find('div', class_='article-con')
    elif (soup.find('div', class_='read-content j_readContent')):
        novelContent = soup.find('div', class_='article-con')
    else:
        # 如果最后找不到,就把body列出来
        novelContent = soup.body
    #        logging.debug('novelContent: ' + soup.body.text)

    if novelContent:
        for br in soup.find_all("br"):
            br.replace_with("\n")  # 替换换行标签
        result += novelContent.text
    if soup.title:
        title = soup.title.text

        # s = re.sub('<br\s*?>', '\n', yourTextHere)

    #        #获取章节名称
    # section_name=soup.select('#wrapper .content_read .box_con .bookname h1')[0]
    ##获取章节文本
    # section_text=soup.select('#wrapper .content_read .box_con #content')[0].text
    # for ss in section_text.select("script"):                #删除无用项
    #    ss.decompose()
    ##按照指定格式替换章节内容，运用正则表达式
    # section_text=re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')
    # ---------------------
    # 作者：SameWorld
    # 来源：CSDN
    # 原文：https://blog.csdn.net/baidu_26678247/article/details/75086587
    # 版权声明：本文为博主原创文章，转载请附上博文链接！

    # for line in novelContent:
    #    result = result + str(line) + '\n'
    #        string = convertQ2B(str(line)).lower()
    ##         logging.debug(string)
    #        if string == '<br/>':
    #            pass
    ##             result += '\n'
    #        elif "】" in string:
    #            logging.debug("原始:  " + string)
    #            string = re.sub(pattern,'',string)
    ##             string = string.lstrip()[16:];
    #            logging.debug("变换:  " + string)
    #            result = result + string + '\n'
    ##             logging.debug("删除:" + string)
    ##         elif "笔趣阁" in string:
    ##             logging.debug("原始:  " + string)
    ##             string = string[:-4];
    ##             logging.debug("变换:  " + string)
    ##             result = result + string + '\n'
    #        else:
    #            result = result + string + '\n'
    return result, nextPage, title


file = open(fileName, 'a+', encoding='utf-8')

i = 0
while 'html' in url and not url.endswith('index.html'):
    result, url, title = getContent(url)
    #################################################################
    # 处理result
    #################################################################
    # result = result.replace('!', '')
    # result = result.replace('?', '')
    # result = result.replace('"', '')
    # result = result.replace('！', '')
    # result = result.replace('？', '')
    # result = result.replace('”', '')
    file.write(result)
    i += 1
    logging.info('保存了' + str(i) + '章:  ' + title)
    time.sleep(1)

# nextPage, url2 = getContent(url1 + url2)
##logging.debug(nextPage);
# file.write(nextPage)

file.close();