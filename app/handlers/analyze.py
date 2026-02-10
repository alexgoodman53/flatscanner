"""Хендлеры анализа объявлений (ссылки)."""

from app.utils.logger import get_logger

logger = get_logger(__name__)


async def cmd_analyze(update, context) -> None:
    """Анализ ссылки на объявление."""
    # TODO: парсинг ссылки, вызов parser + ai, ответ пользователю
    await update.message.reply_text("Пришлите ссылку на объявление для анализа.")
