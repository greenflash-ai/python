# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageCreateResponse", "Turn", "TurnMessage"]


class TurnMessage(BaseModel):
    message_id: str = FieldInfo(alias="messageId")

    message_index: int = FieldInfo(alias="messageIndex")

    role: Literal["user", "assistant", "system"]


class Turn(BaseModel):
    messages: List[TurnMessage]

    turn_id: str = FieldInfo(alias="turnId")

    turn_index: int = FieldInfo(alias="turnIndex")


class MessageCreateResponse(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")
    """The ID of the conversation that was created or updated."""

    success: bool
    """Indicates whether the API call was successful."""

    system_prompt_component_ids: Optional[List[str]] = FieldInfo(alias="systemPromptComponentIds", default=None)
    """The component IDs used internally to track the system prompt components."""

    system_prompt_template_id: Optional[str] = FieldInfo(alias="systemPromptTemplateId", default=None)
    """The template ID used internally to track the system prompt template."""

    turns: Optional[List[Turn]] = None
