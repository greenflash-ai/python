# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageCreateParams", "Turn", "TurnMessage"]


class MessageCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]

    turns: Required[Iterable[Turn]]

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]

    metadata: object

    model: str

    product_id: Annotated[str, PropertyInfo(alias="productId")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    system_prompt: Annotated[str, PropertyInfo(alias="systemPrompt")]

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


class Turn(TypedDict, total=False):
    messages: Required[Iterable[TurnMessage]]

    turn_index: Required[Annotated[int, PropertyInfo(alias="turnIndex")]]

    system_prompt_override: Annotated[str, PropertyInfo(alias="systemPromptOverride")]
