"""Хранилище файлов (R2 / S3)."""

from app.utils.logger import get_logger

logger = get_logger(__name__)


async def upload_file(key: str, data: bytes, content_type: str | None = None) -> str | None:
    """Загрузить файл в R2/S3. Возвращает публичный URL или None."""
    # TODO: boto3 или aioboto3 для R2
    return None


async def get_file_url(key: str) -> str | None:
    """Получить URL файла по ключу."""
    return None
