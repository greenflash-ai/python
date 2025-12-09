# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GetInteractionAnalyticsResponse",
    "AverageUserSentiment",
    "ChangeInUserSentiment",
    "CommercialIntent",
    "Frustration",
    "Struggle",
]


class AverageUserSentiment(BaseModel):
    """Average sentiment across user messages."""

    label: str

    score: float


class ChangeInUserSentiment(BaseModel):
    """How sentiment changed during the interaction."""

    label: str

    score: float


class CommercialIntent(BaseModel):
    """Commercial intent detected."""

    primary_signal: str = FieldInfo(alias="primarySignal")

    score: float


class Frustration(BaseModel):
    """Frustration level detected."""

    label: str

    score: float


class Struggle(BaseModel):
    """Struggle level detected."""

    label: str

    score: float


class GetInteractionAnalyticsResponse(BaseModel):
    average_user_sentiment: AverageUserSentiment = FieldInfo(alias="averageUserSentiment")
    """Average sentiment across user messages."""

    change_in_user_sentiment: ChangeInUserSentiment = FieldInfo(alias="changeInUserSentiment")
    """How sentiment changed during the interaction."""

    commercial_intent: CommercialIntent = FieldInfo(alias="commercialIntent")
    """Commercial intent detected."""

    conversation_quality_index: Optional[float] = FieldInfo(alias="conversationQualityIndex", default=None)
    """Quality index score for the interaction."""

    frustration: Frustration
    """Frustration level detected."""

    message_count: float = FieldInfo(alias="messageCount")
    """Number of messages in the interaction."""

    most_common_user_emotion: str = FieldInfo(alias="mostCommonUserEmotion")
    """Most common emotion expressed by user."""

    rating: Optional[float] = None
    """User rating for this interaction."""

    struggle: Struggle
    """Struggle level detected."""

    summary: str
    """Summary of the interaction."""

    topic: str
    """Main topic discussed."""

    keywords: Optional[List[str]] = None
    """Keywords extracted (insights mode only)."""
