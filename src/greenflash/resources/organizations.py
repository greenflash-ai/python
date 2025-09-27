# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import organization_update_params
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

    def update(
        self,
        *,
        name: str,
        external_organization_id: str | Omit = omit,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateOrganizationResponse:
        """
        Update an organization by providing either the Greenflash organization ID or
        your external organization ID.

        **Identification:** You must provide exactly one identifier:

        - `organizationId`: The Greenflash-generated organization ID
        - `externalOrganizationId`: Your external organization ID

        **Note:** The organization must already exist. Use the identify endpoint to
        create new organizations.

        Args:
          name: The organization's name to update.

          external_organization_id: Your external organization ID. Either organizationId or externalOrganizationId
              must be provided.

          organization_id: The Greenflash organization ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/organizations",
            body=maybe_transform(
                {
                    "name": name,
                    "external_organization_id": external_organization_id,
                    "organization_id": organization_id,
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

    async def update(
        self,
        *,
        name: str,
        external_organization_id: str | Omit = omit,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdateOrganizationResponse:
        """
        Update an organization by providing either the Greenflash organization ID or
        your external organization ID.

        **Identification:** You must provide exactly one identifier:

        - `organizationId`: The Greenflash-generated organization ID
        - `externalOrganizationId`: Your external organization ID

        **Note:** The organization must already exist. Use the identify endpoint to
        create new organizations.

        Args:
          name: The organization's name to update.

          external_organization_id: Your external organization ID. Either organizationId or externalOrganizationId
              must be provided.

          organization_id: The Greenflash organization ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/organizations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "external_organization_id": external_organization_id,
                    "organization_id": organization_id,
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

        self.update = to_raw_response_wrapper(
            organizations.update,
        )


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.update = to_streamed_response_wrapper(
            organizations.update,
        )


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
