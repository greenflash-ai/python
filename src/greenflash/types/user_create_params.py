# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """Your unique identifier for the user.

    Use this same ID in other API calls to reference this user.
    """

    anonymized: bool
    """Whether to anonymize the user's personal information. Defaults to false."""

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
