# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SegmentGetSegmentAnalyticsParams"]


class SegmentGetSegmentAnalyticsParams(TypedDict, total=False):
    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Filter analytics by product ID."""

    version_id: Annotated[str, PropertyInfo(alias="versionId")]
    """Filter analytics by version ID."""
