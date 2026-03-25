# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GetProductAnalyticsResponse",
    "AverageChangeInUserSentiment",
    "AverageCommercialIntent",
    "AverageFrustration",
    "AverageStruggle",
    "AverageUserSentiment",
    "DissatisfactionTheme",
    "HallucinationCount",
    "JailbreakCount",
    "ModelBiasCount",
    "ModelToxicityCount",
    "PillarScores",
    "RootCauseMix",
    "TopFailingTool",
    "TopicGroup",
    "Topic",
    "UserBiasCount",
    "UserToxicityCount",
]


class AverageChangeInUserSentiment(BaseModel):
    """Average change in user sentiment during conversations."""

    label: str

    score: float


class AverageCommercialIntent(BaseModel):
    """Average commercial intent detected."""

    label: str

    score: float


class AverageFrustration(BaseModel):
    """Average frustration level detected."""

    label: str

    score: float


class AverageStruggle(BaseModel):
    """Average struggle level detected."""

    label: str

    score: float


class AverageUserSentiment(BaseModel):
    """Average user sentiment across conversations."""

    label: str

    score: float


class DissatisfactionTheme(BaseModel):
    avg_cqi: Optional[float] = FieldInfo(alias="avgCqi", default=None)

    avg_frustration: float = FieldInfo(alias="avgFrustration")

    avg_struggle: float = FieldInfo(alias="avgStruggle")

    count: float

    topic_canonical: str = FieldInfo(alias="topicCanonical")

    topic_group: str = FieldInfo(alias="topicGroup")


class HallucinationCount(BaseModel):
    """Hallucination detection counts."""

    percentage: float

    total: float


class JailbreakCount(BaseModel):
    """Jailbreak attempt counts."""

    percentage: float

    total: float


class ModelBiasCount(BaseModel):
    """Model bias detection counts."""

    percentage: float

    total: float


class ModelToxicityCount(BaseModel):
    """Model toxicity detection counts."""

    percentage: float

    total: float


class PillarScores(BaseModel):
    """Quality pillar scores."""

    friction: float
    """Friction pillar score (0-1)."""

    growth: float
    """Growth pillar score (0-1)."""

    safety: float
    """Safety pillar score (0-1)."""

    satisfaction: float
    """Satisfaction pillar score (0-1)."""


class RootCauseMix(BaseModel):
    avg_confidence: float = FieldInfo(alias="avgConfidence")

    cause: str

    count: float

    source: str


class TopFailingTool(BaseModel):
    failure_count: float = FieldInfo(alias="failureCount")

    failure_rate: float = FieldInfo(alias="failureRate")

    tool_name: str = FieldInfo(alias="toolName")

    total_calls: float = FieldInfo(alias="totalCalls")


class TopicGroup(BaseModel):
    count: float

    name: str


class Topic(BaseModel):
    count: float

    name: str


class UserBiasCount(BaseModel):
    """User bias detection counts."""

    percentage: float

    total: float


class UserToxicityCount(BaseModel):
    """User toxicity detection counts."""

    percentage: float

    total: float


class GetProductAnalyticsResponse(BaseModel):
    average_change_in_user_sentiment: AverageChangeInUserSentiment = FieldInfo(alias="averageChangeInUserSentiment")
    """Average change in user sentiment during conversations."""

    average_commercial_intent: AverageCommercialIntent = FieldInfo(alias="averageCommercialIntent")
    """Average commercial intent detected."""

    average_conversation_rating: Optional[float] = FieldInfo(alias="averageConversationRating", default=None)
    """Average conversation rating."""

    average_frustration: AverageFrustration = FieldInfo(alias="averageFrustration")
    """Average frustration level detected."""

    average_struggle: AverageStruggle = FieldInfo(alias="averageStruggle")
    """Average struggle level detected."""

    average_user_sentiment: AverageUserSentiment = FieldInfo(alias="averageUserSentiment")
    """Average user sentiment across conversations."""

    dissatisfaction_themes: List[DissatisfactionTheme] = FieldInfo(alias="dissatisfactionThemes")
    """Dissatisfaction themes by topic."""

    hallucination_count: HallucinationCount = FieldInfo(alias="hallucinationCount")
    """Hallucination detection counts."""

    jailbreak_count: JailbreakCount = FieldInfo(alias="jailbreakCount")
    """Jailbreak attempt counts."""

    keywords: List[str]
    """Extracted keywords."""

    api_model_bias_count: ModelBiasCount = FieldInfo(alias="modelBiasCount")
    """Model bias detection counts."""

    api_model_toxicity_count: ModelToxicityCount = FieldInfo(alias="modelToxicityCount")
    """Model toxicity detection counts."""

    pillar_scores: Optional[PillarScores] = FieldInfo(alias="pillarScores", default=None)
    """Quality pillar scores."""

    product_quality_index: Optional[float] = FieldInfo(alias="productQualityIndex", default=None)
    """Product Quality Index score."""

    rating_count: float = FieldInfo(alias="ratingCount")
    """Number of conversations with a rating."""

    root_cause_mix: List[RootCauseMix] = FieldInfo(alias="rootCauseMix")
    """Root cause breakdown."""

    top_failing_tools: List[TopFailingTool] = FieldInfo(alias="topFailingTools")
    """Top failing tools by failure rate."""

    topic_groups: List[TopicGroup] = FieldInfo(alias="topicGroups")
    """Topic group aggregations."""

    topics: List[Topic]
    """Top topics discussed."""

    user_bias_count: UserBiasCount = FieldInfo(alias="userBiasCount")
    """User bias detection counts."""

    user_toxicity_count: UserToxicityCount = FieldInfo(alias="userToxicityCount")
    """User toxicity detection counts."""

    insights: Optional[object] = None
    """AI-generated insights."""
