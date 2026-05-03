import re
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='response.log', level=logging.DEBUG, format=LOG_FORMAT)


def get_encoding(soup):
    encod = soup.meta.get(re.compile("^charset$", re.I)) if soup.meta else None
    logging.debug(encod)
    if encod is None:
        encod = soup.meta.get(re.compile("^content-type$", re.I)) if soup.meta else None
        logging.debug(encod)
        if encod is None:
#            content = soup.meta.get('content')
            meta = soup.head.find('meta', attrs={'http-equiv': re.compile("^content-type$", re.I)}) if soup.head else None
            if meta:
                content = meta.get('content', '')
                match = re.search('charset=(.*)', content)
                if match:
                    encod = match.group(1)
                    logging.debug("get_encoding()得到" + encod)
                else:
                    logging.warning("Unable to find charset in meta content: %s", content)
    return encod