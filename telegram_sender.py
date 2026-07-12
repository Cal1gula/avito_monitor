import requests

from config import BOT_TOKEN, CHAT_ID


class TelegramSender:

    def __init__(self):
        self.url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    def send_new_item(self, item):

        text = (
            "🆕 Новое объявление\n\n"
            f"📱 {item['title']}\n\n"
            f"💰 {item['price']:,} ₽\n"
            f"📍 {item['city']}\n\n"
            f"🔗 {item['url']}"
        )

        requests.post(
            self.url,
            data={
                "chat_id": CHAT_ID,
                "text": text
            },
            timeout=20
        )

    def send_price_changed(self, item, old_price):

        diff = old_price - item["price"]

        text = (
            "📉 Цена изменилась\n\n"
            f"📱 {item['title']}\n\n"
            f"Было: {old_price:,} ₽\n"
            f"Стало: {item['price']:,} ₽\n"
            f"Снижение: {diff:,} ₽\n\n"
            f"📍 {item['city']}\n\n"
            f"🔗 {item['url']}"
        )

        response = requests.post(
            self.url,
            data={
                "chat_id": CHAT_ID,
                "text": text
            },
            timeout=20
        )

        print(response.status_code)
        print(response.text)