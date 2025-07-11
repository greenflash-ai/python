# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RatingLogParams"]


class RatingLogParams(TypedDict, total=False):
    rating: Required[float]

    rating_max: Required[Annotated[float, PropertyInfo(alias="ratingMax")]]

    rating_min: Required[Annotated[float, PropertyInfo(alias="ratingMin")]]

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]

    feedback: str

    message_id: Annotated[str, PropertyInfo(alias="messageId")]

    rated_at: Annotated[Union[str, datetime], PropertyInfo(alias="ratedAt", format="iso8601")]
