# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RatingLogParams"]


class RatingLogParams(TypedDict, total=False):
    rating: Required[float]
    """The rating value. Must be between ratingMin and ratingMax (inclusive)."""

    rating_max: Required[Annotated[float, PropertyInfo(alias="ratingMax")]]
    """The maximum possible rating value (e.g., 5 for a 1-5 scale)."""

    rating_min: Required[Annotated[float, PropertyInfo(alias="ratingMin")]]
    """The minimum possible rating value (e.g., 1 for a 1-5 scale)."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The internal ID of the conversation to rate.

    Either conversationId, externalConversationId, or messageId must be provided.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your external identifier for the conversation to rate.

    Either conversationId, externalConversationId, or messageId must be provided.
    """

    feedback: str
    """Optional text feedback accompanying the rating."""

    message_id: Annotated[str, PropertyInfo(alias="messageId")]
    """The ID of a specific message to rate.

    Either conversationId, externalConversationId, or messageId must be provided.
    """

    rated_at: Annotated[str, PropertyInfo(alias="ratedAt")]
    """The timestamp when the rating was given.

    If not provided, the current time will be used.
    """
