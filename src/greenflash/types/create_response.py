# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateResponse", "Message"]


class Message(BaseModel):
    message_id: str = FieldInfo(alias="messageId")
    """The internal Greenflash message ID."""

    message_type: str = FieldInfo(alias="messageType")
    """The type of the message that was created."""

    external_message_id: Optional[str] = FieldInfo(alias="externalMessageId", default=None)
    """Your external identifier for the message, if provided."""


class CreateResponse(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")
    """The ID of the conversation that was created or updated."""

    messages: List[Message]
    """The messages that were processed."""

    success: bool
    """Whether the API call was successful."""

    system_prompt_component_ids: List[str] = FieldInfo(alias="systemPromptComponentIds")
    """The component IDs used internally to track the system prompt components."""

    system_prompt_template_id: str = FieldInfo(alias="systemPromptTemplateId")
    """The template ID used internally to track the system prompt template."""
