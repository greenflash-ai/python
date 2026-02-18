# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateMessageResponse", "Message", "TemplateMatch"]


class Message(BaseModel):
    message_id: str = FieldInfo(alias="messageId")
    """The internal Greenflash message ID."""

    message_type: str = FieldInfo(alias="messageType")
    """The type of the message that was created."""

    status: Literal["created", "deduplicated"]
    """Whether the message was newly created or deduplicated.

    Messages with an externalMessageId that already exists in the conversation are
    automatically skipped and returned with status "deduplicated".
    """

    external_message_id: Optional[str] = FieldInfo(alias="externalMessageId", default=None)
    """Your external identifier for the message, if provided."""


class TemplateMatch(BaseModel):
    """Template match info when content was auto-matched against an existing template."""

    matched: bool

    confidence: Optional[Literal["exact", "high", "medium"]] = None

    detected_variables: Optional[Dict[str, str]] = FieldInfo(alias="detectedVariables", default=None)

    prompt_id: Optional[str] = FieldInfo(alias="promptId", default=None)


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

    prompt_variables: Optional[Dict[str, str]] = FieldInfo(alias="promptVariables", default=None)
    """Template variables used or detected for this conversation."""

    template_match: Optional[TemplateMatch] = FieldInfo(alias="templateMatch", default=None)
    """Template match info when content was auto-matched against an existing template."""
