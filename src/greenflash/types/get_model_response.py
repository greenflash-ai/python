# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .model_product_usage import ModelProductUsage

__all__ = ["GetModelResponse"]


class GetModelResponse(BaseModel):
    id: str
    """The model ID."""

    canonical_id: str = FieldInfo(alias="canonicalId")
    """The canonical model identifier."""

    coding_index: Optional[float] = FieldInfo(alias="codingIndex", default=None)
    """Coding benchmark index."""

    context_window: Optional[float] = FieldInfo(alias="contextWindow", default=None)
    """Context window size."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the model was created."""

    description: Optional[str] = None
    """Model description."""

    display_name: str = FieldInfo(alias="displayName")
    """Human-readable model name."""

    expiration_date: Optional[datetime] = FieldInfo(alias="expirationDate", default=None)
    """When the model expires, if applicable."""

    family: Optional[str] = None
    """Model family grouping."""

    gpqa: Optional[float] = None
    """GPQA benchmark score."""

    input_cost_per1k: Optional[float] = FieldInfo(alias="inputCostPer1k", default=None)
    """Cost per 1,000 input tokens."""

    input_modalities: Optional[List[str]] = FieldInfo(alias="inputModalities", default=None)
    """Supported input modalities."""

    intelligence_index: Optional[float] = FieldInfo(alias="intelligenceIndex", default=None)
    """Intelligence benchmark index."""

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
    """When the model was last used."""

    math_index: Optional[float] = FieldInfo(alias="mathIndex", default=None)
    """Math benchmark index."""

    mmlu_pro: Optional[float] = FieldInfo(alias="mmluPro", default=None)
    """MMLU-Pro benchmark score."""

    output_cost_per1k: Optional[float] = FieldInfo(alias="outputCostPer1k", default=None)
    """Cost per 1,000 output tokens."""

    output_modalities: Optional[List[str]] = FieldInfo(alias="outputModalities", default=None)
    """Supported output modalities."""

    products: List[ModelProductUsage]
    """Products using this model."""

    provider: str
    """Model provider (e.g. OpenAI, Anthropic)."""

    source: str
    """Model data source."""

    supported_parameters: Optional[List[str]] = FieldInfo(alias="supportedParameters", default=None)
    """Supported generation parameters."""

    usage_count: float = FieldInfo(alias="usageCount")
    """Number of conversations using this model."""
