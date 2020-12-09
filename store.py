import logging

from discord_bot import DiscordBot
from scraper import Scraper

class Store:
    def __init__(self, name, css_selector, validator, rtx_cards):
        self.name = name
        self.css_selector = css_selector
        self.validator_url = validator
        self.rtx_cards = rtx_cards

    def check_sanity(self):
        soup = Scraper.fetch_url(self.validator_url)
        found = soup.select(self.css_selector)
        if found:
            DiscordBot.send(f"{self.name} css selector is valid")
            return True
        else:
            DiscordBot.send(f"{self.name} css selector is invalid")
            return False

    def check_availability(self):
        for url in self.rtx_cards:
            soup = Scraper.fetch_url(url)
            found = soup.select(self.css_selector)
            if found:
                DiscordBot.send(f"In Stock: {url}")
            else:
                logging.info(f"{self.name} no stock")
