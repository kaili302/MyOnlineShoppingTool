import json
import time
from store import Store

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
