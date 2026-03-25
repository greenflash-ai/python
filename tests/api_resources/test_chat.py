# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Greenflash) -> None:
        chat = client.chat.create(
            question="What are the top complaints from enterprise customers this week?",
        )
        assert chat is None

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        chat = client.chat.create(
            question="What are the top complaints from enterprise customers this week?",
            context="Focus on the Customer Support Bot product.",
            conversation_id="conv-abc-123",
            messages=[
                {
                    "content": "Show me sentiment trends for the support bot.",
                    "role": "user",
                },
                {
                    "content": "Based on the last 30 days, sentiment is trending slightly negative (-0.08). The main driver is billing-related frustration, which accounts for 34% of negative conversations.",
                    "role": "assistant",
                },
            ],
            product_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert chat is None

    @parametrize
    def test_raw_response_create(self, client: Greenflash) -> None:
        response = client.chat.with_raw_response.create(
            question="What are the top complaints from enterprise customers this week?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.chat.with_streaming_response.create(
            question="What are the top complaints from enterprise customers this week?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflash) -> None:
        chat = await async_client.chat.create(
            question="What are the top complaints from enterprise customers this week?",
        )
        assert chat is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        chat = await async_client.chat.create(
            question="What are the top complaints from enterprise customers this week?",
            context="Focus on the Customer Support Bot product.",
            conversation_id="conv-abc-123",
            messages=[
                {
                    "content": "Show me sentiment trends for the support bot.",
                    "role": "user",
                },
                {
                    "content": "Based on the last 30 days, sentiment is trending slightly negative (-0.08). The main driver is billing-related frustration, which accounts for 34% of negative conversations.",
                    "role": "assistant",
                },
            ],
            product_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert chat is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.chat.with_raw_response.create(
            question="What are the top complaints from enterprise customers this week?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.chat.with_streaming_response.create(
            question="What are the top complaints from enterprise customers this week?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True
