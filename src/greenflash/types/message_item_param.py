# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .system_prompt_param import SystemPromptParam

__all__ = ["MessageItemParam"]


class MessageItemParam(TypedDict, total=False):
    content: str
    """String content of the message. Required for language-based analyses."""

    context: Optional[str]
    """Additional context (e.g., RAG data) used in generating the message."""

    created_at: Annotated[str, PropertyInfo(alias="createdAt")]
    """When this message was created.

    If not provided, messages will be assigned sequential timestamps to preserve
    order. If provided, this timestamp will be used as-is (useful for importing
    historical data).
    """

    external_message_id: Annotated[str, PropertyInfo(alias="externalMessageId")]
    """Your own external identifier for this message.

    This can be used to reference the message in other API calls.
    """

    input: Dict[str, object]
    """
    Structured input data for tool calls, retrievals, or other structured
    operations.
    """

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

    Cannot be used with role. Allowed values: user_message, assistant_message,
    system_message, thought, tool_call, observation, final_response, retrieval,
    memory_read, memory_write, chain_start, chain_end, embedding, tool_error,
    callback, llm, task, workflow
    """

    metadata: Dict[str, object]
    """Additional metadata for the message."""

    model_override: Annotated[str, PropertyInfo(alias="modelOverride")]
    """Override the conversation-level model for this specific message."""

    output: Dict[str, object]
    """
    Structured output data from tool calls, retrievals, or other structured
    operations.
    """

    parent_external_message_id: Annotated[str, PropertyInfo(alias="parentExternalMessageId")]
    """The external ID of the parent message for threading.

    Cannot be used with parentMessageId.
    """

    parent_message_id: Annotated[str, PropertyInfo(alias="parentMessageId")]
    """The internal ID of the parent message for threading.

    Cannot be used with parentExternalMessageId.
    """

    role: Literal["user", "assistant", "system"]
    """Simple message role for basic chat scenarios.

    One of: 'user', 'assistant', or 'system'. Cannot be used with messageType.
    """

    system_prompt_override: Annotated[SystemPromptParam, PropertyInfo(alias="systemPromptOverride")]
    """System prompt for the conversation.

    Can be a simple string or a template object with components.
    """

    tool_name: Annotated[str, PropertyInfo(alias="toolName")]
    """Name of the tool being called. Required for tool_call messages."""
