import logging
import requests

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='temperature_history.log', level=logging.DEBUG, format=LOG_FORMAT)


def main():
    url = 'http://www.tianqihoubao.com/weather/city.aspx'

    params = {
        "txtareaName": "马鞍山",
        "txtdate": "2018-12-24",
        "btnSearch": "查 询"
    }

    try:
        response = requests.post(url, data=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logging.exception('请求失败: %s', err)
        print('请求失败:', err)
        return

    logging.info('请求成功：%s', url)
    print(response.text)


if __name__ == '__main__':
    main() 
