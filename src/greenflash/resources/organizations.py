# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import organization_create_params, organization_update_params
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
from ..types.create_organization_response import CreateOrganizationResponse
from ..types.update_organization_response import UpdateOrganizationResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_organization_id: str,
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateOrganizationResponse:
        """
        Create or update an organization with a unique external identifier.

        Provide an `externalOrganizationId` to identify the organization. If the
        organization doesn't exist, it'll be created. If it already exists, its
        information will be updated with what you provide. This makes it easy to keep
        organization data in sync without worrying about whether the organization exists
        yet.

        You can reference this organization in other API calls (like user creation with
        `/users` or in the `/messages` endpoint) using the same
        `externalOrganizationId`.

        Args:
          external_organization_id: Your unique identifier for the organization. Use this same ID in other API calls
              to reference this organization.

          metadata: Custom metadata for the organization.

          name: The organization's name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organizations",
            body=maybe_transform(
                {
                    "external_organization_id": external_organization_id,
                    "metadata": metadata,
                    "name": name,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateOrganizationResponse,
        )

    def update(
        self,
        organization_id: str,
        *,
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateOrganizationResponse:
        """
        Update an existing organization with new information.

        The `organizationId` in the URL path should be your `externalOrganizationId`.
        Only the fields you provide will be updated - all other fields will remain
        unchanged. This is useful when you want to update specific fields without
        providing the full organization profile.

        If you prefer a simpler approach where you always provide the complete
        organization information, use `POST /organizations` instead - it will create or
        update the organization automatically.

        Args:
          organization_id: Your external organization ID (the externalOrganizationId used when creating the
              organization)

          metadata: Custom metadata for the organization.

          name: The organization's name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._put(
            f"/organizations/{organization_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateOrganizationResponse,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_organization_id: str,
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateOrganizationResponse:
        """
        Create or update an organization with a unique external identifier.

        Provide an `externalOrganizationId` to identify the organization. If the
        organization doesn't exist, it'll be created. If it already exists, its
        information will be updated with what you provide. This makes it easy to keep
        organization data in sync without worrying about whether the organization exists
        yet.

        You can reference this organization in other API calls (like user creation with
        `/users` or in the `/messages` endpoint) using the same
        `externalOrganizationId`.

        Args:
          external_organization_id: Your unique identifier for the organization. Use this same ID in other API calls
              to reference this organization.

          metadata: Custom metadata for the organization.

          name: The organization's name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organizations",
            body=await async_maybe_transform(
                {
                    "external_organization_id": external_organization_id,
                    "metadata": metadata,
                    "name": name,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateOrganizationResponse,
        )

    async def update(
        self,
        organization_id: str,
        *,
        metadata: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateOrganizationResponse:
        """
        Update an existing organization with new information.

        The `organizationId` in the URL path should be your `externalOrganizationId`.
        Only the fields you provide will be updated - all other fields will remain
        unchanged. This is useful when you want to update specific fields without
        providing the full organization profile.

        If you prefer a simpler approach where you always provide the complete
        organization information, use `POST /organizations` instead - it will create or
        update the organization automatically.

        Args:
          organization_id: Your external organization ID (the externalOrganizationId used when creating the
              organization)

          metadata: Custom metadata for the organization.

          name: The organization's name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._put(
            f"/organizations/{organization_id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "name": name,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateOrganizationResponse,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
