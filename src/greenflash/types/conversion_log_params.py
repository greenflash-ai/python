# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversionLogParams"]


class ConversionLogParams(TypedDict, total=False):
    action: Required[str]
    """The type of conversion (e.g., "purchase", "signup", "upgrade")."""

    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """Your unique identifier for the user who completed the conversion."""

    value: Required[str]
    """The conversion value (interpretation depends on valueType)."""

    value_type: Required[Annotated[Literal["currency", "numeric", "text"], PropertyInfo(alias="valueType")]]
    """The type of value: currency (e.g., "$99.99"), numeric (e.g., "5"), or text."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The Greenflash conversation ID that led to this conversion."""

    converted_at: Annotated[str, PropertyInfo(alias="convertedAt")]
    """When the conversion occurred. Defaults to current time if not provided."""

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your external conversation identifier that led to this conversion."""

    metadata: Dict[str, object]
    """Additional data about the conversion."""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """The Greenflash product associated with this conversion."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The Greenflash project associated with this conversion."""
