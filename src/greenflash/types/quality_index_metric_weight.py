# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["QualityIndexMetricWeight"]


class QualityIndexMetricWeight(BaseModel):
    description: str
    """Metric description."""

    key: str
    """The metric key."""

    name: str
    """Human-readable metric name."""

    weight: float
    """The metric weight (0-1)."""
