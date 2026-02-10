"""Хендлер команды /start."""

from app.utils.logger import get_logger

logger = get_logger(__name__)


async def cmd_start(update, context) -> None:
    """Обработка /start."""
    # TODO: приветствие, меню
    await update.message.reply_text("Привет! Я flatscanner-bot.")
