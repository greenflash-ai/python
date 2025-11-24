# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageItemParam"]


class MessageItemParam(TypedDict, total=False):
    content: str
    """The message content. Required for language-based analyses."""

    context: Optional[str]
    """Additional context (e.g., RAG data) used to generate the message."""

    created_at: Annotated[Union[str, date], PropertyInfo(alias="createdAt", format="iso8601")]
    """When this message was created.

    If not provided, messages get sequential timestamps. Use for importing
    historical data.
    """

    external_message_id: Annotated[str, PropertyInfo(alias="externalMessageId")]
    """Your external identifier for this message.

    Used to reference the message in other API calls.
    """

    input: Dict[str, object]
    """Structured input data for tool calls, retrievals, or other operations."""

    message_type: Annotated[
        Literal[
            "user_message",
            "assistant_message",
            "system_message",
            "thought",
            "tool_call",
            "observation",
            "final_response",
            "retrieval",
            "memory_read",
            "memory_write",
            "chain_start",
            "chain_end",
            "embedding",
            "tool_error",
            "callback",
            "llm",
            "task",
            "workflow",
        ],
        PropertyInfo(alias="messageType"),
    ]
    """Detailed message type for agentic workflows.

    Cannot be used with role. Available types: user_message, assistant_message,
    system_message, thought, tool_call, observation, final_response, retrieval,
    memory_read, memory_write, chain_start, chain_end, embedding, tool_error,
    callback, llm, task, workflow
    """

    output: Dict[str, object]
    """Structured output data from tool calls, retrievals, or other operations."""

    parent_external_message_id: Annotated[str, PropertyInfo(alias="parentExternalMessageId")]
    """The external ID of the parent message for threading.

    Cannot be used with parentMessageId.
    """

    parent_message_id: Annotated[str, PropertyInfo(alias="parentMessageId")]
    """The internal ID of the parent message for threading.

    Cannot be used with parentExternalMessageId.
    """

    properties: Dict[str, object]
    """Custom message properties."""

    role: Literal["user", "assistant", "system"]
    """Simple message role for basic chat: user, assistant, or system.

    Cannot be used with messageType.
    """

    tool_name: Annotated[str, PropertyInfo(alias="toolName")]
    """Name of the tool being called. Required for tool_call messages."""
