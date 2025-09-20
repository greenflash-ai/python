# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import conversion_log_params
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
from ..types.log_conversion_response import LogConversionResponse

__all__ = ["ConversionsResource", "AsyncConversionsResource"]


class ConversionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return ConversionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return ConversionsResourceWithStreamingResponse(self)

    def log(
        self,
        *,
        action: str,
        external_user_id: str,
        value: str,
        value_type: Literal["currency", "numeric", "text"],
        conversation_id: str | Omit = omit,
        converted_at: str | Omit = omit,
        external_conversation_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        product_id: str | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogConversionResponse:
        """
        Track important business events like purchases, signups, or upgrades that result
        from your conversations.

        Use this endpoint to record when users take valuable actions after interacting
        with your AI. You can link conversions to specific conversations using either
        the internal `conversationId` or your own `externalConversationId`.

        Args:
          action: The type of conversion (e.g., "purchase", "signup", "upgrade").

          external_user_id: Your unique identifier for the user who completed the conversion.

          value: The conversion value (interpretation depends on valueType).

          value_type: The type of value: currency (e.g., "$99.99"), numeric (e.g., "5"), or text.

          conversation_id: The Greenflash conversation ID that led to this conversion.

          converted_at: When the conversion occurred. Defaults to current time if not provided.

          external_conversation_id: Your external conversation identifier that led to this conversion.

          metadata: Additional data about the conversion.

          product_id: The Greenflash product associated with this conversion.

          project_id: The Greenflash project associated with this conversion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conversions",
            body=maybe_transform(
                {
                    "action": action,
                    "external_user_id": external_user_id,
                    "value": value,
                    "value_type": value_type,
                    "conversation_id": conversation_id,
                    "converted_at": converted_at,
                    "external_conversation_id": external_conversation_id,
                    "metadata": metadata,
                    "product_id": product_id,
                    "project_id": project_id,
                },
                conversion_log_params.ConversionLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogConversionResponse,
        )


class AsyncConversionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncConversionsResourceWithStreamingResponse(self)

    async def log(
        self,
        *,
        action: str,
        external_user_id: str,
        value: str,
        value_type: Literal["currency", "numeric", "text"],
        conversation_id: str | Omit = omit,
        converted_at: str | Omit = omit,
        external_conversation_id: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        product_id: str | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogConversionResponse:
        """
        Track important business events like purchases, signups, or upgrades that result
        from your conversations.

        Use this endpoint to record when users take valuable actions after interacting
        with your AI. You can link conversions to specific conversations using either
        the internal `conversationId` or your own `externalConversationId`.

        Args:
          action: The type of conversion (e.g., "purchase", "signup", "upgrade").

          external_user_id: Your unique identifier for the user who completed the conversion.

          value: The conversion value (interpretation depends on valueType).

          value_type: The type of value: currency (e.g., "$99.99"), numeric (e.g., "5"), or text.

          conversation_id: The Greenflash conversation ID that led to this conversion.

          converted_at: When the conversion occurred. Defaults to current time if not provided.

          external_conversation_id: Your external conversation identifier that led to this conversion.

          metadata: Additional data about the conversion.

          product_id: The Greenflash product associated with this conversion.

          project_id: The Greenflash project associated with this conversion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conversions",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "external_user_id": external_user_id,
                    "value": value,
                    "value_type": value_type,
                    "conversation_id": conversation_id,
                    "converted_at": converted_at,
                    "external_conversation_id": external_conversation_id,
                    "metadata": metadata,
                    "product_id": product_id,
                    "project_id": project_id,
                },
                conversion_log_params.ConversionLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogConversionResponse,
        )


class ConversionsResourceWithRawResponse:
    def __init__(self, conversions: ConversionsResource) -> None:
        self._conversions = conversions

        self.log = to_raw_response_wrapper(
            conversions.log,
        )


class AsyncConversionsResourceWithRawResponse:
    def __init__(self, conversions: AsyncConversionsResource) -> None:
        self._conversions = conversions

        self.log = async_to_raw_response_wrapper(
            conversions.log,
        )


class ConversionsResourceWithStreamingResponse:
    def __init__(self, conversions: ConversionsResource) -> None:
        self._conversions = conversions

        self.log = to_streamed_response_wrapper(
            conversions.log,
        )


class AsyncConversionsResourceWithStreamingResponse:
    def __init__(self, conversions: AsyncConversionsResource) -> None:
        self._conversions = conversions

        self.log = async_to_streamed_response_wrapper(
            conversions.log,
        )
