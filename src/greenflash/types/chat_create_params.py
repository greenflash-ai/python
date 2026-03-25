# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ChatCreateParams", "Message"]


class ChatCreateParams(TypedDict, total=False):
    question: Required[str]
    """The current user question to send to the AI agent."""

    context: str
    """Free-form hint injected into the system prompt for this turn only."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Stable identifier for multi-turn conversations.

    If omitted, a new ID is generated.
    """

    messages: Iterable[Message]
    """Prior conversation history (NOT including the current question).

    Used for multi-turn context.
    """

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Scope the chat to a specific product.

    If omitted, the agent can access all products.
    """


class Message(TypedDict, total=False):
    content: Required[str]
    """The text content of the message."""

    role: Required[Literal["user", "assistant"]]
    """The role of the message sender."""
