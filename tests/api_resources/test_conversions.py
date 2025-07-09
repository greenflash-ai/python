# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from greenflash_public_api import GreenflashPublicAPI, AsyncGreenflashPublicAPI
from greenflash_public_api.types import ConversionLogResponse
from greenflash_public_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_log(self, client: GreenflashPublicAPI) -> None:
        conversion = client.conversions.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
        )
        assert_matches_type(ConversionLogResponse, conversion, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_log_with_all_params(self, client: GreenflashPublicAPI) -> None:
        conversion = client.conversions.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
            conversation_id="conv-0001",
            converted_at=parse_datetime("2025-07-09T09:15:00Z"),
            external_conversation_id="externalConversationId",
            metadata={"sku": "ABC-123"},
            product_id="productId",
            project_id="projectId",
        )
        assert_matches_type(ConversionLogResponse, conversion, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_log(self, client: GreenflashPublicAPI) -> None:
        response = client.conversions.with_raw_response.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversion = response.parse()
        assert_matches_type(ConversionLogResponse, conversion, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_log(self, client: GreenflashPublicAPI) -> None:
        with client.conversions.with_streaming_response.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversion = response.parse()
            assert_matches_type(ConversionLogResponse, conversion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConversions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_log(self, async_client: AsyncGreenflashPublicAPI) -> None:
        conversion = await async_client.conversions.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
        )
        assert_matches_type(ConversionLogResponse, conversion, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_log_with_all_params(self, async_client: AsyncGreenflashPublicAPI) -> None:
        conversion = await async_client.conversions.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
            conversation_id="conv-0001",
            converted_at=parse_datetime("2025-07-09T09:15:00Z"),
            external_conversation_id="externalConversationId",
            metadata={"sku": "ABC-123"},
            product_id="productId",
            project_id="projectId",
        )
        assert_matches_type(ConversionLogResponse, conversion, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_log(self, async_client: AsyncGreenflashPublicAPI) -> None:
        response = await async_client.conversions.with_raw_response.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversion = await response.parse()
        assert_matches_type(ConversionLogResponse, conversion, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_log(self, async_client: AsyncGreenflashPublicAPI) -> None:
        async with async_client.conversions.with_streaming_response.log(
            action="purchase",
            external_user_id="user-123",
            value="99.99",
            value_type="currency",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversion = await response.parse()
            assert_matches_type(ConversionLogResponse, conversion, path=["response"])

        assert cast(Any, response.is_closed) is True
