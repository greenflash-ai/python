# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import interaction_list_params, interaction_get_interaction_analytics_params
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
from ..types.list_interactions_response import ListInteractionsResponse
from ..types.get_interaction_analytics_response import GetInteractionAnalyticsResponse

__all__ = ["InteractionsResource", "AsyncInteractionsResource"]


class InteractionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return InteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return InteractionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        page: float | Omit = omit,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListInteractionsResponse:
        """
        Browse through all conversations in your workspace to understand how users are
        interacting with your AI. Filter by product or version to focus on specific
        areas of your application.

        Args:
          limit: Maximum number of results to return.

          offset: Offset for pagination.

          page: Page number

          product_id: Filter interactions by product ID.

          version_id: Filter interactions by version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/interactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "page": page,
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    interaction_list_params.InteractionListParams,
                ),
            ),
            cast_to=ListInteractionsResponse,
        )

    def get_interaction_analytics(
        self,
        interaction_id: str,
        *,
        mode: Literal["simple", "insights"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetInteractionAnalyticsResponse:
        """
        Understand what happened in a specific conversation with AI-powered analysis.
        See sentiment shifts, detect frustration, identify commercial intent, and get
        actionable insights.

        **⚠️ Requires Growth+ plan or higher**

        **Two modes available:**

        - **simple mode**: Get just the numbers—sentiment scores, frustration levels,
          and key metrics. Perfect for dashboards and quick checks. No rate limiting.
        - **insights mode** (default): Dive deeper with detailed keywords, insights, and
          AI-generated suggestions for improvement. Rate limited based on your plan's
          `maxAnalysesPerHour`.

        Returns 404 if the conversation doesn't exist or hasn't been analyzed yet.

        Args:
          interaction_id: The interaction ID to get analytics for

          mode: Analysis mode: "simple" returns only numeric aggregates (no rate limiting),
              "insights" includes topics, keywords, and recommendations (rate limited per
              tenant plan).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not interaction_id:
            raise ValueError(f"Expected a non-empty value for `interaction_id` but received {interaction_id!r}")
        return self._get(
            f"/interactions/{interaction_id}/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"mode": mode},
                    interaction_get_interaction_analytics_params.InteractionGetInteractionAnalyticsParams,
                ),
            ),
            cast_to=GetInteractionAnalyticsResponse,
        )


class AsyncInteractionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncInteractionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        page: float | Omit = omit,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListInteractionsResponse:
        """
        Browse through all conversations in your workspace to understand how users are
        interacting with your AI. Filter by product or version to focus on specific
        areas of your application.

        Args:
          limit: Maximum number of results to return.

          offset: Offset for pagination.

          page: Page number

          product_id: Filter interactions by product ID.

          version_id: Filter interactions by version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/interactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "page": page,
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    interaction_list_params.InteractionListParams,
                ),
            ),
            cast_to=ListInteractionsResponse,
        )

    async def get_interaction_analytics(
        self,
        interaction_id: str,
        *,
        mode: Literal["simple", "insights"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetInteractionAnalyticsResponse:
        """
        Understand what happened in a specific conversation with AI-powered analysis.
        See sentiment shifts, detect frustration, identify commercial intent, and get
        actionable insights.

        **⚠️ Requires Growth+ plan or higher**

        **Two modes available:**

        - **simple mode**: Get just the numbers—sentiment scores, frustration levels,
          and key metrics. Perfect for dashboards and quick checks. No rate limiting.
        - **insights mode** (default): Dive deeper with detailed keywords, insights, and
          AI-generated suggestions for improvement. Rate limited based on your plan's
          `maxAnalysesPerHour`.

        Returns 404 if the conversation doesn't exist or hasn't been analyzed yet.

        Args:
          interaction_id: The interaction ID to get analytics for

          mode: Analysis mode: "simple" returns only numeric aggregates (no rate limiting),
              "insights" includes topics, keywords, and recommendations (rate limited per
              tenant plan).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not interaction_id:
            raise ValueError(f"Expected a non-empty value for `interaction_id` but received {interaction_id!r}")
        return await self._get(
            f"/interactions/{interaction_id}/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"mode": mode},
                    interaction_get_interaction_analytics_params.InteractionGetInteractionAnalyticsParams,
                ),
            ),
            cast_to=GetInteractionAnalyticsResponse,
        )


class InteractionsResourceWithRawResponse:
    def __init__(self, interactions: InteractionsResource) -> None:
        self._interactions = interactions

        self.list = to_raw_response_wrapper(
            interactions.list,
        )
        self.get_interaction_analytics = to_raw_response_wrapper(
            interactions.get_interaction_analytics,
        )


class AsyncInteractionsResourceWithRawResponse:
    def __init__(self, interactions: AsyncInteractionsResource) -> None:
        self._interactions = interactions

        self.list = async_to_raw_response_wrapper(
            interactions.list,
        )
        self.get_interaction_analytics = async_to_raw_response_wrapper(
            interactions.get_interaction_analytics,
        )


class InteractionsResourceWithStreamingResponse:
    def __init__(self, interactions: InteractionsResource) -> None:
        self._interactions = interactions

        self.list = to_streamed_response_wrapper(
            interactions.list,
        )
        self.get_interaction_analytics = to_streamed_response_wrapper(
            interactions.get_interaction_analytics,
        )


class AsyncInteractionsResourceWithStreamingResponse:
    def __init__(self, interactions: AsyncInteractionsResource) -> None:
        self._interactions = interactions

        self.list = async_to_streamed_response_wrapper(
            interactions.list,
        )
        self.get_interaction_analytics = async_to_streamed_response_wrapper(
            interactions.get_interaction_analytics,
        )
