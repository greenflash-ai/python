# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from greenflash_public_api import GreenflashAPI, AsyncGreenflashAPI
from greenflash_public_api.types import MessageCreateResponse
from greenflash_public_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: GreenflashAPI) -> None:
        message = client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                        },
                    ],
                    "turn_index": 0,
                }
            ],
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: GreenflashAPI) -> None:
        message = client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                            "context": "context",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "metadata": {"foo": "bar"},
                            "tokens": 1,
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                            "context": "context",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "metadata": {"foo": "bar"},
                            "tokens": 2,
                        },
                    ],
                    "turn_index": 0,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "system_prompt_override": "You are a helpful assistant.",
                }
            ],
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_conversation_id="conv-456",
            metadata={"source": "bar"},
            model="gpt-greenflash-1",
            product_id="123e4567-e89b-12d3-a456-426614174000",
            project_id="123e4567-e89b-12d3-a456-426614174000",
            system_prompt={
                "components": [
                    {
                        "content": "You are a helpful assistant.",
                        "source": "customer",
                        "type": "system",
                        "is_dynamic": True,
                        "name": "name",
                        "tags": ["string"],
                        "version": 0,
                    }
                ],
                "external_template_id": "externalTemplateId",
                "template_id": "tmpl-001",
            },
            version_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: GreenflashAPI) -> None:
        response = client.messages.with_raw_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                        },
                    ],
                    "turn_index": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: GreenflashAPI) -> None:
        with client.messages.with_streaming_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                        },
                    ],
                    "turn_index": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflashAPI) -> None:
        message = await async_client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                        },
                    ],
                    "turn_index": 0,
                }
            ],
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflashAPI) -> None:
        message = await async_client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                            "context": "context",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "metadata": {"foo": "bar"},
                            "tokens": 1,
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                            "context": "context",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "metadata": {"foo": "bar"},
                            "tokens": 2,
                        },
                    ],
                    "turn_index": 0,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "system_prompt_override": "You are a helpful assistant.",
                }
            ],
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_conversation_id="conv-456",
            metadata={"source": "bar"},
            model="gpt-greenflash-1",
            product_id="123e4567-e89b-12d3-a456-426614174000",
            project_id="123e4567-e89b-12d3-a456-426614174000",
            system_prompt={
                "components": [
                    {
                        "content": "You are a helpful assistant.",
                        "source": "customer",
                        "type": "system",
                        "is_dynamic": True,
                        "name": "name",
                        "tags": ["string"],
                        "version": 0,
                    }
                ],
                "external_template_id": "externalTemplateId",
                "template_id": "tmpl-001",
            },
            version_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflashAPI) -> None:
        response = await async_client.messages.with_raw_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                        },
                    ],
                    "turn_index": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageCreateResponse, message, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflashAPI) -> None:
        async with async_client.messages.with_streaming_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "content_type": "text",
                            "message_index": 0,
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "content_type": "text",
                            "message_index": 1,
                            "role": "assistant",
                        },
                    ],
                    "turn_index": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageCreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
