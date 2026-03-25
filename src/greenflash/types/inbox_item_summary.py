# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InboxItemSummary"]


class InboxItemSummary(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")
    """The conversation ID."""

    message_count: int = FieldInfo(alias="messageCount")
    """Number of chat messages in the conversation."""

    review_status: Literal["unreviewed", "reviewed", "dismissed"] = FieldInfo(alias="reviewStatus")
    """Current review status."""

    timestamp: datetime
    """When the inbox item was created (ISO 8601)."""

    topic: Optional[str] = None
    """Main topic of the conversation."""

    trigger_type: Optional[str] = FieldInfo(alias="triggerType", default=None)
    """Primary trigger type that flagged this conversation."""
