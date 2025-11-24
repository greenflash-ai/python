# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import user_list_params, user_create_params, user_update_params, user_get_user_analytics_params
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
from ..types.list_users_response import ListUsersResponse
from ..types.create_user_response import CreateUserResponse
from ..types.update_user_response import UpdateUserResponse
from ..types.get_user_analytics_response import GetUserAnalyticsResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_user_id: str,
        anonymized: bool | Omit = omit,
        email: str | Omit = omit,
        external_organization_id: str | Omit = omit,
        name: str | Omit = omit,
        organization_id: str | Omit = omit,
        phone: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateUserResponse:
        """
        Keep track of who's talking to your AI by creating user profiles with contact
        information and custom properties.

        Provide an `externalUserId` to identify the user—your ID from your own system.
        Don't worry about whether they already exist; we'll create them if they're new
        or update their profile if they already exist. This makes syncing user data
        effortless.

        You can then reference this user in other API calls using the same
        `externalUserId`.

        Optionally associate users with an organization by providing an
        `externalOrganizationId`. If the organization doesn't exist yet, we'll create it
        automatically.

        Args:
          external_user_id: Your unique identifier for the user. Use this same ID in other API calls to
              reference this user.

          anonymized: Whether to anonymize the user's personal information. Defaults to false.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          name: The user's full name.

          organization_id: The Greenflash organization ID that the user belongs to.

          phone: The user's phone number.

          properties: Additional data about the user (e.g., plan type, preferences).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users",
            body=maybe_transform(
                {
                    "external_user_id": external_user_id,
                    "anonymized": anonymized,
                    "email": email,
                    "external_organization_id": external_organization_id,
                    "name": name,
                    "organization_id": organization_id,
                    "phone": phone,
                    "properties": properties,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateUserResponse,
        )

    def update(
        self,
        user_id: str,
        *,
        anonymized: bool | Omit = omit,
        email: str | Omit = omit,
        external_organization_id: str | Omit = omit,
        name: str | Omit = omit,
        organization_id: str | Omit = omit,
        phone: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateUserResponse:
        """
        Update specific fields of an existing user profile without changing everything.

        The `userId` in the URL path should be your `externalUserId`. Only the fields
        you include in your request will be updated—everything else stays the same.
        Perfect for targeted updates like changing an email address or adding new
        properties.

        Prefer a simpler approach? Use `POST /users` instead—it automatically creates or
        updates the user, so you don't need to know if they exist yet.

        Optionally associate the user with an organization by providing an
        `externalOrganizationId`. If the organization doesn't exist yet, we'll create it
        automatically.

        Args:
          user_id: Your external user ID (the externalUserId used when creating the user)

          anonymized: Whether to anonymize the user's personal information.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          name: The user's full name.

          organization_id: The Greenflash organization ID that the user belongs to.

          phone: The user's phone number.

          properties: Additional data about the user (e.g., plan type, preferences).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/users/{user_id}",
            body=maybe_transform(
                {
                    "anonymized": anonymized,
                    "email": email,
                    "external_organization_id": external_organization_id,
                    "name": name,
                    "organization_id": organization_id,
                    "phone": phone,
                    "properties": properties,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateUserResponse,
        )

    def list(
        self,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        organization_id: str | Omit = omit,
        page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUsersResponse:
        """Browse through all the users in your workspace.

        Filter by organization to see
        who belongs to specific teams or companies. Results are paginated for easy
        navigation through large user bases.

        Args:
          limit: Maximum number of results to return.

          offset: Offset for pagination.

          organization_id: Filter users by organization ID.

          page: Page number (used to derive offset = (page-1)\\**limit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "page": page,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=ListUsersResponse,
        )

    def get_user_analytics(
        self,
        user_id: str,
        *,
        mode: Literal["simple", "insights"] | Omit = omit,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetUserAnalyticsResponse:
        """
        Understand how a specific user engages with your AI across all their
        conversations. Track their satisfaction, identify pain points, and spot
        opportunities to improve their experience.

        **⚠️ Requires Growth+ plan or higher**

        **Two modes available:**

        - **simple mode**: Get aggregate metrics like average sentiment, frustration
          levels, and conversation quality. Perfect for user dashboards. No rate
          limiting.
        - **insights mode** (default): Access detailed patterns, recurring topics, and
          AI-generated recommendations specific to this user. Rate limited based on your
          plan's `maxAnalysesPerHour`.

        Returns 404 if the user doesn't exist or has no conversations yet.

        Args:
          user_id: The user ID to get analytics for

          mode: Analysis mode: "simple" returns only numeric aggregates (no rate limiting),
              "insights" includes topics, keywords, and recommendations (rate limited per
              tenant plan).

          product_id: Filter analytics by product ID.

          version_id: Filter analytics by version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/users/{user_id}/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mode": mode,
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    user_get_user_analytics_params.UserGetUserAnalyticsParams,
                ),
            ),
            cast_to=GetUserAnalyticsResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_user_id: str,
        anonymized: bool | Omit = omit,
        email: str | Omit = omit,
        external_organization_id: str | Omit = omit,
        name: str | Omit = omit,
        organization_id: str | Omit = omit,
        phone: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateUserResponse:
        """
        Keep track of who's talking to your AI by creating user profiles with contact
        information and custom properties.

        Provide an `externalUserId` to identify the user—your ID from your own system.
        Don't worry about whether they already exist; we'll create them if they're new
        or update their profile if they already exist. This makes syncing user data
        effortless.

        You can then reference this user in other API calls using the same
        `externalUserId`.

        Optionally associate users with an organization by providing an
        `externalOrganizationId`. If the organization doesn't exist yet, we'll create it
        automatically.

        Args:
          external_user_id: Your unique identifier for the user. Use this same ID in other API calls to
              reference this user.

          anonymized: Whether to anonymize the user's personal information. Defaults to false.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          name: The user's full name.

          organization_id: The Greenflash organization ID that the user belongs to.

          phone: The user's phone number.

          properties: Additional data about the user (e.g., plan type, preferences).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users",
            body=await async_maybe_transform(
                {
                    "external_user_id": external_user_id,
                    "anonymized": anonymized,
                    "email": email,
                    "external_organization_id": external_organization_id,
                    "name": name,
                    "organization_id": organization_id,
                    "phone": phone,
                    "properties": properties,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateUserResponse,
        )

    async def update(
        self,
        user_id: str,
        *,
        anonymized: bool | Omit = omit,
        email: str | Omit = omit,
        external_organization_id: str | Omit = omit,
        name: str | Omit = omit,
        organization_id: str | Omit = omit,
        phone: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateUserResponse:
        """
        Update specific fields of an existing user profile without changing everything.

        The `userId` in the URL path should be your `externalUserId`. Only the fields
        you include in your request will be updated—everything else stays the same.
        Perfect for targeted updates like changing an email address or adding new
        properties.

        Prefer a simpler approach? Use `POST /users` instead—it automatically creates or
        updates the user, so you don't need to know if they exist yet.

        Optionally associate the user with an organization by providing an
        `externalOrganizationId`. If the organization doesn't exist yet, we'll create it
        automatically.

        Args:
          user_id: Your external user ID (the externalUserId used when creating the user)

          anonymized: Whether to anonymize the user's personal information.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          name: The user's full name.

          organization_id: The Greenflash organization ID that the user belongs to.

          phone: The user's phone number.

          properties: Additional data about the user (e.g., plan type, preferences).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "anonymized": anonymized,
                    "email": email,
                    "external_organization_id": external_organization_id,
                    "name": name,
                    "organization_id": organization_id,
                    "phone": phone,
                    "properties": properties,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateUserResponse,
        )

    async def list(
        self,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        organization_id: str | Omit = omit,
        page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListUsersResponse:
        """Browse through all the users in your workspace.

        Filter by organization to see
        who belongs to specific teams or companies. Results are paginated for easy
        navigation through large user bases.

        Args:
          limit: Maximum number of results to return.

          offset: Offset for pagination.

          organization_id: Filter users by organization ID.

          page: Page number (used to derive offset = (page-1)\\**limit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "page": page,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=ListUsersResponse,
        )

    async def get_user_analytics(
        self,
        user_id: str,
        *,
        mode: Literal["simple", "insights"] | Omit = omit,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetUserAnalyticsResponse:
        """
        Understand how a specific user engages with your AI across all their
        conversations. Track their satisfaction, identify pain points, and spot
        opportunities to improve their experience.

        **⚠️ Requires Growth+ plan or higher**

        **Two modes available:**

        - **simple mode**: Get aggregate metrics like average sentiment, frustration
          levels, and conversation quality. Perfect for user dashboards. No rate
          limiting.
        - **insights mode** (default): Access detailed patterns, recurring topics, and
          AI-generated recommendations specific to this user. Rate limited based on your
          plan's `maxAnalysesPerHour`.

        Returns 404 if the user doesn't exist or has no conversations yet.

        Args:
          user_id: The user ID to get analytics for

          mode: Analysis mode: "simple" returns only numeric aggregates (no rate limiting),
              "insights" includes topics, keywords, and recommendations (rate limited per
              tenant plan).

          product_id: Filter analytics by product ID.

          version_id: Filter analytics by version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/users/{user_id}/analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mode": mode,
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    user_get_user_analytics_params.UserGetUserAnalyticsParams,
                ),
            ),
            cast_to=GetUserAnalyticsResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.get_user_analytics = to_raw_response_wrapper(
            users.get_user_analytics,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.get_user_analytics = async_to_raw_response_wrapper(
            users.get_user_analytics,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.get_user_analytics = to_streamed_response_wrapper(
            users.get_user_analytics,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.get_user_analytics = async_to_streamed_response_wrapper(
            users.get_user_analytics,
        )
