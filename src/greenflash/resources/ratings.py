# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import rating_log_params
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
from ..types.log_rating_response import LogRatingResponse

__all__ = ["RatingsResource", "AsyncRatingsResource"]


class RatingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return RatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return RatingsResourceWithStreamingResponse(self)

    def log(
        self,
        *,
        product_id: str,
        rating: float,
        rating_max: float,
        rating_min: float,
        conversation_id: str | Omit = omit,
        external_conversation_id: str | Omit = omit,
        external_message_id: str | Omit = omit,
        feedback: str | Omit = omit,
        message_id: str | Omit = omit,
        rated_at: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRatingResponse:
        """
        Record user feedback and ratings for conversations or individual messages.

        Use this endpoint to collect feedback about response quality or overall
        conversation experiences. You can rate either a specific message (using
        `messageId` or `externalMessageId`) or an entire conversation (using
        `conversationId` or `externalConversationId`).

        Args:
          product_id: The Greenflash product ID to rate.

          rating: The rating value. Must be between ratingMin and ratingMax (inclusive).

          rating_max: The maximum possible rating value (e.g., 5 for a 1-5 scale).

          rating_min: The minimum possible rating value (e.g., 1 for a 1-5 scale).

          conversation_id: The Greenflash conversation ID to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          external_conversation_id: Your external conversation identifier to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          external_message_id: Your external message identifier to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          feedback: Optional text feedback accompanying the rating.

          message_id: The Greenflash message ID to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          rated_at: When the rating was given. Defaults to current time if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ratings",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "rating": rating,
                    "rating_max": rating_max,
                    "rating_min": rating_min,
                    "conversation_id": conversation_id,
                    "external_conversation_id": external_conversation_id,
                    "external_message_id": external_message_id,
                    "feedback": feedback,
                    "message_id": message_id,
                    "rated_at": rated_at,
                },
                rating_log_params.RatingLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogRatingResponse,
        )


class AsyncRatingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncRatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncRatingsResourceWithStreamingResponse(self)

    async def log(
        self,
        *,
        product_id: str,
        rating: float,
        rating_max: float,
        rating_min: float,
        conversation_id: str | Omit = omit,
        external_conversation_id: str | Omit = omit,
        external_message_id: str | Omit = omit,
        feedback: str | Omit = omit,
        message_id: str | Omit = omit,
        rated_at: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRatingResponse:
        """
        Record user feedback and ratings for conversations or individual messages.

        Use this endpoint to collect feedback about response quality or overall
        conversation experiences. You can rate either a specific message (using
        `messageId` or `externalMessageId`) or an entire conversation (using
        `conversationId` or `externalConversationId`).

        Args:
          product_id: The Greenflash product ID to rate.

          rating: The rating value. Must be between ratingMin and ratingMax (inclusive).

          rating_max: The maximum possible rating value (e.g., 5 for a 1-5 scale).

          rating_min: The minimum possible rating value (e.g., 1 for a 1-5 scale).

          conversation_id: The Greenflash conversation ID to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          external_conversation_id: Your external conversation identifier to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          external_message_id: Your external message identifier to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          feedback: Optional text feedback accompanying the rating.

          message_id: The Greenflash message ID to rate. Either conversationId,
              externalConversationId, messageId, or externalMessageId must be provided.

          rated_at: When the rating was given. Defaults to current time if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ratings",
            body=await async_maybe_transform(
                {
                    "product_id": product_id,
                    "rating": rating,
                    "rating_max": rating_max,
                    "rating_min": rating_min,
                    "conversation_id": conversation_id,
                    "external_conversation_id": external_conversation_id,
                    "external_message_id": external_message_id,
                    "feedback": feedback,
                    "message_id": message_id,
                    "rated_at": rated_at,
                },
                rating_log_params.RatingLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogRatingResponse,
        )


class RatingsResourceWithRawResponse:
    def __init__(self, ratings: RatingsResource) -> None:
        self._ratings = ratings

        self.log = to_raw_response_wrapper(
            ratings.log,
        )


class AsyncRatingsResourceWithRawResponse:
    def __init__(self, ratings: AsyncRatingsResource) -> None:
        self._ratings = ratings

        self.log = async_to_raw_response_wrapper(
            ratings.log,
        )


class RatingsResourceWithStreamingResponse:
    def __init__(self, ratings: RatingsResource) -> None:
        self._ratings = ratings

        self.log = to_streamed_response_wrapper(
            ratings.log,
        )


class AsyncRatingsResourceWithStreamingResponse:
    def __init__(self, ratings: AsyncRatingsResource) -> None:
        self._ratings = ratings

        self.log = async_to_streamed_response_wrapper(
            ratings.log,
        )
