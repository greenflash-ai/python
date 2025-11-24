# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .message_item_param import MessageItemParam
from .system_prompt_param import SystemPromptParam

__all__ = ["MessageCreateParams", "SystemPrompt"]


class MessageCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """Your external user ID that will be mapped to a user in our system."""

    messages: Required[Iterable[MessageItemParam]]
    """Array of conversation messages."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The Greenflash conversation ID.

    When provided, updates an existing conversation instead of creating a new one.
    Either conversationId, externalConversationId, productId must be provided.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your external identifier for the conversation.

    Either conversationId, externalConversationId, productId must be provided.
    """

    external_organization_id: Annotated[str, PropertyInfo(alias="externalOrganizationId")]
    """Your unique identifier for the organization this user belongs to.

    If provided, the user will be associated with this organization.
    """

    model: str
    """The AI model used for the conversation."""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """The Greenflash product this conversation belongs to.

    Either conversationId, externalConversationId, productId must be provided.
    """

    properties: Dict[str, object]
    """Additional data about the conversation."""

    system_prompt: Annotated[SystemPrompt, PropertyInfo(alias="systemPrompt")]
    """System prompt for the conversation.

    Can be a simple string or a prompt object with components.
    """


SystemPrompt: TypeAlias = Union[str, SystemPromptParam]
