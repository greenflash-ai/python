# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_item_param import MessageItemParam
from .system_prompt_param import SystemPromptParam

__all__ = ["MessageCreateParams", "VoiceCall", "VoiceCallLatency"]


class MessageCreateParams(TypedDict, total=False):
    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """Your external user ID that will be mapped to a user in our system."""

    messages: Required[Iterable[MessageItemParam]]
    """Array of conversation messages."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The Greenflash conversation ID.

    When provided, updates an existing conversation instead of creating a new one.
    Either conversationId, externalConversationId, productId must be provided.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your external identifier for the conversation.

    Either conversationId, externalConversationId, productId must be provided.
    """

    external_organization_id: Annotated[str, PropertyInfo(alias="externalOrganizationId")]
    """Your unique identifier for the organization this user belongs to.

    If provided, the user will be associated with this organization.
    """

    force_sample: Annotated[bool, PropertyInfo(alias="forceSample")]
    """
    When true, bypasses sampling and ensures this request is always ingested
    regardless of sampleRate. Use for critical conversations that must be captured.
    """

    model: str
    """The AI model used for the conversation."""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """The Greenflash product this conversation belongs to.

    Either conversationId, externalConversationId, productId must be provided.
    """

    properties: Dict[str, object]
    """Additional data about the conversation."""

    sample_rate: Annotated[float, PropertyInfo(alias="sampleRate")]
    """Controls the percentage of requests that are ingested (0.0 to 1.0).

    For example, 0.1 means 10% of requests will be stored. Defaults to 1.0 (all
    requests ingested). Sampling is deterministic based on conversation ID.
    """

    system_prompt: Annotated[SystemPromptParam, PropertyInfo(alias="systemPrompt")]
    """System prompt for the conversation.

    Can be a simple string or a prompt object with components.
    """

    voice_call: Annotated[VoiceCall, PropertyInfo(alias="voiceCall")]
    """
    Voice-specific signals for the full call/conversation (platform, duration,
    latency aggregates, recording URL, etc.). Stored on the conversation alongside
    `properties` and analyzed by voice-aware pipelines.
    """


class VoiceCallLatency(TypedDict, total=False):
    """Component and end-to-end latency aggregates for the call."""

    asr_ms: Annotated[int, PropertyInfo(alias="asrMs")]
    """Average ASR (speech-to-text) latency in ms."""

    e2e_ms: Annotated[int, PropertyInfo(alias="e2eMs")]
    """Average end-to-end latency from user end-of-turn to agent first audio (ms)."""

    llm_ms: Annotated[int, PropertyInfo(alias="llmMs")]
    """Average LLM inference latency in ms."""

    tts_ms: Annotated[int, PropertyInfo(alias="ttsMs")]
    """Average TTS (text-to-speech) latency in ms."""


class VoiceCall(TypedDict, total=False):
    """
    Voice-specific signals for the full call/conversation (platform, duration, latency aggregates, recording URL, etc.). Stored on the conversation alongside `properties` and analyzed by voice-aware pipelines.
    """

    call_successful: Annotated[bool, PropertyInfo(alias="callSuccessful")]
    """Optional platform-supplied success determination (e.g.

    Retell’s `call_successful`).
    """

    duration_ms: Annotated[int, PropertyInfo(alias="durationMs")]
    """Total call duration in milliseconds."""

    ended_reason: Annotated[str, PropertyInfo(alias="endedReason")]
    """How the call ended (platform-specific string, e.g.

    "user_hangup", "assistant_hangup", "timeout").
    """

    interruption_count: Annotated[int, PropertyInfo(alias="interruptionCount")]
    """Number of barge-ins / interruptions detected over the call."""

    latency: VoiceCallLatency
    """Component and end-to-end latency aggregates for the call."""

    platform: Literal[
        "vapi", "retell", "elevenlabs", "openai_realtime", "livekit", "bland", "synthflow", "simpleai", "other"
    ]
    """Identifier of the voice platform that produced the call."""

    platform_call_id: Annotated[str, PropertyInfo(alias="platformCallId")]
    """The voice platform’s native call ID.

    Useful for cross-referencing back to the source.
    """

    recording_url: Annotated[str, PropertyInfo(alias="recordingUrl")]
    """Optional URL to the full call recording.

    Greenflash does not store audio; the URL is embedded in the UI as a
    pass-through.
    """

    silence_count: Annotated[int, PropertyInfo(alias="silenceCount")]
    """Number of long silence segments detected over the call."""

    structured_outputs: Annotated[Dict[str, object], PropertyInfo(alias="structuredOutputs")]
    """Optional structured data extracted from the call by the platform (e.g.

    Vapi structured outputs, Retell custom analysis data).
    """
