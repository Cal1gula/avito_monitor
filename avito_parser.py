import re
from datetime import datetime

from playwright.sync_api import sync_playwright

from config import SEARCH_URLS, HEADLESS


class AvitoParser:

    def __init__(self):
        self.browser = None

    def parse(self):

        items = []

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=HEADLESS
            )

            page = browser.new_page(
                viewport={
                    "width": 1920,
                    "height": 1080
                }
            )

            for search_url in SEARCH_URLS:

                print(f"\nОткрываю:\n{search_url}\n")

                page.goto(
                    search_url,
                    wait_until="domcontentloaded",
                    timeout=60000
                )

                page.wait_for_timeout(5000)

                cards = page.locator(
                    '[data-marker="item"]'
                )

                print("Карточек:", cards.count())

                for i in range(cards.count()):

                    try:

                        card = cards.nth(i)

                        title = card.locator(
                            '[data-marker="item-title"]'
                        ).inner_text()

                        price_text = card.locator(
                            '[data-marker="item-price-value"]'
                        ).inner_text()

                        href = card.locator(
                            '[data-marker="item-title"]'
                        ).get_attribute("href")

                        path = href.split("?")[0]

                        item_id = path.rsplit("_", 1)[1]

                        url = "https://www.avito.ru" + href


                        price = int(
                            "".join(
                                c for c in price_text
                                if c.isdigit()
                            )
                        )

                        city = ""

                        for line in card.inner_text().split("\n"):

                            if any(word in line for word in [

                                "Москва",

                                "обл.",

                                "край",

                                "респ.",

                                "Санкт"

                            ]):

                                city = line
                                break

                        items.append({

                            "id": item_id,

                            "title": title,

                            "price": price,

                            "city": city,

                            "url": url,

                            "search_url": search_url,

                            "found_at": datetime.now().strftime(
                                "%d.%m.%Y %H:%M:%S"
                            )

                        })

                    except Exception as e:

                        print("Ошибка:", e)

            browser.close()

        return items