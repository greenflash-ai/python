# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageItemParam", "Voice", "VoiceProsody"]


class VoiceProsody(TypedDict, total=False):
    """
    Optional prosody / tone signals from upstream voice infrastructure (Deepgram, Hume, Retell, etc.).
    """

    arousal: float
    """Vocal energy / intensity, 0 (calm) to 1 (highly energetic)."""

    emotion: str
    """Optional fine-grained emotion label provided by an upstream prosody model."""

    sentiment_label: Annotated[Literal["positive", "neutral", "negative"], PropertyInfo(alias="sentimentLabel")]
    """Prosody-derived sentiment label."""

    sentiment_score: Annotated[float, PropertyInfo(alias="sentimentScore")]
    """Prosody-derived sentiment score from -1 (negative) to 1 (positive).

    Distinct from text-derived sentiment — captures tone/intonation rather than word
    choice.
    """


class Voice(TypedDict, total=False):
    """
    Voice-specific signals for this turn (latency, interruption, ASR confidence, prosody, etc.). Stored alongside `properties` and analyzed by voice-aware pipelines.
    """

    asr_confidence: Annotated[float, PropertyInfo(alias="asrConfidence")]
    """
    ASR transcription confidence for this turn, 0 (uncertain) to 1 (fully
    confident).
    """

    audio_url: Annotated[str, PropertyInfo(alias="audioUrl")]
    """Optional URL to the audio segment for this turn.

    Greenflash does not store audio; the URL is embedded in the UI as a
    pass-through.
    """

    barge_in: Annotated[bool, PropertyInfo(alias="bargeIn")]
    """
    True when this turn began while the other speaker was still talking (a barge-in
    / overlap).
    """

    duration_ms: Annotated[int, PropertyInfo(alias="durationMs")]
    """Length of this turn in milliseconds."""

    ended_at: Annotated[int, PropertyInfo(alias="endedAt")]
    """When this turn finished speaking, as Unix epoch milliseconds."""

    prosody: VoiceProsody
    """
    Optional prosody / tone signals from upstream voice infrastructure (Deepgram,
    Hume, Retell, etc.).
    """

    response_latency_ms: Annotated[int, PropertyInfo(alias="responseLatencyMs")]
    """Time between the previous speaker ending and this turn starting (ms).

    Useful for measuring agent response latency.
    """

    silence_before_ms: Annotated[int, PropertyInfo(alias="silenceBeforeMs")]
    """Silence duration immediately before this turn (ms)."""

    speaker: str
    """Optional speaker label (e.g.

    "agent", "user", or a diarization-assigned ID like "Speaker 0").
    """

    started_at: Annotated[int, PropertyInfo(alias="startedAt")]
    """When this turn started speaking, as Unix epoch milliseconds."""

    was_interrupted: Annotated[bool, PropertyInfo(alias="wasInterrupted")]
    """True when this turn was cut off by the other speaker."""


class MessageItemParam(TypedDict, total=False):
    content: str
    """The message content. Required for language-based analyses."""

    context: Optional[str]
    """Additional context (e.g., RAG data) used to generate the message."""

    created_at: Annotated[Union[str, date, None], PropertyInfo(alias="createdAt", format="iso8601")]
    """When this message was created.

    Accepts a Date or an ISO-8601 string. If not provided, messages get sequential
    timestamps. Use for importing historical data — and required when you want the
    voice analysis pipeline to derive response-latency / silence-before signals from
    inter-message gaps on uninstrumented voice transcripts.
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
            "final_response",
            "thought",
            "tool_call",
            "observation",
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
    system_message, final_response, thought, tool_call, observation, retrieval,
    memory_read, memory_write, chain_start, chain_end, embedding, tool_error,
    callback, llm, task, workflow
    """

    model: str
    """The AI model used for this specific message.

    Use for multi-agent scenarios where different messages use different models.
    Overrides the conversation-level model for this message.
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

    voice: Voice
    """
    Voice-specific signals for this turn (latency, interruption, ASR confidence,
    prosody, etc.). Stored alongside `properties` and analyzed by voice-aware
    pipelines.
    """
