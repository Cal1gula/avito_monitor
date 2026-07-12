# Avito Monitor

Автоматический монитор объявлений Avito с уведомлениями в Telegram.

## Возможности

- Мониторинг сразу нескольких поисковых запросов
- Фильтрация по максимальной цене
- Отслеживание изменения цены
- Уведомления в Telegram
- История изменений цен
- Логирование
- Хранение объявлений в SQLite
- Экспорт новых объявлений в Excel
- Автоматическая работа по расписанию

## Стек

- Python 3.12
- Playwright
- SQLite
- OpenPyXL
- Telegram Bot API

## Структура проекта

```
avito_monitor_v2/

├── monitor.py
├── avito_parser.py
├── database.py
├── telegram_sender.py
├── excel_logger.py
├── price_logger.py
├── logger.py
├── config.py
├── requirements.txt
│
├── data/
│   ├── avito.db
│   ├── new_items.xlsx
│   └── price_history.xlsx
│
└── logs/
```

## Как установить

```bash
git clone https://github.com/USERNAME/avito_monitor.git

cd avito_monitor

pip install -r requirements.txt
```

## Настройка

В файле `config.py` необходимо указать:

- TOKEN Telegram-бота
- CHAT_ID
- поисковые ссылки Avito
- максимальную цену
- интервал проверки

## Запуск

```bash
python monitor.py
```

## Пример уведомления

```
📱 iPhone 15

💰 Цена: 39000 ₽

📍 Москва

🔗 https://www.avito.ru/...
```

## Возможности для развития

- Docker
- VPS
- Веб-интерфейс
- История цен в виде графиков
- Поддержка любых категорий Avito

## Автор

GitHub: [https://github.com/Cal1gula]