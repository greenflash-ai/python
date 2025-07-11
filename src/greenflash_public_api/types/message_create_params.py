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

    turns: Required[Iterable[Turn]]

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]

    metadata: Dict[str, object]

    model: str

    product_id: Annotated[str, PropertyInfo(alias="productId")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    system_prompt: Annotated[SystemPrompt, PropertyInfo(alias="systemPrompt")]

    version_id: Annotated[str, PropertyInfo(alias="versionId")]


class TurnMessage(TypedDict, total=False):
    content: Required[str]

    content_type: Required[Annotated[Literal["text", "image", "audio", "json"], PropertyInfo(alias="contentType")]]

    message_index: Required[Annotated[int, PropertyInfo(alias="messageIndex")]]

    role: Required[Literal["user", "assistant", "system"]]

    context: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    metadata: Dict[str, object]

    tokens: int


TurnSystemPromptOverride: TypeAlias = Union[str, SystemPromptParam]


class Turn(TypedDict, total=False):
    messages: Required[Iterable[TurnMessage]]

    turn_index: Required[Annotated[int, PropertyInfo(alias="turnIndex")]]

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    metadata: Dict[str, object]

    model_override: Annotated[str, PropertyInfo(alias="modelOverride")]

    system_prompt_override: Annotated[TurnSystemPromptOverride, PropertyInfo(alias="systemPromptOverride")]


SystemPrompt: TypeAlias = Union[str, SystemPromptParam]
