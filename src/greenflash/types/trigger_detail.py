# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TriggerDetail"]


class TriggerDetail(BaseModel):
    confidence: Optional[float] = None
    """Confidence score of the trigger."""

    reason: Optional[str] = None
    """Human-readable reason."""

    severity: int
    """Severity level (1-5)."""

    source: Optional[str] = None
    """Source key of the trigger."""

    trigger_type: str = FieldInfo(alias="triggerType")
    """Type of trigger."""
