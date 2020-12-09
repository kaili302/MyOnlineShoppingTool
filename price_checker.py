from scraper import Scraper

from enum import Enum

class Stores(Enum):
    Argos       = 1
    John_Lewis  = 2
    Currys      = 3


class PriceChecker:

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

