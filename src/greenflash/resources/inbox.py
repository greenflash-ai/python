# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import inbox_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_inbox_response import ListInboxResponse
from ..types.get_inbox_item_response import GetInboxItemResponse

__all__ = ["InboxResource", "AsyncInboxResource"]


class InboxResource(SyncAPIResource):
    """Review flagged conversations"""

    @cached_property
    def with_raw_response(self) -> InboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return InboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return InboxResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        min_severity: int | Omit = omit,
        status: Literal["unreviewed", "reviewed", "dismissed"] | Omit = omit,
        trigger_type: Literal["guardrail", "expectation_check", "novelty", "manual_review", "revenue_risk"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListInboxResponse:
        """List conversations that have been flagged for review.

        Filter by review status,
        trigger type, or severity to focus on what matters most. Results are ordered by
        attention score (unreviewed) or last updated (reviewed/dismissed).

        Args:
          min_severity: Minimum severity level to include (1-5).

          status: Filter by review status. Defaults to "unreviewed".

          trigger_type: Filter by trigger type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/inbox",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_severity": min_severity,
                        "status": status,
                        "trigger_type": trigger_type,
                    },
                    inbox_list_params.InboxListParams,
                ),
            ),
            cast_to=ListInboxResponse,
        )

    def get(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetInboxItemResponse:
        """
        Get the full detail of a single inbox item including conversation messages,
        analysis scores, trigger metadata, keywords, and participant information.

        Args:
          conversation_id: The conversation ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return self._get(
            path_template("/inbox/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetInboxItemResponse,
        )


class AsyncInboxResource(AsyncAPIResource):
    """Review flagged conversations"""

    @cached_property
    def with_raw_response(self) -> AsyncInboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncInboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncInboxResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        min_severity: int | Omit = omit,
        status: Literal["unreviewed", "reviewed", "dismissed"] | Omit = omit,
        trigger_type: Literal["guardrail", "expectation_check", "novelty", "manual_review", "revenue_risk"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListInboxResponse:
        """List conversations that have been flagged for review.

        Filter by review status,
        trigger type, or severity to focus on what matters most. Results are ordered by
        attention score (unreviewed) or last updated (reviewed/dismissed).

        Args:
          min_severity: Minimum severity level to include (1-5).

          status: Filter by review status. Defaults to "unreviewed".

          trigger_type: Filter by trigger type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/inbox",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_severity": min_severity,
                        "status": status,
                        "trigger_type": trigger_type,
                    },
                    inbox_list_params.InboxListParams,
                ),
            ),
            cast_to=ListInboxResponse,
        )

    async def get(
        self,
        conversation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetInboxItemResponse:
        """
        Get the full detail of a single inbox item including conversation messages,
        analysis scores, trigger metadata, keywords, and participant information.

        Args:
          conversation_id: The conversation ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_id:
            raise ValueError(f"Expected a non-empty value for `conversation_id` but received {conversation_id!r}")
        return await self._get(
            path_template("/inbox/{conversation_id}", conversation_id=conversation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetInboxItemResponse,
        )


class InboxResourceWithRawResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

        self.list = to_raw_response_wrapper(
            inbox.list,
        )
        self.get = to_raw_response_wrapper(
            inbox.get,
        )


class AsyncInboxResourceWithRawResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

        self.list = async_to_raw_response_wrapper(
            inbox.list,
        )
        self.get = async_to_raw_response_wrapper(
            inbox.get,
        )


class InboxResourceWithStreamingResponse:
    def __init__(self, inbox: InboxResource) -> None:
        self._inbox = inbox

        self.list = to_streamed_response_wrapper(
            inbox.list,
        )
        self.get = to_streamed_response_wrapper(
            inbox.get,
        )


class AsyncInboxResourceWithStreamingResponse:
    def __init__(self, inbox: AsyncInboxResource) -> None:
        self._inbox = inbox

        self.list = async_to_streamed_response_wrapper(
            inbox.list,
        )
        self.get = async_to_streamed_response_wrapper(
            inbox.get,
        )
