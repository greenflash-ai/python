# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IdentifyCreateOrUpdateParams"]


class IdentifyCreateOrUpdateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """Your unique identifier for the user.

    This is used to reference the user in other API calls.
    """

    anonymized: bool
    """Whether the user's personal information should be anonymized.

    Defaults to false for new users.
    """

    email: str
    """The user's email address. Must be a valid email format."""

    metadata: Dict[str, object]
    """Additional metadata associated with the user as key-value pairs."""

    name: str
    """The user's full name."""

    phone: str
    """The user's phone number."""
