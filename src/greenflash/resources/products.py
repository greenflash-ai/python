# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import product_list_params
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
from ..types.get_product_response import GetProductResponse
from ..types.list_products_response import ListProductsResponse
from ..types.get_product_analytics_response import GetProductAnalyticsResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    """Manage products"""

    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

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
    ) -> ListProductsResponse:
        """List all products in your workspace.

        Returns a summary view of each product with
        pagination support. Available on all plans.

        Args:
          page: Page number (default 1).

          page_size: Number of results per page (default 50, max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/products",
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
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ListProductsResponse,
        )

    def get(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetProductResponse:
        """
        Get detailed configuration data for a specific product, including description,
        optimization notes, team members, and quality index metric weights. Available on
        all plans.

        Args:
          product_id: The product ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._get(
            path_template("/products/{product_id}", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetProductResponse,
        )

    def get_product_analytics(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetProductAnalyticsResponse:
        """
        Get comprehensive analytics for a specific product, including sentiment
        analysis, quality scores, safety metrics, topics, root causes, and actionable
        insights.

        **Requires Growth+ plan or higher.**

        Rate limited based on your plan's `maxAnalysesPerHour`.

        Args:
          product_id: The product ID to get analytics for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._get(
            path_template("/products/{product_id}/analytics", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetProductAnalyticsResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    """Manage products"""

    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

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
    ) -> ListProductsResponse:
        """List all products in your workspace.

        Returns a summary view of each product with
        pagination support. Available on all plans.

        Args:
          page: Page number (default 1).

          page_size: Number of results per page (default 50, max 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/products",
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
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ListProductsResponse,
        )

    async def get(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetProductResponse:
        """
        Get detailed configuration data for a specific product, including description,
        optimization notes, team members, and quality index metric weights. Available on
        all plans.

        Args:
          product_id: The product ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._get(
            path_template("/products/{product_id}", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetProductResponse,
        )

    async def get_product_analytics(
        self,
        product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GetProductAnalyticsResponse:
        """
        Get comprehensive analytics for a specific product, including sentiment
        analysis, quality scores, safety metrics, topics, root causes, and actionable
        insights.

        **Requires Growth+ plan or higher.**

        Rate limited based on your plan's `maxAnalysesPerHour`.

        Args:
          product_id: The product ID to get analytics for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._get(
            path_template("/products/{product_id}/analytics", product_id=product_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetProductAnalyticsResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.get = to_raw_response_wrapper(
            products.get,
        )
        self.get_product_analytics = to_raw_response_wrapper(
            products.get_product_analytics,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.get = async_to_raw_response_wrapper(
            products.get,
        )
        self.get_product_analytics = async_to_raw_response_wrapper(
            products.get_product_analytics,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.get = to_streamed_response_wrapper(
            products.get,
        )
        self.get_product_analytics = to_streamed_response_wrapper(
            products.get_product_analytics,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.get = async_to_streamed_response_wrapper(
            products.get,
        )
        self.get_product_analytics = async_to_streamed_response_wrapper(
            products.get_product_analytics,
        )
