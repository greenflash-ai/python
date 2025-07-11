# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .system_prompt_param import SystemPromptParam

__all__ = ["MessageCreateParams", "Turn", "TurnMessage", "TurnSystemPromptOverride", "SystemPrompt"]


class MessageCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """The external user ID that will be mapped to a participant in our system."""

    turns: Required[Iterable[Turn]]
    """
    An array of conversation turns, each containing messages exchanged during that
    turn.
    """

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The conversation ID.

    When provided, this will update an existing conversation instead of creating a
    new one. Either conversationId, externalConversationId, productId, or projectId
    must be provided.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your own external identifier for the conversation.

    Either conversationId, externalConversationId, productId, or projectId must be
    provided.
    """

    metadata: Dict[str, object]
    """Additional metadata for the conversation."""

    model: str
    """The AI model used for the conversation."""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """The ID of the product this conversation belongs to.

    Either conversationId, externalConversationId, productId, or projectId must be
    provided.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The ID of the project this conversation belongs to.

    Either conversationId, externalConversationId, productId, or projectId must be
    provided.
    """

    system_prompt: Annotated[SystemPrompt, PropertyInfo(alias="systemPrompt")]
    """System prompt for the conversation.

    Can be a simple string or a template object with components.
    """

    version_id: Annotated[str, PropertyInfo(alias="versionId")]
    """The ID of the product version."""


class TurnMessage(TypedDict, total=False):
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

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """When this message was created."""

    message_index: Annotated[int, PropertyInfo(alias="messageIndex")]
    """The index of the message within the turn.

    Inferred based on the location in the array and previous records, but can be
    overridden here.
    """

    metadata: Dict[str, object]
    """Additional metadata for the message."""

    tokens: int
    """The number of tokens in the message."""


TurnSystemPromptOverride: TypeAlias = Union[str, SystemPromptParam]


class Turn(TypedDict, total=False):
    messages: Required[Iterable[TurnMessage]]
    """The messages exchanged during this turn."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """When this turn was created."""

    metadata: Dict[str, object]
    """Additional metadata for this turn."""

    model_override: Annotated[str, PropertyInfo(alias="modelOverride")]
    """Override the conversation-level model for this specific turn."""

    system_prompt_override: Annotated[TurnSystemPromptOverride, PropertyInfo(alias="systemPromptOverride")]
    """Override the conversation-level system prompt for this specific turn."""

    turn_index: Annotated[int, PropertyInfo(alias="turnIndex")]
    """The index of the turn in the conversation sequence.

    Inferred based on the location in the array and previous records, but can be
    overridden here.
    """


SystemPrompt: TypeAlias = Union[str, SystemPromptParam]
