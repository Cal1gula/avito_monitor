# 📱 Avito Monitor

Telegram-бот для мониторинга новых объявлений на Avito.

## Возможности

- 🔍 Мониторинг нескольких поисковых запросов
- 💰 Фильтр по максимальной цене
- 📈 Отслеживание изменения цен
- 📲 Уведомления в Telegram
- 💾 Хранение объявлений в SQLite
- 📊 Экспорт новых объявлений в Excel
- 📝 Логирование работы

---

## Стек

- Python 3
- Playwright
- SQLite
- OpenPyXL
- Telegram Bot API

---

## Установка

```bash
git clone https://github.com/Cal1gula/avito_monitor.git
cd avito_monitor

pip install -r requirements.txt
playwright install
```

Создать файл `.env`

```
BOT_TOKEN=YOUR_TOKEN
CHAT_ID=YOUR_CHAT_ID
```

Запуск

```bash
python monitor.py
```

---

## Структура проекта

```
avito_monitor/
│
├── avito_parser.py
├── database.py
├── monitor.py
├── telegram_sender.py
├── excel_logger.py
├── price_logger.py
├── logger.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
└── data/
```

---

## Автор

GitHub: https://github.com/Cal1gula
