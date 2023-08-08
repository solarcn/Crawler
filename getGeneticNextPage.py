
#coding:utf-8
import requests
import re
import logging


from bs4 import BeautifulSoup
from stringConvert import convertQ2B
from encoding import get_encoding
from urllib.parse import urljoin  #从相对路径中得到绝对路径


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='response.log', level=logging.DEBUG, format=LOG_FORMAT)


#url = 'http://www.liushuba.com/files/article/html/60/60186/23554540.html'
#url = 'http://www.81xsw.com/0_169/10088024.html'

def get_next_page_url(url,soup): 
    next_page = ''
    logging.debug("Trying to get next page link from soup")
    #r = requests.get(url)
    #soup = BeautifulSoup(r.text,'lxml')
    encoding = get_encoding(soup)
    urls = soup.find_all('a', href=True)
    
    for u in urls:
            if '下一章' in u.text or '下一页' in u.text:
                next_page = urljoin(url,u['href'])
                logging.debug("Getting next page url = " + next_page)
                break
    return next_page;

