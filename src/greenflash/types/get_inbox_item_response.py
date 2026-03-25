# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .trigger_detail import TriggerDetail
from .analysis_scores import AnalysisScores
from .participant_info import ParticipantInfo
from .conversation_message import ConversationMessage

__all__ = ["GetInboxItemResponse"]


class GetInboxItemResponse(BaseModel):
    analysis: Optional[AnalysisScores] = None
    """Analysis scores for this conversation."""

    conversation_id: str = FieldInfo(alias="conversationId")
    """The conversation ID."""

    keywords: Optional[List[str]] = None
    """Keywords extracted from the conversation."""

    message_count: int = FieldInfo(alias="messageCount")
    """Number of chat messages in the conversation."""

    messages: List[ConversationMessage]
    """Conversation messages."""

    participant: Optional[ParticipantInfo] = None
    """Participant information."""

    review_status: Literal["unreviewed", "reviewed", "dismissed"] = FieldInfo(alias="reviewStatus")
    """Current review status."""

    summary: Optional[str] = None
    """AI-generated summary of the conversation."""

    timestamp: datetime
    """When the inbox item was created (ISO 8601)."""

    topic: Optional[str] = None
    """Main topic of the conversation."""

    triggers: List[TriggerDetail]
    """All triggers associated with this conversation."""

    trigger_type: Optional[str] = FieldInfo(alias="triggerType", default=None)
    """Primary trigger type that flagged this conversation."""
