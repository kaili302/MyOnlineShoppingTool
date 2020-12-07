import os
import sys
import urllib3
import time
from bs4 import BeautifulSoup
from enum import Enum

class Stores(Enum):
    Argos = 1
    John_Lewis = 2


httpHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                             "87.0.4280.88 Safari/537.36"}
http = urllib3.PoolManager(headers=httpHeader)

def fetch_url(url):
    resp = http.request('GET', url)
    return BeautifulSoup(resp.data, "html5lib")

def get_john_lewis_price(url):
    soup = fetch_url(url)
    return (Stores.John_Lewis.name,
            float(soup.find("p",class_="price price--large").text.strip()[1:]))

def get_argos_price(url):
    soup = fetch_url(url)
    return (Stores.Argos.name,
            float(soup.find("li", {"data-test": "product-price-primary"})
                      .get('content').strip()))
