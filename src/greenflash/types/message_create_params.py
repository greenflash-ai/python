# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .turn_item_param import TurnItemParam
from .system_prompt_param import SystemPromptParam

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """The external user ID that will be mapped to a participant in our system."""

    turns: Required[Iterable[TurnItemParam]]
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
