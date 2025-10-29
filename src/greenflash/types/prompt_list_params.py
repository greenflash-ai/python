# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromptListParams"]


class PromptListParams(TypedDict, total=False):
    active_only: Annotated[bool, PropertyInfo(alias="activeOnly")]
    """Filter to only show prompts that are part of active versions.

    When true, only returns prompts associated with versions where isActive=true.
    """

    include_archived: Annotated[bool, PropertyInfo(alias="includeArchived")]
    """Include archived prompts."""

    limit: float
    """Page size limit (cursor-based pagination).

    Use either limit/cursor OR page/pageSize, not both.
    """

    page: float
    """Page number (page-based pagination).

    Use either page/pageSize OR limit/cursor, not both.
    """

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]
    """Number of items per page (page-based pagination).

    Use either page/pageSize OR limit/cursor, not both.
    """

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Filter prompts by product ID."""

    version_id: Annotated[str, PropertyInfo(alias="versionId")]
    """Filter prompts by specific version ID."""
