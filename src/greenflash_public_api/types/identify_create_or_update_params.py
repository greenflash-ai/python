# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IdentifyCreateOrUpdateParams"]


class IdentifyCreateOrUpdateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]

    anonymized: bool

    email: str

    metadata: Dict[str, object]

    name: str

    phone: str
