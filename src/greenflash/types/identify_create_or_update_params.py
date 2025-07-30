# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IdentifyCreateOrUpdateParams"]


class IdentifyCreateOrUpdateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """Your unique identifier for the user.

    Use this same ID in other API calls to reference this user.
    """

    anonymized: bool
    """Whether to anonymize the user's personal information. Defaults to false."""

    email: str
    """The user's email address."""

    metadata: Dict[str, object]
    """Additional data about the user (e.g., plan type, preferences)."""

    name: str
    """The user's full name."""

    phone: str
    """The user's phone number."""
