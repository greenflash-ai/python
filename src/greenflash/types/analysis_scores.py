# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AnalysisScores", "Frustration", "Sentiment", "Struggle"]


class Frustration(BaseModel):
    """Frustration level detected."""

    label: str

    score: float


class Sentiment(BaseModel):
    """Average user sentiment."""

    label: str

    score: float


class Struggle(BaseModel):
    """Struggle level detected."""

    label: str

    score: float


class AnalysisScores(BaseModel):
    """Analysis scores for this conversation."""

    frustration: Optional[Frustration] = None
    """Frustration level detected."""

    quality_index: Optional[float] = FieldInfo(alias="qualityIndex", default=None)
    """Conversation quality index score."""

    sentiment: Optional[Sentiment] = None
    """Average user sentiment."""

    struggle: Optional[Struggle] = None
    """Struggle level detected."""
