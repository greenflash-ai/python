# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GetSegmentAnalyticsResponse",
    "AverageChangeInUserSentiment",
    "AverageCommercialIntent",
    "AverageFrustration",
    "AverageStruggle",
    "AverageUserSentiment",
    "HallucinationCount",
    "JailbreakCount",
    "Keyword",
    "ModelBiasCount",
    "ModelToxicityCount",
    "TopicGroup",
    "Topic",
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
    """Average sentiment across all conversations."""

    label: str

    score: float


class HallucinationCount(BaseModel):
    """Number of hallucinations detected."""

    percentage: float

    total: float


class JailbreakCount(BaseModel):
    """Number of jailbreak attempts detected."""

    percentage: float

    total: float


class Keyword(BaseModel):
    count: float

    name: str


class ModelBiasCount(BaseModel):
    """Number of model bias detections."""

    percentage: float

    total: float


class ModelToxicityCount(BaseModel):
    """Number of model toxicity detections."""

    percentage: float

    total: float


class TopicGroup(BaseModel):
    count: float

    name: str


class Topic(BaseModel):
    count: float

    name: str


class UserBiasCount(BaseModel):
    """Number of user bias detections."""

    percentage: float

    total: float


class UserToxicityCount(BaseModel):
    """Number of user toxicity detections."""

    percentage: float

    total: float


class GetSegmentAnalyticsResponse(BaseModel):
    average_change_in_user_sentiment: AverageChangeInUserSentiment = FieldInfo(alias="averageChangeInUserSentiment")
    """Average change in user sentiment."""

    average_commercial_intent: AverageCommercialIntent = FieldInfo(alias="averageCommercialIntent")
    """Average commercial intent."""

    average_frustration: AverageFrustration = FieldInfo(alias="averageFrustration")
    """Average frustration level."""

    average_struggle: AverageStruggle = FieldInfo(alias="averageStruggle")
    """Average struggle level."""

    average_user_sentiment: AverageUserSentiment = FieldInfo(alias="averageUserSentiment")
    """Average sentiment across all conversations."""

    hallucination_count: HallucinationCount = FieldInfo(alias="hallucinationCount")
    """Number of hallucinations detected."""

    jailbreak_count: JailbreakCount = FieldInfo(alias="jailbreakCount")
    """Number of jailbreak attempts detected."""

    keywords: List[Keyword]
    """Keywords extracted from conversations."""

    api_model_bias_count: ModelBiasCount = FieldInfo(alias="modelBiasCount")
    """Number of model bias detections."""

    api_model_toxicity_count: ModelToxicityCount = FieldInfo(alias="modelToxicityCount")
    """Number of model toxicity detections."""

    participant_count: float = FieldInfo(alias="participantCount")
    """Total number of participants in the segment."""

    summary: Optional[Dict[str, object]] = None
    """LLM-generated summary of the segment."""

    topic_groups: List[TopicGroup] = FieldInfo(alias="topicGroups")
    """Topic groups across conversations."""

    topics: List[Topic]
    """Topics discussed across conversations."""

    total_conversations: float = FieldInfo(alias="totalConversations")
    """Total number of conversations in the segment."""

    user_bias_count: UserBiasCount = FieldInfo(alias="userBiasCount")
    """Number of user bias detections."""

    user_toxicity_count: UserToxicityCount = FieldInfo(alias="userToxicityCount")
    """Number of user toxicity detections."""

    average_conversation_quality_index: Optional[float] = FieldInfo(
        alias="averageConversationQualityIndex", default=None
    )
    """Average conversation quality index."""

    average_conversation_rating: Optional[float] = FieldInfo(alias="averageConversationRating", default=None)
    """Average conversation rating."""
