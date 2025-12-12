# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    event_type: Required[Annotated[str, PropertyInfo(alias="eventType")]]
    """
    The specific name or category of the event being tracked (e.g., "trial_started",
    "signup", "feature_usage"). This helps categorize events for analysis and often
    pairs with "value" to define the outcome.
    """

    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """The unique identifier of the Greenflash product associated with this event.

    This links the event to a specific product context.
    """

    value: Required[str]
    """
    The specific value associated with the event (e.g., "99.00", "5",
    "premium_plan"). This pairs with "valueType" and "eventType" to define the
    magnitude or content of the event.
    """

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The unique Greenflash identifier for the conversation.

    Links the event to a specific chat session in Greenflash.
    """

    event_at: Annotated[Union[str, datetime], PropertyInfo(alias="eventAt", format="iso8601")]
    """The ISO 8601 timestamp of when the event actually occurred.

    Defaults to the current time if not provided. Useful for backdating historical
    events.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """
    Your system's unique identifier for the conversation or thread where this event
    occurred.
    """

    external_organization_id: Annotated[str, PropertyInfo(alias="externalOrganizationId")]
    """Your system's unique identifier for the organization associated with this event.

    Used to map events to your customer accounts.
    """

    external_user_id: Annotated[str, PropertyInfo(alias="externalUserId")]
    """Your system's unique identifier for the user associated with this event.

    Used to map Greenflash events back to your user records.
    """

    force_sample: Annotated[bool, PropertyInfo(alias="forceSample")]
    """
    When true, bypasses sampling and ensures this event is always ingested
    regardless of sampleRate. Use for critical events that must be captured.
    """

    influence: Literal["positive", "negative", "neutral"]
    """
    A high-level categorization of how this event generally "changed things" or
    influenced quality (positive, negative, or neutral). Use this for broad
    classification of outcomes.
    """

    insert_id: Annotated[str, PropertyInfo(alias="insertId")]
    """A unique key for idempotency.

    If you retry a request with the same insertId, it prevents creating a duplicate
    event record.
    """

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """The unique Greenflash identifier for the organization.

    Provide this if you have the Greenflash Organization ID.
    """

    properties: Dict[str, object]
    """
    A key-value object for storing additional, unstructured context about the event
    (e.g., { source: "web_app", campaign_id: "123" }). Useful for custom filtering.
    """

    quality_impact_score: Annotated[float, PropertyInfo(alias="qualityImpactScore")]
    """
    A precise numeric score between -1.0 and 1.0 for direct control over the quality
    impact. If omitted, it is automatically derived from the "influence" field.
    """

    sample_rate: Annotated[float, PropertyInfo(alias="sampleRate")]
    """Controls the percentage of requests that are ingested (0.0 to 1.0).

    For example, 0.1 means 10% of events will be stored. Defaults to 1.0 (all events
    ingested). Sampling is deterministic based on event type and organization.
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """The unique Greenflash identifier for the user.

    Provide this if you already have the Greenflash User ID; otherwise, use
    "externalUserId".
    """

    value_type: Annotated[Literal["currency", "numeric", "text", "boolean"], PropertyInfo(alias="valueType")]
    """Defines the format of the "value" field (currency, numeric, or text).

    This ensures the value is interpreted and processed correctly.
    """
