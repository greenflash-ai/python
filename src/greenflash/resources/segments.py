# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import segment_list_params, segment_create_params, segment_get_segment_analytics_params
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
from ..types.get_segment_response import GetSegmentResponse
from ..types.list_segments_response import ListSegmentsResponse
from ..types.create_segment_response import CreateSegmentResponse
from ..types.get_segment_analytics_response import GetSegmentAnalyticsResponse

__all__ = ["SegmentsResource", "AsyncSegmentsResource"]


class SegmentsResource(SyncAPIResource):
    """Manage user segments"""

    @cached_property
    def with_raw_response(self) -> SegmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return SegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SegmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return SegmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        filters: segment_create_params.Filters,
        description: str | Omit = omit,
        icon: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSegmentResponse:
        """Create a custom user segment based on filter rules.

        Available on all plans,
        limited by your plan's `maxCustomSegments` quota.

        After creation, segment membership is computed asynchronously. The segment will
        be available immediately but member counts may take a few moments to populate.

        Args:
          filters: Filter configuration defining segment membership.

          description: A description of the segment purpose.

          icon: Icon identifier for the segment (e.g. "Users", "Tag").

          name: Segment name. If omitted, an auto-generated name will be assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/segments",
            body=maybe_transform(
                {
                    "filters": filters,
                    "description": description,
                    "icon": icon,
                    "name": name,
                },
                segment_create_params.SegmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSegmentResponse,
        )

    def list(
        self,
        *,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListSegmentsResponse:
        """List all segments in your workspace.

        Returns summary data including member
        counts. Supports pagination.

        Args:
          page: Page number (default: 1).

          page_size: Number of results per page (default: 50, max: 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/segments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    segment_list_params.SegmentListParams,
                ),
            ),
            cast_to=ListSegmentsResponse,
        )

    def get(
        self,
        segment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetSegmentResponse:
        """
        Get detailed information about a specific segment, including its filter
        configuration, description, and metadata. Accepts either a UUID or a preset ID
        for system segments.

        Args:
          segment_id: The segment ID (UUID) or preset ID for system segments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not segment_id:
            raise ValueError(f"Expected a non-empty value for `segment_id` but received {segment_id!r}")
        return self._get(
            path_template("/segments/{segment_id}", segment_id=segment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetSegmentResponse,
        )

    def get_segment_analytics(
        self,
        segment_id: str,
        *,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetSegmentAnalyticsResponse:
        """
        Get aggregated analytics for a specific segment including sentiment, safety
        metrics, topics, keywords, and an LLM-generated summary.

        **Requires Growth+ plan or higher.**

        Rate limited based on your plan's `maxAnalysesPerHour`. Cached results (less
        than 2 hours old) do not consume rate limit points.

        Args:
          segment_id: The segment ID to get analytics for.

          product_id: Filter analytics by product ID.

          version_id: Filter analytics by version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not segment_id:
            raise ValueError(f"Expected a non-empty value for `segment_id` but received {segment_id!r}")
        return self._get(
            path_template("/segments/{segment_id}/analytics", segment_id=segment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    segment_get_segment_analytics_params.SegmentGetSegmentAnalyticsParams,
                ),
            ),
            cast_to=GetSegmentAnalyticsResponse,
        )


