import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

CHECK_INTERVAL = 300
HEADLESS = False
MAX_PRICE = 60000

SEARCH_URLS = [
    "https://www.avito.ru/all/telefony?q=iphone+15",
    "https://www.avito.ru/all/telefony?q=iphone+15+pro",
    "https://www.avito.ru/all/telefony?q=iphone+16",
]