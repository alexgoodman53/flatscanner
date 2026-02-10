# flatscanner-bot

Telegram-бот для анализа объявлений о недвижимости.

## Структура

- `app/main.py` — точка входа
- `app/config.py` — конфигурация из env
- `app/bot.py` — инициализация бота
- `app/handlers/` — команды (start, register, analyze, feedback)
- `app/services/` — парсер, ИИ, платежи, R2/S3
- `app/db/` — сессия и модели БД
- `app/utils/` — логгер и прочее

## Запуск

1. Скопировать `.env.example` в `.env` и заполнить `BOT_TOKEN`.
2. Установить зависимости: `pip install -r requirements.txt`
3. Запуск: `python -m app.main`
