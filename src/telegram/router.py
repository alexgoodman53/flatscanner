"""FastAPI router for Telegram webhook ingress."""

import logging

from fastapi import APIRouter, HTTPException, Request

from src.telegram.dispatcher import route_update
from src.telegram.models import TelegramUpdate
from src.telegram.sender import send_message

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/telegram", tags=["telegram"])

_MSG_ANALYSING = (
    "Got it! I'm looking at the listing at {url} — I'll get back to you shortly."
)
_MSG_HELP = (
    "Please send a rental listing URL (e.g. an Airbnb link) and I'll analyse it for you."
)


@router.post("/webhook")
async def webhook(request: Request, update: TelegramUpdate) -> dict:
    """Receive a Telegram update and route it to the appropriate handler.

    Returns ``{"ok": true}`` in all cases so Telegram stops retrying.

    If ``Settings.telegram_webhook_secret`` is set the request must carry a
    matching ``X-Telegram-Bot-Api-Secret-Token`` header; otherwise 403 is
    returned before the update is processed.
    """
    settings = request.app.state.settings

    if settings.telegram_webhook_secret:
        incoming_secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token", "")
        if incoming_secret != settings.telegram_webhook_secret:
            raise HTTPException(status_code=403, detail="Forbidden")

    decision = route_update(update)

    if decision["action"] == "ignore":
        return {"ok": True}

    if decision["action"] == "analyse":
        text = _MSG_ANALYSING.format(url=decision["url"])
    else:
        text = _MSG_HELP

    try:
        await send_message(settings.telegram_bot_token, decision["chat_id"], text)
    except Exception:
        logger.exception("send_message failed for chat_id=%s", decision["chat_id"])
        raise HTTPException(status_code=502, detail="Failed to deliver reply to Telegram")
    return {"ok": True}
