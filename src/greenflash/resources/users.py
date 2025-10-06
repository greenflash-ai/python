# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import user_create_params, user_update_params
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
from ..types.create_user_response import CreateUserResponse
from ..types.update_user_response import UpdateUserResponse

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
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        phone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateUserResponse:
        """
        Create or update a user profile with contact information and metadata.

        Provide an `externalUserId` to identify the user. If the user doesn't exist,
        they'll be created. If they already exist, their profile will be updated with
        the information you provide. This makes it easy to keep user data in sync
        without worrying about whether the user exists yet.

        You can then reference this user in other API calls using the same
        `externalUserId`.

        Optionally provide an `externalOrganizationId` to associate the user with an
        organization. If the organization doesn't exist, it will be created
        automatically.

        Args:
          external_user_id: Your unique identifier for the user. Use this same ID in other API calls to
              reference this user.

          anonymized: Whether to anonymize the user's personal information. Defaults to false.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          metadata: Additional data about the user (e.g., plan type, preferences).

          name: The user's full name.

          phone: The user's phone number.

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
                    "metadata": metadata,
                    "name": name,
                    "phone": phone,
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
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        phone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateUserResponse:
        """
        Update an existing user profile with new contact information and metadata.

        The `userId` in the URL path should be your `externalUserId`. Only the fields
        you provide will be updated - all other fields will remain unchanged. This is
        useful when you want to update specific fields without providing the full user
        profile.

        If you prefer a simpler approach where you always provide the complete user
        profile, use `POST /users` instead - it will create or update the user
        automatically.

        Optionally provide an `externalOrganizationId` to associate the user with an
        organization. If the organization doesn't exist, it will be created
        automatically.

        Args:
          user_id: Your external user ID (the externalUserId used when creating the user)

          anonymized: Whether to anonymize the user's personal information.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          metadata: Additional data about the user (e.g., plan type, preferences).

          name: The user's full name.

          phone: The user's phone number.

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
                    "metadata": metadata,
                    "name": name,
                    "phone": phone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateUserResponse,
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
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        phone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateUserResponse:
        """
        Create or update a user profile with contact information and metadata.

        Provide an `externalUserId` to identify the user. If the user doesn't exist,
        they'll be created. If they already exist, their profile will be updated with
        the information you provide. This makes it easy to keep user data in sync
        without worrying about whether the user exists yet.

        You can then reference this user in other API calls using the same
        `externalUserId`.

        Optionally provide an `externalOrganizationId` to associate the user with an
        organization. If the organization doesn't exist, it will be created
        automatically.

        Args:
          external_user_id: Your unique identifier for the user. Use this same ID in other API calls to
              reference this user.

          anonymized: Whether to anonymize the user's personal information. Defaults to false.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          metadata: Additional data about the user (e.g., plan type, preferences).

          name: The user's full name.

          phone: The user's phone number.

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
                    "metadata": metadata,
                    "name": name,
                    "phone": phone,
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
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        phone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateUserResponse:
        """
        Update an existing user profile with new contact information and metadata.

        The `userId` in the URL path should be your `externalUserId`. Only the fields
        you provide will be updated - all other fields will remain unchanged. This is
        useful when you want to update specific fields without providing the full user
        profile.

        If you prefer a simpler approach where you always provide the complete user
        profile, use `POST /users` instead - it will create or update the user
        automatically.

        Optionally provide an `externalOrganizationId` to associate the user with an
        organization. If the organization doesn't exist, it will be created
        automatically.

        Args:
          user_id: Your external user ID (the externalUserId used when creating the user)

          anonymized: Whether to anonymize the user's personal information.

          email: The user's email address.

          external_organization_id: Your unique identifier for the organization this user belongs to. If provided,
              the user will be associated with this organization.

          metadata: Additional data about the user (e.g., plan type, preferences).

          name: The user's full name.

          phone: The user's phone number.

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
                    "metadata": metadata,
                    "name": name,
                    "phone": phone,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateUserResponse,
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


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
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


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
