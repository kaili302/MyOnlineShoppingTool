import json
from scraper import Scraper
from discord_bot import DiscordBot


def check_overclockers():
    # url = "https://www.overclockers.co.uk/pc-components/graphics-cards/nvidia/geforce-rtx-3090"
    url = "https://www.overclockers.co.uk/pc-components/graphics-cards/nvidia/geforce-rtx-3060-ti"
    soup = Scraper.fetch_url(url)
    found = soup.find("span", class_="delivery_container", partial=False)
    if found:
        DiscordBot.send(f"In stock: {url}")


def check_ccl():
    # url = "https://www.cclonline.com/category/430/PC-Components/Graphics-Cards/NVIDIA-Chipset-Graphics-Cards/"
    url = "https://www.cclonline.com/category/430/PC-Components/Graphics-Cards/NVIDIA-Chipset-Graphics-Cards/attributeslist/1267059/"
    soup = Scraper.fetch_url(url)
    found = soup.find("a", class_="btnAddToBasket", partial=False)
    if found:
        DiscordBot.send(f"In Stock: {url}")

def check_scan():
    # url = "https://www.scan.co.uk/shop/gaming/gpu-nvidia/all"
    url = "https://www.scan.co.uk/shop/gaming/gpu-nvidia/geforce-rtx-3060-ti-graphics-cards"
    soup = Scraper.fetch_url(url)
    found_buy = soup.findAll("div", class_="buyButton", partial=False)
    if len(found_buy) > 1:
        DiscordBot.send(f"In Stock: {url}")

    found_pre_order = soup.find("div", class_="preOrder", partial=False)
    if found_pre_order:
        DiscordBot.send(f"Pre order: {url}")

check_overclockers()
check_ccl()
check_scan()
