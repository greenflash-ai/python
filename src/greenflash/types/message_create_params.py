# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_item_param import MessageItemParam
from .system_prompt_param import SystemPromptParam

__all__ = ["MessageCreateParams", "Turn"]


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

    system_prompt: Annotated[SystemPromptParam, PropertyInfo(alias="systemPrompt")]
    """System prompt for the conversation.

    Can be a simple string or a template object with components.
    """

    version_id: Annotated[str, PropertyInfo(alias="versionId")]
    """The ID of the product version."""


class Turn(TypedDict, total=False):
    messages: Required[Iterable[MessageItemParam]]
    """The messages exchanged during this turn."""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """When this turn was created."""

    metadata: Dict[str, object]
    """Additional metadata for this turn."""

    model_override: Annotated[str, PropertyInfo(alias="modelOverride")]
    """Override the conversation-level model for this specific turn."""

    system_prompt_override: Annotated[SystemPromptParam, PropertyInfo(alias="systemPromptOverride")]
    """System prompt for the conversation.

    Can be a simple string or a template object with components.
    """

    turn_index: Annotated[float, PropertyInfo(alias="turnIndex")]
    """The index of the turn in the conversation sequence.

    Inferred based on the location in the array and previous records, but can be
    overridden here.
    """
