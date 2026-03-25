# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import GetProductResponse, ListProductsResponse, GetProductAnalyticsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Greenflash) -> None:
        product = client.products.list()
        assert_matches_type(ListProductsResponse, product, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Greenflash) -> None:
        product = client.products.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(ListProductsResponse, product, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Greenflash) -> None:
        response = client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ListProductsResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Greenflash) -> None:
        with client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ListProductsResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Greenflash) -> None:
        product = client.products.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetProductResponse, product, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Greenflash) -> None:
        response = client.products.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(GetProductResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Greenflash) -> None:
        with client.products.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(GetProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_product_analytics(self, client: Greenflash) -> None:
        product = client.products.get_product_analytics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetProductAnalyticsResponse, product, path=["response"])

    @parametrize
    def test_raw_response_get_product_analytics(self, client: Greenflash) -> None:
        response = client.products.with_raw_response.get_product_analytics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(GetProductAnalyticsResponse, product, path=["response"])

    @parametrize
    def test_streaming_response_get_product_analytics(self, client: Greenflash) -> None:
        with client.products.with_streaming_response.get_product_analytics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(GetProductAnalyticsResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_product_analytics(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.products.with_raw_response.get_product_analytics(
                "",
            )


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGreenflash) -> None:
        product = await async_client.products.list()
        assert_matches_type(ListProductsResponse, product, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGreenflash) -> None:
        product = await async_client.products.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(ListProductsResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ListProductsResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGreenflash) -> None:
        async with async_client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ListProductsResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGreenflash) -> None:
        product = await async_client.products.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetProductResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.products.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(GetProductResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGreenflash) -> None:
        async with async_client.products.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(GetProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_product_analytics(self, async_client: AsyncGreenflash) -> None:
        product = await async_client.products.get_product_analytics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetProductAnalyticsResponse, product, path=["response"])

    @parametrize
    async def test_raw_response_get_product_analytics(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.products.with_raw_response.get_product_analytics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(GetProductAnalyticsResponse, product, path=["response"])

    @parametrize
    async def test_streaming_response_get_product_analytics(self, async_client: AsyncGreenflash) -> None:
        async with async_client.products.with_streaming_response.get_product_analytics(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(GetProductAnalyticsResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_product_analytics(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.products.with_raw_response.get_product_analytics(
                "",
            )
