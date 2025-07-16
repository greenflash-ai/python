# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_item_param import MessageItemParam
from .system_prompt_param import SystemPromptParam

__all__ = ["TurnItemParam"]


class TurnItemParam(TypedDict, total=False):
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
