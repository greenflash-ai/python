# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationGetOrganizationAnalyticsParams"]


class OrganizationGetOrganizationAnalyticsParams(TypedDict, total=False):
    mode: Literal["simple", "insights"]
    """
    Analysis mode: "simple" returns only numeric aggregates (no rate limiting),
    "insights" includes topics, keywords, and recommendations (rate limited per
    tenant plan).
    """

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Filter analytics by product ID."""

    version_id: Annotated[str, PropertyInfo(alias="versionId")]
    """Filter analytics by version ID."""
