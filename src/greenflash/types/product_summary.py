# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductSummary"]


class ProductSummary(BaseModel):
    id: str
    """The product ID."""

    color: Optional[str] = None
    """Product color hex code."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the product was created (ISO 8601)."""

    icon: Optional[str] = None
    """Product icon identifier."""

    name: str
    """The product name."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the product was last updated (ISO 8601)."""
