"""Pytest fixtures (общие для тестов)."""

import pytest


@pytest.fixture
def sample_listing_url() -> str:
    """Пример ссылки на объявление."""
    return "https://example.com/listing/123"
