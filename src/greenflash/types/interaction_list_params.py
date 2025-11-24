# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InteractionListParams"]


class InteractionListParams(TypedDict, total=False):
    limit: float
    """Maximum number of results to return."""

    offset: float
    """Offset for pagination."""

    page: float
    """Page number"""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Filter interactions by product ID."""

    version_id: Annotated[str, PropertyInfo(alias="versionId")]
    """Filter interactions by version ID."""
