# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from greenflash_public_api import GreenflashPublicAPI, AsyncGreenflashPublicAPI
from greenflash_public_api.types import GenericSuccess
from greenflash_public_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRatings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GreenflashPublicAPI) -> None:
        rating = client.ratings.create(
            rating=4,
            rating_max=5,
            rating_min=1,
        )
        assert_matches_type(GenericSuccess, rating, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GreenflashPublicAPI) -> None:
        rating = client.ratings.create(
            rating=4,
            rating_max=5,
            rating_min=1,
            conversation_id="123e4567-e89b-12d3-a456-426614174000",
            external_conversation_id="externalConversationId",
            feedback="Helpful response!",
            message_id="msg-001",
            rated_at=parse_datetime("2025-07-09T09:00:00Z"),
        )
        assert_matches_type(GenericSuccess, rating, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GreenflashPublicAPI) -> None:
        response = client.ratings.with_raw_response.create(
            rating=4,
            rating_max=5,
            rating_min=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rating = response.parse()
        assert_matches_type(GenericSuccess, rating, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GreenflashPublicAPI) -> None:
        with client.ratings.with_streaming_response.create(
            rating=4,
            rating_max=5,
            rating_min=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rating = response.parse()
            assert_matches_type(GenericSuccess, rating, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRatings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflashPublicAPI) -> None:
        rating = await async_client.ratings.create(
            rating=4,
            rating_max=5,
            rating_min=1,
        )
        assert_matches_type(GenericSuccess, rating, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflashPublicAPI) -> None:
        rating = await async_client.ratings.create(
            rating=4,
            rating_max=5,
            rating_min=1,
            conversation_id="123e4567-e89b-12d3-a456-426614174000",
            external_conversation_id="externalConversationId",
            feedback="Helpful response!",
            message_id="msg-001",
            rated_at=parse_datetime("2025-07-09T09:00:00Z"),
        )
        assert_matches_type(GenericSuccess, rating, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflashPublicAPI) -> None:
        response = await async_client.ratings.with_raw_response.create(
            rating=4,
            rating_max=5,
            rating_min=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rating = await response.parse()
        assert_matches_type(GenericSuccess, rating, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflashPublicAPI) -> None:
        async with async_client.ratings.with_streaming_response.create(
            rating=4,
            rating_max=5,
            rating_min=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rating = await response.parse()
            assert_matches_type(GenericSuccess, rating, path=["response"])

        assert cast(Any, response.is_closed) is True
