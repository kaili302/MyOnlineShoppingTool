import urllib3
from bs4 import BeautifulSoup

class Scraper:
    httpHeader = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                                "87.0.4280.88 Safari/537.36"}
    http = urllib3.PoolManager(headers=httpHeader)

    @staticmethod
    def fetch_url(url):
        resp = Scraper.http.request('GET', url)
        return BeautifulSoup(resp.data, "html5lib")

