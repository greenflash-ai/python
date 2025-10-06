# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RatingLogParams"]


class RatingLogParams(TypedDict, total=False):
    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """The Greenflash product ID to rate."""

    rating: Required[float]
    """The rating value. Must be between ratingMin and ratingMax (inclusive)."""

    rating_max: Required[Annotated[float, PropertyInfo(alias="ratingMax")]]
    """The maximum possible rating value (e.g., 5 for a 1-5 scale)."""

    rating_min: Required[Annotated[float, PropertyInfo(alias="ratingMin")]]
    """The minimum possible rating value (e.g., 1 for a 1-5 scale)."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The Greenflash conversation ID to rate.

    Either conversationId, externalConversationId, messageId, or externalMessageId
    must be provided.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your external conversation identifier to rate.

    Either conversationId, externalConversationId, messageId, or externalMessageId
    must be provided.
    """

    external_message_id: Annotated[str, PropertyInfo(alias="externalMessageId")]
    """Your external message identifier to rate.

    Either conversationId, externalConversationId, messageId, or externalMessageId
    must be provided.
    """

    feedback: str
    """Optional text feedback accompanying the rating."""

    message_id: Annotated[str, PropertyInfo(alias="messageId")]
    """The Greenflash message ID to rate.

    Either conversationId, externalConversationId, messageId, or externalMessageId
    must be provided.
    """

    rated_at: Annotated[Union[str, date], PropertyInfo(alias="ratedAt", format="iso8601")]
    """When the rating was given. Defaults to current time if not provided."""
