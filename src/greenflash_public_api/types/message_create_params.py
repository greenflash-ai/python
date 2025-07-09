# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MessageCreateParams",
    "Turn",
    "TurnMessage",
    "TurnSystemPromptOverride",
    "TurnSystemPromptOverrideSystemPrompt",
    "TurnSystemPromptOverrideSystemPromptComponent",
    "SystemPrompt",
    "SystemPromptSystemPrompt",
    "SystemPromptSystemPromptComponent",
]


class MessageCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]

    turns: Required[Iterable[Turn]]

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]

    metadata: object

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

    metadata: object

    tokens: int


class TurnSystemPromptOverrideSystemPromptComponent(TypedDict, total=False):
    content: Required[str]

    source: Required[Literal["customer", "participant", "greenflash", "agent"]]

    type: Required[Literal["system", "endUser", "userModified", "rag", "agent"]]

    is_dynamic: Annotated[bool, PropertyInfo(alias="isDynamic")]

    name: str

    tags: List[str]

    version: int


class TurnSystemPromptOverrideSystemPrompt(TypedDict, total=False):
    components: Iterable[TurnSystemPromptOverrideSystemPromptComponent]

    external_template_id: Annotated[str, PropertyInfo(alias="externalTemplateId")]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]


TurnSystemPromptOverride: TypeAlias = Union[str, TurnSystemPromptOverrideSystemPrompt]


class Turn(TypedDict, total=False):
    messages: Required[Iterable[TurnMessage]]

    turn_index: Required[Annotated[int, PropertyInfo(alias="turnIndex")]]

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    metadata: object

    model_override: Annotated[str, PropertyInfo(alias="modelOverride")]

    system_prompt_override: Annotated[TurnSystemPromptOverride, PropertyInfo(alias="systemPromptOverride")]


class SystemPromptSystemPromptComponent(TypedDict, total=False):
    content: Required[str]

    source: Required[Literal["customer", "participant", "greenflash", "agent"]]

    type: Required[Literal["system", "endUser", "userModified", "rag", "agent"]]

    is_dynamic: Annotated[bool, PropertyInfo(alias="isDynamic")]

    name: str

    tags: List[str]

    version: int


class SystemPromptSystemPrompt(TypedDict, total=False):
    components: Iterable[SystemPromptSystemPromptComponent]

    external_template_id: Annotated[str, PropertyInfo(alias="externalTemplateId")]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]


SystemPrompt: TypeAlias = Union[str, SystemPromptSystemPrompt]
