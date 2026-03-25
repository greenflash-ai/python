# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GetModelAnalyticsResponse",
    "AverageChangeInUserSentiment",
    "AverageCommercialIntent",
    "AverageFrustration",
    "AverageStruggle",
    "AverageUserSentiment",
    "DataPoint",
    "HallucinationCount",
    "JailbreakCount",
    "ModelBiasCount",
    "ModelToxicityCount",
    "Recommendations",
    "RecommendationsDetectedIssue",
    "RecommendationsRecommendation",
    "RecommendationsRecommendationEvidence",
    "RecommendationsRecommendationRationale",
    "UserBiasCount",
    "UserToxicityCount",
]


class AverageChangeInUserSentiment(BaseModel):
    """Average change in user sentiment."""

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
    """Average user sentiment."""

    label: str

    score: float


class DataPoint(BaseModel):
    avg_conversation_quality_index: Optional[float] = FieldInfo(alias="avgConversationQualityIndex", default=None)
    """Average conversation quality index."""

    avg_friction_score: Optional[float] = FieldInfo(alias="avgFrictionScore", default=None)
    """Average friction score."""

    avg_growth_score: Optional[float] = FieldInfo(alias="avgGrowthScore", default=None)
    """Average growth score."""

    avg_safety_score: Optional[float] = FieldInfo(alias="avgSafetyScore", default=None)
    """Average safety score."""

    avg_satisfaction_score: Optional[float] = FieldInfo(alias="avgSatisfactionScore", default=None)
    """Average satisfaction score."""

    conversation_count: float = FieldInfo(alias="conversationCount")
    """Number of conversations."""

    date: datetime
    """Data point date."""

    message_count: float = FieldInfo(alias="messageCount")
    """Number of messages."""


class HallucinationCount(BaseModel):
    """Hallucination detection counts."""

    percentage: float

    total: float


class JailbreakCount(BaseModel):
    """Jailbreak detection counts."""

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


class RecommendationsDetectedIssue(BaseModel):
    id: str

    severity: Literal["critical", "warning", "info"]

    title: str


class RecommendationsRecommendationEvidence(BaseModel):
    example_snippets: List[str] = FieldInfo(alias="exampleSnippets")


class RecommendationsRecommendationRationale(BaseModel):
    observed_pattern: str = FieldInfo(alias="observedPattern")

    why_this_matters: str = FieldInfo(alias="whyThisMatters")

    tradeoff: Optional[str] = None


class RecommendationsRecommendation(BaseModel):
    action: str

    category: Literal["model_switch", "cost_optimization", "use_case_fit", "prompt_optimization_link"]

    evidence: RecommendationsRecommendationEvidence

    expected_impact: List[str] = FieldInfo(alias="expectedImpact")

    priority: Literal["high", "medium", "low"]

    rationale: RecommendationsRecommendationRationale

    title: str


class Recommendations(BaseModel):
    """LLM-generated recommendations and health assessment."""

    detected_issues: List[RecommendationsDetectedIssue] = FieldInfo(alias="detectedIssues")
    """Issues detected via rules-based analysis."""

    health_level: Literal["healthy", "needs_attention", "critical"] = FieldInfo(alias="healthLevel")
    """Overall health level."""

    recommendations: List[RecommendationsRecommendation]
    """Actionable recommendations."""

    strengths: List[str]
    """Identified model strengths."""

    summary: str
    """Overall summary of model health."""


class UserBiasCount(BaseModel):
    """User bias detection counts."""

    percentage: float

    total: float


class UserToxicityCount(BaseModel):
    """User toxicity detection counts."""

    percentage: float

    total: float


class GetModelAnalyticsResponse(BaseModel):
    average_change_in_user_sentiment: Optional[AverageChangeInUserSentiment] = FieldInfo(
        alias="averageChangeInUserSentiment", default=None
    )
    """Average change in user sentiment."""

    average_commercial_intent: Optional[AverageCommercialIntent] = FieldInfo(
        alias="averageCommercialIntent", default=None
    )
    """Average commercial intent."""

    average_conversation_rating: Optional[float] = FieldInfo(alias="averageConversationRating", default=None)
    """Average conversation rating."""

    average_frustration: Optional[AverageFrustration] = FieldInfo(alias="averageFrustration", default=None)
    """Average frustration level."""

    average_struggle: Optional[AverageStruggle] = FieldInfo(alias="averageStruggle", default=None)
    """Average struggle level."""

    average_user_sentiment: Optional[AverageUserSentiment] = FieldInfo(alias="averageUserSentiment", default=None)
    """Average user sentiment."""

    avg_conversation_quality_index: Optional[float] = FieldInfo(alias="avgConversationQualityIndex", default=None)
    """Average conversation quality index."""

    avg_friction_score: Optional[float] = FieldInfo(alias="avgFrictionScore", default=None)
    """Average friction score."""

    avg_growth_score: Optional[float] = FieldInfo(alias="avgGrowthScore", default=None)
    """Average growth score."""

    avg_safety_score: Optional[float] = FieldInfo(alias="avgSafetyScore", default=None)
    """Average safety score."""

    avg_satisfaction_score: Optional[float] = FieldInfo(alias="avgSatisfactionScore", default=None)
    """Average satisfaction score."""

    conversation_count: float = FieldInfo(alias="conversationCount")
    """Total conversation count."""

    data_points: List[DataPoint] = FieldInfo(alias="dataPoints")
    """Time-series data points for the requested period."""

    hallucination_count: Optional[HallucinationCount] = FieldInfo(alias="hallucinationCount", default=None)
    """Hallucination detection counts."""

    jailbreak_count: Optional[JailbreakCount] = FieldInfo(alias="jailbreakCount", default=None)
    """Jailbreak detection counts."""

    message_count: float = FieldInfo(alias="messageCount")
    """Total message count."""

    api_model_bias_count: Optional[ModelBiasCount] = FieldInfo(alias="modelBiasCount", default=None)
    """Model bias detection counts."""

    api_model_toxicity_count: Optional[ModelToxicityCount] = FieldInfo(alias="modelToxicityCount", default=None)
    """Model toxicity detection counts."""

    recommendations: Optional[Recommendations] = None
    """LLM-generated recommendations and health assessment."""

    user_bias_count: Optional[UserBiasCount] = FieldInfo(alias="userBiasCount", default=None)
    """User bias detection counts."""

    user_toxicity_count: Optional[UserToxicityCount] = FieldInfo(alias="userToxicityCount", default=None)
    """User toxicity detection counts."""
