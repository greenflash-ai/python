# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import identify_create_or_update_params
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
from ..types.create_or_update_response import CreateOrUpdateResponse

__all__ = ["IdentifyResource", "AsyncIdentifyResource"]


class IdentifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return IdentifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return IdentifyResourceWithStreamingResponse(self)

    def create_or_update(
        self,
        *,
        external_user_id: str,
        anonymized: bool | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateOrUpdateResponse:
        """
        The `/identify` endpoint allows you to create or update user profiles in the
        system. This endpoint is used to manage user identity information that can be
        referenced in other API calls using the `externalUserId`.

        When you call this endpoint with an `externalUserId` that already exists, the
        user profile will be updated. If the `externalUserId` doesn't exist yet, a new
        profile will be created.

        Args:
          external_user_id: Your unique identifier for the user. This is used to reference the user in other
              API calls.

          anonymized: Whether the user's personal information should be anonymized. Defaults to false
              for new users.

          email: The user's email address. Must be a valid email format.

          metadata: Additional metadata associated with the user as key-value pairs.

          name: The user's full name.

          phone: The user's phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/identify",
            body=maybe_transform(
                {
                    "external_user_id": external_user_id,
                    "anonymized": anonymized,
                    "email": email,
                    "metadata": metadata,
                    "name": name,
                    "phone": phone,
                },
                identify_create_or_update_params.IdentifyCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateOrUpdateResponse,
        )


class AsyncIdentifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncIdentifyResourceWithStreamingResponse(self)

    async def create_or_update(
        self,
        *,
        external_user_id: str,
        anonymized: bool | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateOrUpdateResponse:
        """
        The `/identify` endpoint allows you to create or update user profiles in the
        system. This endpoint is used to manage user identity information that can be
        referenced in other API calls using the `externalUserId`.

        When you call this endpoint with an `externalUserId` that already exists, the
        user profile will be updated. If the `externalUserId` doesn't exist yet, a new
        profile will be created.

        Args:
          external_user_id: Your unique identifier for the user. This is used to reference the user in other
              API calls.

          anonymized: Whether the user's personal information should be anonymized. Defaults to false
              for new users.

          email: The user's email address. Must be a valid email format.

          metadata: Additional metadata associated with the user as key-value pairs.

          name: The user's full name.

          phone: The user's phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/identify",
            body=await async_maybe_transform(
                {
                    "external_user_id": external_user_id,
                    "anonymized": anonymized,
                    "email": email,
                    "metadata": metadata,
                    "name": name,
                    "phone": phone,
                },
                identify_create_or_update_params.IdentifyCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateOrUpdateResponse,
        )


class IdentifyResourceWithRawResponse:
    def __init__(self, identify: IdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = to_raw_response_wrapper(
            identify.create_or_update,
        )


class AsyncIdentifyResourceWithRawResponse:
    def __init__(self, identify: AsyncIdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = async_to_raw_response_wrapper(
            identify.create_or_update,
        )


class IdentifyResourceWithStreamingResponse:
    def __init__(self, identify: IdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = to_streamed_response_wrapper(
            identify.create_or_update,
        )


class AsyncIdentifyResourceWithStreamingResponse:
    def __init__(self, identify: AsyncIdentifyResource) -> None:
        self._identify = identify

        self.create_or_update = async_to_streamed_response_wrapper(
            identify.create_or_update,
        )
