# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OrganizationListParams"]


class OrganizationListParams(TypedDict, total=False):
    limit: float
    """Maximum number of results to return."""

    offset: float
    """Offset for pagination."""

    page: float
    """Page number (used to derive offset = (page-1)\\**limit)."""
