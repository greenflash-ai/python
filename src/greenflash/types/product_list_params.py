# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    page: float
    """Page number (default 1)."""

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]
    """Number of results per page (default 50, max 100)."""
