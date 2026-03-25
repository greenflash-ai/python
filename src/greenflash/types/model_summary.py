# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelSummary"]


class ModelSummary(BaseModel):
    id: str
    """The model ID."""

    canonical_id: str = FieldInfo(alias="canonicalId")
    """The canonical model identifier."""

    display_name: str = FieldInfo(alias="displayName")
    """Human-readable model name."""

    family: Optional[str] = None
    """Model family grouping."""

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)
    """When the model was last used."""

    provider: str
    """Model provider (e.g. OpenAI, Anthropic)."""

    usage_count: float = FieldInfo(alias="usageCount")
    """Number of conversations using this model."""
