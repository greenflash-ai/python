# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import conversion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.conversion_create_response import ConversionCreateResponse

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

    def create(
        self,
        *,
        action: str,
        external_user_id: str,
        value: str,
        value_type: Literal["currency", "numeric", "text"],
        conversation_id: str | NotGiven = NOT_GIVEN,
        converted_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_conversation_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversionCreateResponse:
        """
        Create Business Conversion Events

        Args:
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
                conversion_create_params.ConversionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversionCreateResponse,
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

    async def create(
        self,
        *,
        action: str,
        external_user_id: str,
        value: str,
        value_type: Literal["currency", "numeric", "text"],
        conversation_id: str | NotGiven = NOT_GIVEN,
        converted_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        external_conversation_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversionCreateResponse:
        """
        Create Business Conversion Events

        Args:
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
                conversion_create_params.ConversionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversionCreateResponse,
        )


class ConversionsResourceWithRawResponse:
    def __init__(self, conversions: ConversionsResource) -> None:
        self._conversions = conversions

        self.create = to_raw_response_wrapper(
            conversions.create,
        )


class AsyncConversionsResourceWithRawResponse:
    def __init__(self, conversions: AsyncConversionsResource) -> None:
        self._conversions = conversions

        self.create = async_to_raw_response_wrapper(
            conversions.create,
        )


class ConversionsResourceWithStreamingResponse:
    def __init__(self, conversions: ConversionsResource) -> None:
        self._conversions = conversions

        self.create = to_streamed_response_wrapper(
            conversions.create,
        )


class AsyncConversionsResourceWithStreamingResponse:
    def __init__(self, conversions: AsyncConversionsResource) -> None:
        self._conversions = conversions

        self.create = async_to_streamed_response_wrapper(
            conversions.create,
        )
