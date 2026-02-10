"""Хендлеры обратной связи."""

from app.utils.logger import get_logger

logger = get_logger(__name__)


async def cmd_feedback(update, context) -> None:
    """Приём обратной связи от пользователя."""
    # TODO: сохранение в БД / уведомление админу
    await update.message.reply_text("Спасибо за отзыв!")
