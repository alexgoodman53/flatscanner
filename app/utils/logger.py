"""Логирование."""

import logging
import sys


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Настроенный логгер."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        h = logging.StreamHandler(sys.stdout)
        h.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
        logger.addHandler(h)
    return logger
