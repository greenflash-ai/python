# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateMessageResponse", "Message"]


class Message(BaseModel):
    message_id: str = FieldInfo(alias="messageId")
    """The internal Greenflash message ID."""

    message_type: str = FieldInfo(alias="messageType")
    """The type of the message that was created."""

    external_message_id: Optional[str] = FieldInfo(alias="externalMessageId", default=None)
    """Your external identifier for the message, if provided."""


class CreateMessageResponse(BaseModel):
    """Success response for message logging."""

    conversation_id: str = FieldInfo(alias="conversationId")
    """The ID of the conversation that was created or updated."""

    messages: List[Message]
    """The messages that were processed."""

    success: bool
    """Whether the API call was successful."""

    system_prompt_component_ids: List[str] = FieldInfo(alias="systemPromptComponentIds")
    """The component IDs used internally to track the system prompt components."""

    system_prompt_prompt_id: str = FieldInfo(alias="systemPromptPromptId")
    """The prompt ID used internally to track the system prompt."""
