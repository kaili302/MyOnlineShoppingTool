import urllib3
from bs4 import BeautifulSoup

from stores import Stores

class Scraper:
    httpHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                                "87.0.4280.88 Safari/537.36"}
    http = urllib3.PoolManager(headers=httpHeader)

    @staticmethod
    def fetch_url(url):
        resp = Scraper.http.request('GET', url)
        return BeautifulSoup(resp.data, "html5lib")

    @staticmethod
    def get_john_lewis_price(url):
        soup = Scraper.fetch_url(url)
        return (Stores.John_Lewis.name,
                float(soup.find("p",class_="price price--large").text.strip()[1:]))

    @staticmethod
    def get_argos_price(url):
        soup = Scraper.fetch_url(url)
        return (Stores.Argos.name,
                float(soup.find("li", {"data-test": "product-price-primary"})
                        .get('content').strip()))

    @staticmethod
    def get_currys_price(url):
        soup = Scraper.fetch_url(url)
        return (Stores.Currys.name,
                float(soup.find("strong", {"class": "current",
                                           "data-key":"current-price"})
                          .text.strip()[1:]))

