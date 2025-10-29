# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import prompt_list_params, prompt_create_params, prompt_update_params
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
from ..types.get_prompt_response import GetPromptResponse
from ..types.component_input_param import ComponentInputParam
from ..types.list_prompts_response import ListPromptsResponse
from ..types.component_update_param import ComponentUpdateParam
from ..types.create_prompt_response import CreatePromptResponse
from ..types.delete_prompt_response import DeletePromptResponse
from ..types.update_prompt_response import UpdatePromptResponse

__all__ = ["PromptsResource", "AsyncPromptsResource"]


class PromptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return PromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return PromptsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        components: Iterable[ComponentInputParam],
        name: str,
        product_id: str,
        role: str,
        description: str | Omit = omit,
        external_prompt_id: str | Omit = omit,
        source: Literal["customer", "participant", "greenflash", "agent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatePromptResponse:
        """Create a new immutable prompt with one or more components.

        Supports
        handlebars-style variables like `{{variable_name}}` in component content.

        **Versioning behavior:**

        - Creates prompt + components (immutable)
        - Creates a new version with fingerprinting (idempotent)
        - Version is created but NOT activated
        - Activation happens separately via UI or when used by Messages API

        This allows you to create and prepare prompts without affecting production.

        Args:
          components: Array of component objects.

          name: Prompt name.

          product_id: Product this prompt will map to.

          role: Role key in the product mapping (e.g. "agent tool").

          description: Prompt description.

          external_prompt_id: Your external identifier for the prompt.

          source: Prompt source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/prompts",
            body=maybe_transform(
                {
                    "components": components,
                    "name": name,
                    "product_id": product_id,
                    "role": role,
                    "description": description,
                    "external_prompt_id": external_prompt_id,
                    "source": source,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatePromptResponse,
        )

    def update(
        self,
        id: str,
        *,
        components: Iterable[ComponentUpdateParam] | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        role: str | Omit = omit,
        source: Literal["customer", "participant", "greenflash", "agent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdatePromptResponse:
        """Update a prompt.

        Creates a new immutable row (never mutates existing).

        **Versioning behavior:**

        - Always creates a new row if components are provided
        - Creates a new version with fingerprinting (idempotent)
        - Version is created but NOT activated
        - Activation happens separately via UI
        - Old versions continue pointing to old prompts (preserves history)

        If only metadata (name, description) is updated without components, updates the
        existing prompt in-place and does not create a new version.

        Args:
          id: The prompt ID to update

          components: Updated components (if provided, creates new immutable prompt and version).

          description: Updated prompt description.

          name: Updated prompt name.

          role: Role key in the product mapping.

          source: Prompt source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/prompts/{id}",
            body=maybe_transform(
                {
                    "components": components,
                    "description": description,
                    "name": name,
                    "role": role,
                    "source": source,
                },
                prompt_update_params.PromptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdatePromptResponse,
        )

    def list(
        self,
        *,
        active_only: bool | Omit = omit,
        include_archived: bool | Omit = omit,
        limit: float | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListPromptsResponse:
        """List all prompts for your organization.

        By default, returns all prompts (both
        active and inactive versions) across all products. Use `versionId` to filter by
        a specific version, or `productId` to filter by a specific product. Supports
        both cursor-based pagination (using `limit` and `cursor`) and page-based
        pagination (using `page` and `pageSize`). The response includes a Link header
        with pagination navigation URLs following RFC 8288. Returns slimmed down data
        with only component IDs (use GET /prompts/:id for full details).

        Args:
          active_only: Filter to only show prompts that are part of active versions. When true, only
              returns prompts associated with versions where isActive=true.

          include_archived: Include archived prompts.

          limit: Page size limit (cursor-based pagination). Use either limit/cursor OR
              page/pageSize, not both.

          page: Page number (page-based pagination). Use either page/pageSize OR limit/cursor,
              not both.

          page_size: Number of items per page (page-based pagination). Use either page/pageSize OR
              limit/cursor, not both.

          product_id: Filter prompts by product ID.

          version_id: Filter prompts by specific version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/prompts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_only": active_only,
                        "include_archived": include_archived,
                        "limit": limit,
                        "page": page,
                        "page_size": page_size,
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            cast_to=ListPromptsResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletePromptResponse:
        """Archive (soft delete) a prompt.

        Sets the `archived_at` timestamp.

        **Safety constraints:**

        - BLOCKS archiving if the prompt is referenced by any active version
        - You must promote a different version first before archiving
        - Historical versions continue to reference archived prompts (preserves message
          history)
        - Archived prompts can still be retrieved for historical data

        Args:
          id: The prompt ID to archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletePromptResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetPromptResponse:
        """Retrieve a prompt with optional variable interpolation.

        Supports
        handlebars-style variables like `{{variable_name}}` in the prompt content. Pass
        query parameters to interpolate variables.

        **Example:** `/prompts/abc-123?userName=Alice&productName=Premium` will replace
        `{{userName}}` with "Alice" and `{{productName}}` with "Premium" in the composed
        prompt.

        Args:
          id: The prompt identifier. Can be: internal prompt ID (UUID), or externalPromptId
              (your custom ID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetPromptResponse,
        )


class AsyncPromptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncPromptsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        components: Iterable[ComponentInputParam],
        name: str,
        product_id: str,
        role: str,
        description: str | Omit = omit,
        external_prompt_id: str | Omit = omit,
        source: Literal["customer", "participant", "greenflash", "agent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatePromptResponse:
        """Create a new immutable prompt with one or more components.

        Supports
        handlebars-style variables like `{{variable_name}}` in component content.

        **Versioning behavior:**

        - Creates prompt + components (immutable)
        - Creates a new version with fingerprinting (idempotent)
        - Version is created but NOT activated
        - Activation happens separately via UI or when used by Messages API

        This allows you to create and prepare prompts without affecting production.

        Args:
          components: Array of component objects.

          name: Prompt name.

          product_id: Product this prompt will map to.

          role: Role key in the product mapping (e.g. "agent tool").

          description: Prompt description.

          external_prompt_id: Your external identifier for the prompt.

          source: Prompt source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/prompts",
            body=await async_maybe_transform(
                {
                    "components": components,
                    "name": name,
                    "product_id": product_id,
                    "role": role,
                    "description": description,
                    "external_prompt_id": external_prompt_id,
                    "source": source,
                },
                prompt_create_params.PromptCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatePromptResponse,
        )

    async def update(
        self,
        id: str,
        *,
        components: Iterable[ComponentUpdateParam] | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        role: str | Omit = omit,
        source: Literal["customer", "participant", "greenflash", "agent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UpdatePromptResponse:
        """Update a prompt.

        Creates a new immutable row (never mutates existing).

        **Versioning behavior:**

        - Always creates a new row if components are provided
        - Creates a new version with fingerprinting (idempotent)
        - Version is created but NOT activated
        - Activation happens separately via UI
        - Old versions continue pointing to old prompts (preserves history)

        If only metadata (name, description) is updated without components, updates the
        existing prompt in-place and does not create a new version.

        Args:
          id: The prompt ID to update

          components: Updated components (if provided, creates new immutable prompt and version).

          description: Updated prompt description.

          name: Updated prompt name.

          role: Role key in the product mapping.

          source: Prompt source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/prompts/{id}",
            body=await async_maybe_transform(
                {
                    "components": components,
                    "description": description,
                    "name": name,
                    "role": role,
                    "source": source,
                },
                prompt_update_params.PromptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdatePromptResponse,
        )

    async def list(
        self,
        *,
        active_only: bool | Omit = omit,
        include_archived: bool | Omit = omit,
        limit: float | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        product_id: str | Omit = omit,
        version_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListPromptsResponse:
        """List all prompts for your organization.

        By default, returns all prompts (both
        active and inactive versions) across all products. Use `versionId` to filter by
        a specific version, or `productId` to filter by a specific product. Supports
        both cursor-based pagination (using `limit` and `cursor`) and page-based
        pagination (using `page` and `pageSize`). The response includes a Link header
        with pagination navigation URLs following RFC 8288. Returns slimmed down data
        with only component IDs (use GET /prompts/:id for full details).

        Args:
          active_only: Filter to only show prompts that are part of active versions. When true, only
              returns prompts associated with versions where isActive=true.

          include_archived: Include archived prompts.

          limit: Page size limit (cursor-based pagination). Use either limit/cursor OR
              page/pageSize, not both.

          page: Page number (page-based pagination). Use either page/pageSize OR limit/cursor,
              not both.

          page_size: Number of items per page (page-based pagination). Use either page/pageSize OR
              limit/cursor, not both.

          product_id: Filter prompts by product ID.

          version_id: Filter prompts by specific version ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/prompts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_only": active_only,
                        "include_archived": include_archived,
                        "limit": limit,
                        "page": page,
                        "page_size": page_size,
                        "product_id": product_id,
                        "version_id": version_id,
                    },
                    prompt_list_params.PromptListParams,
                ),
            ),
            cast_to=ListPromptsResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeletePromptResponse:
        """Archive (soft delete) a prompt.

        Sets the `archived_at` timestamp.

        **Safety constraints:**

        - BLOCKS archiving if the prompt is referenced by any active version
        - You must promote a different version first before archiving
        - Historical versions continue to reference archived prompts (preserves message
          history)
        - Archived prompts can still be retrieved for historical data

        Args:
          id: The prompt ID to archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeletePromptResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetPromptResponse:
        """Retrieve a prompt with optional variable interpolation.

        Supports
        handlebars-style variables like `{{variable_name}}` in the prompt content. Pass
        query parameters to interpolate variables.

        **Example:** `/prompts/abc-123?userName=Alice&productName=Premium` will replace
        `{{userName}}` with "Alice" and `{{productName}}` with "Premium" in the composed
        prompt.

        Args:
          id: The prompt identifier. Can be: internal prompt ID (UUID), or externalPromptId
              (your custom ID).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/prompts/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetPromptResponse,
        )


class PromptsResourceWithRawResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.create = to_raw_response_wrapper(
            prompts.create,
        )
        self.update = to_raw_response_wrapper(
            prompts.update,
        )
        self.list = to_raw_response_wrapper(
            prompts.list,
        )
        self.delete = to_raw_response_wrapper(
            prompts.delete,
        )
        self.get = to_raw_response_wrapper(
            prompts.get,
        )


class AsyncPromptsResourceWithRawResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.create = async_to_raw_response_wrapper(
            prompts.create,
        )
        self.update = async_to_raw_response_wrapper(
            prompts.update,
        )
        self.list = async_to_raw_response_wrapper(
            prompts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            prompts.delete,
        )
        self.get = async_to_raw_response_wrapper(
            prompts.get,
        )


class PromptsResourceWithStreamingResponse:
    def __init__(self, prompts: PromptsResource) -> None:
        self._prompts = prompts

        self.create = to_streamed_response_wrapper(
            prompts.create,
        )
        self.update = to_streamed_response_wrapper(
            prompts.update,
        )
        self.list = to_streamed_response_wrapper(
            prompts.list,
        )
        self.delete = to_streamed_response_wrapper(
            prompts.delete,
        )
        self.get = to_streamed_response_wrapper(
            prompts.get,
        )


class AsyncPromptsResourceWithStreamingResponse:
    def __init__(self, prompts: AsyncPromptsResource) -> None:
        self._prompts = prompts

        self.create = async_to_streamed_response_wrapper(
            prompts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            prompts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            prompts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            prompts.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            prompts.get,
        )
