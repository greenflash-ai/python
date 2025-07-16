# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageItemParam"]


class MessageItemParam(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[Literal["user", "assistant", "system"]]
    """The role of the message sender.

    Must be one of: 'user', 'assistant', or 'system'.
    """

    content_type: Annotated[Literal["text", "image", "audio", "json"], PropertyInfo(alias="contentType")]
    """The type of content.

    One of: 'text', 'image', 'audio', or 'json'. Defaults to 'text'.
    """

    context: str
    """Additional context for the message."""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """When this message was created."""

    message_index: Annotated[float, PropertyInfo(alias="messageIndex")]
    """The index of the message within the turn.

    Inferred based on the location in the array and previous records, but can be
    overridden here.
    """

    metadata: Dict[str, object]
    """Additional metadata for the message."""

    tokens: float
    """The number of tokens in the message."""
