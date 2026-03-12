# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

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
    "SummaryBehavioralPattern",
    "SummaryEngagement",
    "SummaryProductAlignment",
    "SummarySignal",
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


class SummaryBehavioralPattern(BaseModel):
    evidence: str
    """Specific examples from conversations."""

    frequency: Literal["recurring", "occasional", "rare"]
    """How often this pattern appears."""

    pattern: str
    """What the participant consistently does."""


class SummaryEngagement(BaseModel):
    """Engagement profile."""

    description: str
    """Explanation of the engagement assessment."""

    level: Literal["power_user", "regular", "casual", "at_risk", "churning"]
    """Engagement level classification."""

    trajectory: Literal["growing", "stable", "declining"]
    """Engagement trend direction."""


class SummaryProductAlignment(BaseModel):
    """Product-specific observations (when business context is available)."""

    gaps: List[str]
    """Where the product isn't serving them."""

    strengths: List[str]
    """What's working well for this participant."""

    summary: str
    """How the participant relates to product goals."""


class SummarySignal(BaseModel):
    description: str
    """Evidence-based description."""

    priority: Literal["high", "medium", "low"]
    """Signal priority."""

    title: str
    """Short headline."""

    type: Literal["opportunity", "risk", "insight"]
    """Signal category."""


class Summary(BaseModel):
    """Structured participant profile summary."""

    behavioral_patterns: List[SummaryBehavioralPattern] = FieldInfo(alias="behavioralPatterns")
    """Behavioral patterns observed across conversations."""

    engagement: SummaryEngagement
    """Engagement profile."""

    methodology: str
    """Transparency about what data drove the analysis."""

    product_alignment: Optional[SummaryProductAlignment] = FieldInfo(alias="productAlignment", default=None)
    """Product-specific observations (when business context is available)."""

    profile_summary: str = FieldInfo(alias="profileSummary")
    """Executive summary of the participant."""

    signals: List[SummarySignal]
    """Key signals the product owner should know about."""


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
    """Structured participant profile summary."""

    total_conversations: float = FieldInfo(alias="totalConversations")
    """Total number of conversations analyzed."""

    keywords: Optional[List[Keyword]] = None
    """Keywords extracted (insights mode only)."""

    topics: Optional[List[Topic]] = None
    """Topics discussed (insights mode only)."""
