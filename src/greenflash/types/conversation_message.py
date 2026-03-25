# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ConversationMessage"]


class ConversationMessage(BaseModel):
    content: str
    """Message content."""

    role: str
    """Message role (e.g. "user", "assistant")."""

    timestamp: Optional[datetime] = None
    """When the message was sent (ISO 8601)."""
