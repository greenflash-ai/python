# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import (
    organization_list_params,
    organization_create_params,
    organization_update_params,
    organization_get_organization_analytics_params,
)
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
from ..types.list_organizations_response import ListOrganizationsResponse
from ..types.create_organization_response import CreateOrganizationResponse
from ..types.update_organization_response import UpdateOrganizationResponse
from ..types.get_organization_analytics_response import GetOrganizationAnalyticsResponse

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
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateOrganizationResponse:
        """
        Group your users by company, team, or any organizational structure that makes
        sense for your business.

        Provide an `externalOrganizationId` to identify the organization—your ID from
        your own system. Don't worry about whether it already exists; we'll create it if
        it's new or update it if it already exists. This makes syncing organization data
        effortless.

        Reference this organization when creating users (via `/users`) or logging
        messages (via `/messages`) using the same `externalOrganizationId`. Perfect for
        B2B products where you need to track which company each user belongs to.

        Args:
          external_organization_id: Your unique identifier for the organization. Use this same ID in other API calls
              to reference this organization.

          name: The organization's name.

          properties: Custom organization properties.

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
                    "name": name,
                    "properties": properties,
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
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateOrganizationResponse:
        """
        Update specific fields of an existing organization without changing everything.

        The `organizationId` in the URL path should be your `externalOrganizationId`.
        Only the fields you include in your request will be updated—everything else
        stays the same. Perfect for targeted updates like renaming a company or updating
        properties.

        Prefer a simpler approach? Use `POST /organizations` instead—it automatically
        creates or updates the organization, so you don't need to know if it exists yet.

        Args:
          organization_id: Your external organization ID (the externalOrganizationId used when creating the
              organization)

          name: The organization's name.

          properties: Custom organization properties.

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
                    "name": name,
                    "properties": properties,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateOrganizationResponse,
        )

    def list(
        self,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListOrganizationsResponse:
        """
        Browse through all the organizations (companies, teams, etc.) in your workspace.
        Search for specific organizations or paginate through the full list. Perfect for
        building admin dashboards or organization management interfaces.

        The response includes a `Link` header with URLs for next/previous pages, making
        pagination straightforward.

        Args:
          limit: Maximum number of results to return.

          offset: Offset for pagination.

          page: Page number (used to derive offset = (page-1)\\**limit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/organizations",
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
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            cast_to=ListOrganizationsResponse,
        )

    def get_organization_analytics(
        self,
        organization_id: str,
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
    ) -> GetOrganizationAnalyticsResponse:
        """
        See how an entire organization (company, team, etc.) engages with your AI across
        all their users and conversations. Spot trends, measure satisfaction, and
        identify opportunities to improve the experience for your biggest customers.

        **⚠️ Requires Growth+ plan or higher**

        **Two modes available:**

        - **simple mode**: Get organization-wide metrics like average sentiment,
          frustration levels, commercial intent, and quality scores. Perfect for
          executive dashboards and health monitoring. No rate limiting.
        - **insights mode** (default): Dive into detailed patterns, common topics, and
          AI-generated recommendations for improving this organization's experience.
          Rate limited based on your plan's `maxAnalysesPerHour`.

        If analytics don't exist yet, they'll be generated in real-time from the
        organization's conversations (this may take a few seconds). Returns 404 if the
        organization doesn't exist or has no conversations.

        Args:
          organization_id: The organization ID to get analytics for

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/organizations/{organization_id}/analytics",
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
                    organization_get_organization_analytics_params.OrganizationGetOrganizationAnalyticsParams,
                ),
            ),
            cast_to=GetOrganizationAnalyticsResponse,
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
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateOrganizationResponse:
        """
        Group your users by company, team, or any organizational structure that makes
        sense for your business.

        Provide an `externalOrganizationId` to identify the organization—your ID from
        your own system. Don't worry about whether it already exists; we'll create it if
        it's new or update it if it already exists. This makes syncing organization data
        effortless.

        Reference this organization when creating users (via `/users`) or logging
        messages (via `/messages`) using the same `externalOrganizationId`. Perfect for
        B2B products where you need to track which company each user belongs to.

        Args:
          external_organization_id: Your unique identifier for the organization. Use this same ID in other API calls
              to reference this organization.

          name: The organization's name.

          properties: Custom organization properties.

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
                    "name": name,
                    "properties": properties,
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
        name: str | Omit = omit,
        properties: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateOrganizationResponse:
        """
        Update specific fields of an existing organization without changing everything.

        The `organizationId` in the URL path should be your `externalOrganizationId`.
        Only the fields you include in your request will be updated—everything else
        stays the same. Perfect for targeted updates like renaming a company or updating
        properties.

        Prefer a simpler approach? Use `POST /organizations` instead—it automatically
        creates or updates the organization, so you don't need to know if it exists yet.

        Args:
          organization_id: Your external organization ID (the externalOrganizationId used when creating the
              organization)

          name: The organization's name.

          properties: Custom organization properties.

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
                    "name": name,
                    "properties": properties,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateOrganizationResponse,
        )

    async def list(
        self,
        *,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListOrganizationsResponse:
        """
        Browse through all the organizations (companies, teams, etc.) in your workspace.
        Search for specific organizations or paginate through the full list. Perfect for
        building admin dashboards or organization management interfaces.

        The response includes a `Link` header with URLs for next/previous pages, making
        pagination straightforward.

        Args:
          limit: Maximum number of results to return.

          offset: Offset for pagination.

          page: Page number (used to derive offset = (page-1)\\**limit).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/organizations",
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
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            cast_to=ListOrganizationsResponse,
        )

    async def get_organization_analytics(
        self,
        organization_id: str,
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
    ) -> GetOrganizationAnalyticsResponse:
        """
        See how an entire organization (company, team, etc.) engages with your AI across
        all their users and conversations. Spot trends, measure satisfaction, and
        identify opportunities to improve the experience for your biggest customers.

        **⚠️ Requires Growth+ plan or higher**

        **Two modes available:**

        - **simple mode**: Get organization-wide metrics like average sentiment,
          frustration levels, commercial intent, and quality scores. Perfect for
          executive dashboards and health monitoring. No rate limiting.
        - **insights mode** (default): Dive into detailed patterns, common topics, and
          AI-generated recommendations for improving this organization's experience.
          Rate limited based on your plan's `maxAnalysesPerHour`.

        If analytics don't exist yet, they'll be generated in real-time from the
        organization's conversations (this may take a few seconds). Returns 404 if the
        organization doesn't exist or has no conversations.

        Args:
          organization_id: The organization ID to get analytics for

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
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/organizations/{organization_id}/analytics",
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
                    organization_get_organization_analytics_params.OrganizationGetOrganizationAnalyticsParams,
                ),
            ),
            cast_to=GetOrganizationAnalyticsResponse,
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
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.get_organization_analytics = to_raw_response_wrapper(
            organizations.get_organization_analytics,
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
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.get_organization_analytics = async_to_raw_response_wrapper(
            organizations.get_organization_analytics,
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
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.get_organization_analytics = to_streamed_response_wrapper(
            organizations.get_organization_analytics,
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
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.get_organization_analytics = async_to_streamed_response_wrapper(
            organizations.get_organization_analytics,
        )
