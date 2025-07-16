# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import CreateOrUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_or_update(self, client: Greenflash) -> None:
        identify = client.identify.create_or_update(
            external_user_id="user-123",
        )
        assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Greenflash) -> None:
        identify = client.identify.create_or_update(
            external_user_id="user-123",
            anonymized=False,
            email="alice@example.com",
            metadata={"plan": "bar"},
            name="Alice Example",
            phone="+15551234567",
        )
        assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

    @parametrize
    def test_raw_response_create_or_update(self, client: Greenflash) -> None:
        response = client.identify.with_raw_response.create_or_update(
            external_user_id="user-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identify = response.parse()
        assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update(self, client: Greenflash) -> None:
        with client.identify.with_streaming_response.create_or_update(
            external_user_id="user-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identify = response.parse()
            assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIdentify:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncGreenflash) -> None:
        identify = await async_client.identify.create_or_update(
            external_user_id="user-123",
        )
        assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncGreenflash) -> None:
        identify = await async_client.identify.create_or_update(
            external_user_id="user-123",
            anonymized=False,
            email="alice@example.com",
            metadata={"plan": "bar"},
            name="Alice Example",
            phone="+15551234567",
        )
        assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.identify.with_raw_response.create_or_update(
            external_user_id="user-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identify = await response.parse()
        assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncGreenflash) -> None:
        async with async_client.identify.with_streaming_response.create_or_update(
            external_user_id="user-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identify = await response.parse()
            assert_matches_type(CreateOrUpdateResponse, identify, path=["response"])

        assert cast(Any, response.is_closed) is True