class AsyncSegmentsResource(AsyncAPIResource):
    """Manage user segments"""

    @cached_property
    def with_raw_response(self) -> AsyncSegmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncSegmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSegmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncSegmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        filters: segment_create_params.Filters,
        description: str | Omit = omit,
        icon: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateSegmentResponse:
        """Create a custom user segment based on filter rules.

        Available on all plans,
        limited by your plan's `maxCustomSegments` quota.

        After creation, segment membership is computed asynchronously. The segment will
        be available immediately but member counts may take a few moments to populate.

        Args:
          filters: Filter configuration defining segment membership.

          description: A description of the segment purpose.

          icon: Icon identifier for the segment (e.g. "Users", "Tag").

          name: Segment name. If omitted, an auto-generated name will be assigned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/segments",
            body=await async_maybe_transform(
                {
                    "filters": filters,
                    "description": description,
                    "icon": icon,
                    "name": name,
                },
                segment_create_params.SegmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSegmentResponse,
        )

    async def list(
        self,
        *,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListSegmentsResponse:
        """List all segments in your workspace.

        Returns summary data including member
        counts. Supports pagination.

        Args:
          page: Page number (default: 1).

          page_size: Number of results per page (default: 50, max: 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/segments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    segment_list_params.SegmentListParams,
                ),
            ),
            cast_to=ListSegmentsResponse,
        )

    async def get(
        self,
        segment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetSegmentResponse:
        """
        Get detailed information about a specific segment, including its filter
        configuration, description, and metadata. Accepts either a UUID or a preset ID
        for system segments.

        Args:
          segment_id: The segment ID (UUID) or preset ID for system segments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not segment_id:
            raise ValueError(f"Expected a non-empty value for `segment_id` but received {segment_id!r}")
        return await self._get(
            path_template("/segments/{segment_id}", segment_id=segment_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetSegmentResponse,
        )

    async def get_segment_analytics(
        self,
        segment_id: str,
        *,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetSegmentAnalyticsResponse:
        """
        Get aggregated analytics for a specific segment including sentiment, safety
        metrics, topics, keywords, and an LLM-generated summary.

        **Requires Growth+ plan or higher.**

        Rate limited based on your plan's `maxAnalysesPerHour`. Cached results (less
        than 2 hours old) do not consume rate limit points.

        Args:
          segment_id: The segment ID to get analytics for.

          product_id: Filter analytics by product ID.

          version_id: Filter analytics by version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not segment_id:
            raise ValueError(f"Expected a non-empty value for `segment_id` but received {segment_id!r}")
        return await self._get(
            path_template("/segments/{segment_id}/analytics", segment_id=segment_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    segment_get_segment_analytics_params.SegmentGetSegmentAnalyticsParams,
                ),
            ),
            cast_to=GetSegmentAnalyticsResponse,
        )


class SegmentsResourceWithRawResponse:
    def __init__(self, segments: SegmentsResource) -> None:
        self._segments = segments

        self.create = to_raw_response_wrapper(
            segments.create,
        )
        self.list = to_raw_response_wrapper(
            segments.list,
        )
        self.get = to_raw_response_wrapper(
            segments.get,
        )
        self.get_segment_analytics = to_raw_response_wrapper(
            segments.get_segment_analytics,
        )


class AsyncSegmentsResourceWithRawResponse:
    def __init__(self, segments: AsyncSegmentsResource) -> None:
        self._segments = segments

        self.create = async_to_raw_response_wrapper(
            segments.create,
        )
        self.list = async_to_raw_response_wrapper(
            segments.list,
        )
        self.get = async_to_raw_response_wrapper(
            segments.get,
        )
        self.get_segment_analytics = async_to_raw_response_wrapper(
            segments.get_segment_analytics,
        )


class SegmentsResourceWithStreamingResponse:
    def __init__(self, segments: SegmentsResource) -> None:
        self._segments = segments

        self.create = to_streamed_response_wrapper(
            segments.create,
        )
        self.list = to_streamed_response_wrapper(
            segments.list,
        )
        self.get = to_streamed_response_wrapper(
            segments.get,
        )
        self.get_segment_analytics = to_streamed_response_wrapper(
            segments.get_segment_analytics,
        )


class AsyncSegmentsResourceWithStreamingResponse:
    def __init__(self, segments: AsyncSegmentsResource) -> None:
        self._segments = segments

        self.create = async_to_streamed_response_wrapper(
            segments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            segments.list,
        )
        self.get = async_to_streamed_response_wrapper(
            segments.get,
        )
        self.get_segment_analytics = async_to_streamed_response_wrapper(
            segments.get_segment_analytics,
        )
