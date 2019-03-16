import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.tianqihoubao.com/weather/city.aspx'

txtareaName = '马鞍山'
txtdate = '2018-12-24'
btnSearch = '查 询'
# dateTo = ''

params = {
    "txtareaName":"马鞍山",
    "txtdate":"2018-12-24",
    "btnSearch":"查 询"
    }

html=requests.post(url,data=params)
print(html.text) 
