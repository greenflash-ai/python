# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateResponse", "Turn", "TurnMessage"]


class TurnMessage(BaseModel):
    message_id: str = FieldInfo(alias="messageId")
    """The internal ID of the message."""

    message_index: float = FieldInfo(alias="messageIndex")
    """The index of the message within the turn."""

    role: Literal["user", "assistant", "system"]
    """The role of the message sender."""


class Turn(BaseModel):
    messages: List[TurnMessage]
    """The messages that were processed during this turn."""

    turn_id: str = FieldInfo(alias="turnId")
    """The internal ID of the turn."""

    turn_index: float = FieldInfo(alias="turnIndex")
    """The index of the turn in the conversation."""


class CreateResponse(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")
    """The ID of the conversation that was created or updated."""

    success: bool
    """Indicates whether the API call was successful."""

    system_prompt_component_ids: List[str] = FieldInfo(alias="systemPromptComponentIds")
    """The component IDs used internally to track the system prompt components."""

    system_prompt_template_id: str = FieldInfo(alias="systemPromptTemplateId")
    """The template ID used internally to track the system prompt template."""

    turns: List[Turn]
    """The turns that were processed, including their internal IDs."""
