import time

from avito_parser import AvitoParser
from database import Database
from telegram_sender import TelegramSender
from excel_logger import ExcelLogger
from price_logger import PriceLogger
from logger import logger

from config import CHECK_INTERVAL, MAX_PRICE


parser = AvitoParser()
db = Database()
sender = TelegramSender()
excel = ExcelLogger()
price_logger = PriceLogger()

print("Монитор запущен...")
logger.info("Монитор запущен")


while True:

    try:

        start_time = time.time()

        new_items = 0
        changed_prices = 0
        skipped_price = 0

        items = parser.parse()
        total_items = len(items)

        for item in items:

            if MAX_PRICE is not None and item["price"] > MAX_PRICE:
                skipped_price += 1
                continue

            if not db.exists(item["id"]):

                logger.info(
                    f'Новое объявление: {item["title"]} | {item["price"]} ₽'
                )

                db.add(item)

                excel.add_item(item)

                sender.send_new_item(item)

                new_items += 1

            else:

                old = db.get(item["id"])

                if old is None:
                    continue

                if old["price"] != item["price"]:

                    logger.info(
                        f'Цена изменилась: {old["price"]} -> {item["price"]}'
                    )

                    sender.send_price_changed(
                        item,
                        old["price"]
                    )

                    price_logger.add(
                        item,
                        old["price"]
                    )

                    db.update(item)

                    changed_prices += 1

        elapsed = round(time.time() - start_time, 1)

        print("\n" + "=" * 60)
        print("ПРОВЕРКА ЗАВЕРШЕНА")
        print("=" * 60)
        print(f"Всего объявлений:      {total_items}")
        print(f"Новых:                 {new_items}")
        print(f"Изменений цены:        {changed_prices}")
        print(f"Пропущено по цене:     {skipped_price}")
        print(f"Время проверки:        {elapsed} сек")
        print(f"Следующая проверка:    через {CHECK_INTERVAL} сек")
        print("=" * 60 + "\n")

        logger.info(
            f"Проверка завершена | "
            f"Всего: {total_items} | "
            f"Новых: {new_items} | "
            f"Изменений цены: {changed_prices}"
        )

        time.sleep(CHECK_INTERVAL)

    except Exception as e:

        logger.exception(e)

        print("Ошибка:", e)

        time.sleep(60)