# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import event_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.create_event_response import CreateEventResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        event_type: str,
        product_id: str,
        value: str,
        conversation_id: str | Omit = omit,
        event_at: Union[str, datetime] | Omit = omit,
        external_conversation_id: str | Omit = omit,
        external_organization_id: str | Omit = omit,
        external_user_id: str | Omit = omit,
        force_sample: bool | Omit = omit,
        influence: Literal["positive", "negative", "neutral"] | Omit = omit,
        insert_id: str | Omit = omit,
        organization_id: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        quality_impact_score: float | Omit = omit,
        sample_rate: float | Omit = omit,
        user_id: str | Omit = omit,
        value_type: Literal["currency", "numeric", "text", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateEventResponse:
        """Track timestamped events representing user or organization actions.

        Events are
        used to track important business outcomes (signups, conversions, upgrades,
        cancellations, etc.) and integrate them into Greenflash's quality metrics. Each
        event can be optionally linked to a conversation, user, and organization.

        Args:
          event_type: The specific name or category of the event being tracked (e.g., "trial_started",
              "signup", "feature_usage"). This helps categorize events for analysis and often
              pairs with "value" to define the outcome.

          product_id: The unique identifier of the Greenflash product associated with this event. This
              links the event to a specific product context.

          value: The specific value associated with the event (e.g., "99.00", "5",
              "premium_plan"). This pairs with "valueType" and "eventType" to define the
              magnitude or content of the event.

          conversation_id: The unique Greenflash identifier for the conversation. Links the event to a
              specific chat session in Greenflash.

          event_at: The ISO 8601 timestamp of when the event actually occurred. Defaults to the
              current time if not provided. Useful for backdating historical events.

          external_conversation_id: Your system's unique identifier for the conversation or thread where this event
              occurred.

          external_organization_id: Your system's unique identifier for the organization associated with this event.
              Used to map events to your customer accounts.

          external_user_id: Your system's unique identifier for the user associated with this event. Used to
              map Greenflash events back to your user records.

          force_sample: When true, bypasses sampling and ensures this event is always ingested
              regardless of sampleRate. Use for critical events that must be captured.

          influence: A high-level categorization of how this event generally "changed things" or
              influenced quality (positive, negative, or neutral). Use this for broad
              classification of outcomes.

          insert_id: A unique key for idempotency. If you retry a request with the same insertId, it
              prevents creating a duplicate event record.

          organization_id: The unique Greenflash identifier for the organization. Provide this if you have
              the Greenflash Organization ID.

          properties: A key-value object for storing additional, unstructured context about the event
              (e.g., { source: "web_app", campaign_id: "123" }). Useful for custom filtering.

          quality_impact_score: A precise numeric score between -1.0 and 1.0 for direct control over the quality
              impact. If omitted, it is automatically derived from the "influence" field.

          sample_rate: Controls the percentage of requests that are ingested (0.0 to 1.0). For example,
              0.1 means 10% of events will be stored. Defaults to 1.0 (all events ingested).
              Sampling is deterministic based on event type and organization.

          user_id: The unique Greenflash identifier for the user. Provide this if you already have
              the Greenflash User ID; otherwise, use "externalUserId".

          value_type: Defines the format of the "value" field (currency, numeric, or text). This
              ensures the value is interpreted and processed correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "product_id": product_id,
                    "value": value,
                    "conversation_id": conversation_id,
                    "event_at": event_at,
                    "external_conversation_id": external_conversation_id,
                    "external_organization_id": external_organization_id,
                    "external_user_id": external_user_id,
                    "force_sample": force_sample,
                    "influence": influence,
                    "insert_id": insert_id,
                    "organization_id": organization_id,
                    "properties": properties,
                    "quality_impact_score": quality_impact_score,
                    "sample_rate": sample_rate,
                    "user_id": user_id,
                    "value_type": value_type,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEventResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        event_type: str,
        product_id: str,
        value: str,
        conversation_id: str | Omit = omit,
        event_at: Union[str, datetime] | Omit = omit,
        external_conversation_id: str | Omit = omit,
        external_organization_id: str | Omit = omit,
        external_user_id: str | Omit = omit,
        force_sample: bool | Omit = omit,
        influence: Literal["positive", "negative", "neutral"] | Omit = omit,
        insert_id: str | Omit = omit,
        organization_id: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        quality_impact_score: float | Omit = omit,
        sample_rate: float | Omit = omit,
        user_id: str | Omit = omit,
        value_type: Literal["currency", "numeric", "text", "boolean"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateEventResponse:
        """Track timestamped events representing user or organization actions.

        Events are
        used to track important business outcomes (signups, conversions, upgrades,
        cancellations, etc.) and integrate them into Greenflash's quality metrics. Each
        event can be optionally linked to a conversation, user, and organization.

        Args:
          event_type: The specific name or category of the event being tracked (e.g., "trial_started",
              "signup", "feature_usage"). This helps categorize events for analysis and often
              pairs with "value" to define the outcome.

          product_id: The unique identifier of the Greenflash product associated with this event. This
              links the event to a specific product context.

          value: The specific value associated with the event (e.g., "99.00", "5",
              "premium_plan"). This pairs with "valueType" and "eventType" to define the
              magnitude or content of the event.

          conversation_id: The unique Greenflash identifier for the conversation. Links the event to a
              specific chat session in Greenflash.

          event_at: The ISO 8601 timestamp of when the event actually occurred. Defaults to the
              current time if not provided. Useful for backdating historical events.

          external_conversation_id: Your system's unique identifier for the conversation or thread where this event
              occurred.

          external_organization_id: Your system's unique identifier for the organization associated with this event.
              Used to map events to your customer accounts.

          external_user_id: Your system's unique identifier for the user associated with this event. Used to
              map Greenflash events back to your user records.

          force_sample: When true, bypasses sampling and ensures this event is always ingested
              regardless of sampleRate. Use for critical events that must be captured.

          influence: A high-level categorization of how this event generally "changed things" or
              influenced quality (positive, negative, or neutral). Use this for broad
              classification of outcomes.

          insert_id: A unique key for idempotency. If you retry a request with the same insertId, it
              prevents creating a duplicate event record.

          organization_id: The unique Greenflash identifier for the organization. Provide this if you have
              the Greenflash Organization ID.

          properties: A key-value object for storing additional, unstructured context about the event
              (e.g., { source: "web_app", campaign_id: "123" }). Useful for custom filtering.

          quality_impact_score: A precise numeric score between -1.0 and 1.0 for direct control over the quality
              impact. If omitted, it is automatically derived from the "influence" field.

          sample_rate: Controls the percentage of requests that are ingested (0.0 to 1.0). For example,
              0.1 means 10% of events will be stored. Defaults to 1.0 (all events ingested).
              Sampling is deterministic based on event type and organization.

          user_id: The unique Greenflash identifier for the user. Provide this if you already have
              the Greenflash User ID; otherwise, use "externalUserId".

          value_type: Defines the format of the "value" field (currency, numeric, or text). This
              ensures the value is interpreted and processed correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "product_id": product_id,
                    "value": value,
                    "conversation_id": conversation_id,
                    "event_at": event_at,
                    "external_conversation_id": external_conversation_id,
                    "external_organization_id": external_organization_id,
                    "external_user_id": external_user_id,
                    "force_sample": force_sample,
                    "influence": influence,
                    "insert_id": insert_id,
                    "organization_id": organization_id,
                    "properties": properties,
                    "quality_impact_score": quality_impact_score,
                    "sample_rate": sample_rate,
                    "user_id": user_id,
                    "value_type": value_type,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEventResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
