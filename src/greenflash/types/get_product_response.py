# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .product_member import ProductMember
from .quality_index_metric_weight import QualityIndexMetricWeight

__all__ = ["GetProductResponse"]


class GetProductResponse(BaseModel):
    id: str
    """The product ID."""

    color: Optional[str] = None
    """Product color hex code."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the product was created (ISO 8601)."""

    description: Optional[str] = None
    """Product description."""

    icon: Optional[str] = None
    """Product icon identifier."""

    members: List[ProductMember]
    """Product team members."""

    name: str
    """The product name."""

    optimization_notes: Optional[str] = FieldInfo(alias="optimizationNotes", default=None)
    """AI optimization notes for the product."""

    quality_index_metric_weights: List[QualityIndexMetricWeight] = FieldInfo(alias="qualityIndexMetricWeights")
    """Quality index metric weight configuration."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the product was last updated (ISO 8601)."""

    user_privacy: str = FieldInfo(alias="userPrivacy")
    """User privacy setting."""
