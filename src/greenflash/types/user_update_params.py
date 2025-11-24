# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    anonymized: bool
    """Whether to anonymize the user's personal information."""

    email: str
    """The user's email address."""

    external_organization_id: Annotated[str, PropertyInfo(alias="externalOrganizationId")]
    """Your unique identifier for the organization this user belongs to.

    If provided, the user will be associated with this organization.
    """

    name: str
    """The user's full name."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """The Greenflash organization ID that the user belongs to."""

    phone: str
    """The user's phone number."""

    properties: Dict[str, object]
    """Additional data about the user (e.g., plan type, preferences)."""
