# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ModelProductUsage"]


class ModelProductUsage(BaseModel):
    id: str
    """The product ID."""

    conversation_count: float = FieldInfo(alias="conversationCount")
    """Number of conversations in this product."""

    icon: Optional[str] = None
    """Product icon."""

    name: str
    """Product name."""
