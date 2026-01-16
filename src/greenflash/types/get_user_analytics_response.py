# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GetUserAnalyticsResponse",
    "AverageChangeInUserSentiment",
    "AverageCommercialIntent",
    "AverageFrustration",
    "AverageStruggle",
    "AverageUserSentiment",
    "Summary",
    "Keyword",
    "Topic",
]


class AverageChangeInUserSentiment(BaseModel):
    """Distribution of sentiment changes."""

    label: str

    score: float


class AverageCommercialIntent(BaseModel):
    """Average commercial intent."""

    label: str

    score: float


class AverageFrustration(BaseModel):
    """Average frustration level."""

    label: str

    score: float


class AverageStruggle(BaseModel):
    """Average struggle level."""

    label: str

    score: float


class AverageUserSentiment(BaseModel):
    """Average sentiment across all conversations."""

    label: str

    score: float


class Summary(BaseModel):
    """Summary of the user analytics."""

    analysis: str

    reason: str


class Keyword(BaseModel):
    count: float

    name: str


class Topic(BaseModel):
    count: float

    name: str


class GetUserAnalyticsResponse(BaseModel):
    average_change_in_user_sentiment: AverageChangeInUserSentiment = FieldInfo(alias="averageChangeInUserSentiment")
    """Distribution of sentiment changes."""

    average_commercial_intent: AverageCommercialIntent = FieldInfo(alias="averageCommercialIntent")
    """Average commercial intent."""

    average_conversation_quality_index: Optional[float] = FieldInfo(
        alias="averageConversationQualityIndex", default=None
    )
    """Average conversation quality index."""

    average_conversation_rating: Optional[float] = FieldInfo(alias="averageConversationRating", default=None)
    """Average conversation rating."""

    average_frustration: AverageFrustration = FieldInfo(alias="averageFrustration")
    """Average frustration level."""

    average_struggle: AverageStruggle = FieldInfo(alias="averageStruggle")
    """Average struggle level."""

    average_user_sentiment: AverageUserSentiment = FieldInfo(alias="averageUserSentiment")
    """Average sentiment across all conversations."""

    summary: Optional[Summary] = None
    """Summary of the user analytics."""

    total_conversations: float = FieldInfo(alias="totalConversations")
    """Total number of conversations analyzed."""

    keywords: Optional[List[Keyword]] = None
    """Keywords extracted (insights mode only)."""

    topics: Optional[List[Topic]] = None
    """Topics discussed (insights mode only)."""
