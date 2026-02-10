"""Конфигурация приложения."""

import os
from pathlib import Path


def _env(key: str, default: str = "") -> str:
    return os.getenv(key, default).strip()


# Telegram
BOT_TOKEN = _env("BOT_TOKEN")
WEBHOOK_URL = _env("WEBHOOK_URL", "")

# Database
DATABASE_URL = _env("DATABASE_URL", "sqlite:///./flatscanner.db")

# R2 / S3
R2_ACCESS_KEY_ID = _env("R2_ACCESS_KEY_ID", "")
R2_SECRET_ACCESS_KEY = _env("R2_SECRET_ACCESS_KEY", "")
R2_BUCKET_NAME = _env("R2_BUCKET_NAME", "")
R2_ENDPOINT_URL = _env("R2_ENDPOINT_URL", "")

# AI
AI_API_KEY = _env("AI_API_KEY", "")
AI_BASE_URL = _env("AI_BASE_URL", "")

# Payments
PAYMENTS_PROVIDER_TOKEN = _env("PAYMENTS_PROVIDER_TOKEN", "")

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
