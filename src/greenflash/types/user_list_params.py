# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    limit: float
    """Maximum number of results to return."""

    offset: float
    """Offset for pagination."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """Filter users by organization ID."""

    page: float
    """Page number (used to derive offset = (page-1)\\**limit)."""
