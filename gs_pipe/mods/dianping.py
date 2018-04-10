# -*-encoding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as Soup


HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}


def fetch_html(url):
    resp = requests.get(url, headers=HTTP_HEADERS)
    resp.raise_for_status()
    return resp.content


def parse_dianping_address(html):
    html = Soup(html, "html5lib")
    return html.find("div", attrs={"class": "expand-info address"}).find('span', attrs={"class": "item"}).text.strip()
