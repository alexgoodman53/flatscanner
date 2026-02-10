"""Хендлеры регистрации пользователя."""

from app.utils.logger import get_logger

logger = get_logger(__name__)


async def cmd_register(update, context) -> None:
    """Регистрация / привязка пользователя."""
    # TODO: проверка подписки, сохранение в БД
    await update.message.reply_text("Регистрация (в разработке).")
