"""Платежи (Telegram Payments / внешний провайдер)."""

from app.utils.logger import get_logger

logger = get_logger(__name__)


async def create_invoice(user_id: int, amount: int, description: str) -> str | None:
    """Создать счёт для оплаты. Возвращает invoice_link или None."""
    # TODO: интеграция с платежами
    return None


async def check_payment(payment_id: str) -> bool:
    """Проверить статус платежа."""
    return False
