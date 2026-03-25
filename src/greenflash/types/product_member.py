# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductMember"]


class ProductMember(BaseModel):
    id: str
    """The member record ID."""

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)
    """Avatar URL of the member."""

    role: str
    """The member role."""

    user_id: str = FieldInfo(alias="userId")
    """The user ID."""
