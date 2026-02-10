"""Telegram bot инициализация и запуск."""

from app.config import BOT_TOKEN
from app.utils.logger import get_logger

logger = get_logger(__name__)


def run_bot() -> None:
    """Запуск long polling бота."""
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не задан в окружении")
    # TODO: инициализация Application, регистрация handlers, запуск
    logger.info("Bot starting...")
