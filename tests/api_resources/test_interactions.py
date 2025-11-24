# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import (
    ListInteractionsResponse,
    GetInteractionAnalyticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInteractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Greenflash) -> None:
        interaction = client.interactions.list()
        assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Greenflash) -> None:
        interaction = client.interactions.list(
            limit=1,
            offset=0,
            page=1,
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Greenflash) -> None:
        response = client.interactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interaction = response.parse()
        assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Greenflash) -> None:
        with client.interactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interaction = response.parse()
            assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_interaction_analytics(self, client: Greenflash) -> None:
        interaction = client.interactions.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

    @parametrize
    def test_method_get_interaction_analytics_with_all_params(self, client: Greenflash) -> None:
        interaction = client.interactions.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mode="simple",
        )
        assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

    @parametrize
    def test_raw_response_get_interaction_analytics(self, client: Greenflash) -> None:
        response = client.interactions.with_raw_response.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interaction = response.parse()
        assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

    @parametrize
    def test_streaming_response_get_interaction_analytics(self, client: Greenflash) -> None:
        with client.interactions.with_streaming_response.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interaction = response.parse()
            assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_interaction_analytics(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `interaction_id` but received ''"):
            client.interactions.with_raw_response.get_interaction_analytics(
                interaction_id="",
            )


class TestAsyncInteractions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncGreenflash) -> None:
        interaction = await async_client.interactions.list()
        assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGreenflash) -> None:
        interaction = await async_client.interactions.list(
            limit=1,
            offset=0,
            page=1,
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.interactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interaction = await response.parse()
        assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGreenflash) -> None:
        async with async_client.interactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interaction = await response.parse()
            assert_matches_type(ListInteractionsResponse, interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_interaction_analytics(self, async_client: AsyncGreenflash) -> None:
        interaction = await async_client.interactions.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

    @parametrize
    async def test_method_get_interaction_analytics_with_all_params(self, async_client: AsyncGreenflash) -> None:
        interaction = await async_client.interactions.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mode="simple",
        )
        assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

    @parametrize
    async def test_raw_response_get_interaction_analytics(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.interactions.with_raw_response.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interaction = await response.parse()
        assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

    @parametrize
    async def test_streaming_response_get_interaction_analytics(self, async_client: AsyncGreenflash) -> None:
        async with async_client.interactions.with_streaming_response.get_interaction_analytics(
            interaction_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interaction = await response.parse()
            assert_matches_type(GetInteractionAnalyticsResponse, interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_interaction_analytics(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `interaction_id` but received ''"):
            await async_client.interactions.with_raw_response.get_interaction_analytics(
                interaction_id="",
            )
