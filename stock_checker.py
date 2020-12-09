import json
import time
from store import Store

# def check_overclockers():
    # # url = "https://www.overclockers.co.uk/pc-components/graphics-cards/nvidia/geforce-rtx-3090"
    # url = "https://www.overclockers.co.uk/pc-components/graphics-cards/nvidia/geforce-rtx-3060-ti"
    # soup = Scraper.fetch_url(url)
    # found = soup.find("span", class_="delivery_container", partial=False)
    # if found:
        # DiscordBot.send(f"In stock: {url}")


# def check_ccl():
    # # url = "https://www.cclonline.com/category/430/PC-Components/Graphics-Cards/NVIDIA-Chipset-Graphics-Cards/"
    # url = "https://www.cclonline.com/category/430/PC-Components/Graphics-Cards/NVIDIA-Chipset-Graphics-Cards/attributeslist/1267059/"
    # soup = Scraper.fetch_url(url)
    # found = soup.find("a", class_="btnAddToBasket", partial=False)
    # if found:
        # DiscordBot.send(f"In Stock: {url}")


class StockChecker:
    def __init__(self, config):
        self.stores = StockChecker.load_stores(config)

    @staticmethod
    def load_stores(config):
        stores = []
        with open(config) as f:
            data = json.load(f)
            for d in data:
                stores.append(Store(d["name"], d["cssSelector"],
                                    d["cssSelectorValidator"], d["urls"]))
        return stores

    def sanity_check(self):
        for store in self.stores:
            store.check_sanity()

    def run(self):
        for store in self.stores:
            store.check_availability()

checker = StockChecker("rtx.json")
checker.sanity_check()

checker.run()
