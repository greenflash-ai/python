# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import CreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Greenflash) -> None:
        message = client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                        },
                    ]
                }
            ],
        )
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        message = client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                            "content_type": "text",
                            "context": "context",
                            "created_at": "createdAt",
                            "message_index": 0,
                            "metadata": {"foo": "bar"},
                            "tokens": 1,
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                            "content_type": "text",
                            "context": "context",
                            "created_at": "createdAt",
                            "message_index": 1,
                            "metadata": {"foo": "bar"},
                            "tokens": 2,
                        },
                    ],
                    "created_at": "createdAt",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "system_prompt_override": "You are a helpful assistant.",
                    "turn_index": 0,
                }
            ],
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_conversation_id="conv-456",
            metadata={"campaign": "bar"},
            model="gpt-greenflash-1",
            product_id="123e4567-e89b-12d3-a456-426614174001",
            project_id="123e4567-e89b-12d3-a456-426614174002",
            system_prompt={
                "components": [
                    {
                        "content": "You are a helpful assistant.",
                        "component_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "external_component_id": "externalComponentId",
                        "is_dynamic": True,
                        "name": "name",
                        "source": "customer",
                        "tags": ["string"],
                        "type": "system",
                        "version": 0,
                    }
                ],
                "external_template_id": "externalTemplateId",
                "tags": ["string"],
                "template_id": "123e4567-e89b-12d3-a456-426614174004",
            },
            version_id="123e4567-e89b-12d3-a456-426614174003",
        )
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Greenflash) -> None:
        response = client.messages.with_raw_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                        },
                    ]
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.messages.with_streaming_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                        },
                    ]
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(CreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflash) -> None:
        message = await async_client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                        },
                    ]
                }
            ],
        )
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        message = await async_client.messages.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                            "content_type": "text",
                            "context": "context",
                            "created_at": "createdAt",
                            "message_index": 0,
                            "metadata": {"foo": "bar"},
                            "tokens": 1,
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                            "content_type": "text",
                            "context": "context",
                            "created_at": "createdAt",
                            "message_index": 1,
                            "metadata": {"foo": "bar"},
                            "tokens": 2,
                        },
                    ],
                    "created_at": "createdAt",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "system_prompt_override": "You are a helpful assistant.",
                    "turn_index": 0,
                }
            ],
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            external_conversation_id="conv-456",
            metadata={"campaign": "bar"},
            model="gpt-greenflash-1",
            product_id="123e4567-e89b-12d3-a456-426614174001",
            project_id="123e4567-e89b-12d3-a456-426614174002",
            system_prompt={
                "components": [
                    {
                        "content": "You are a helpful assistant.",
                        "component_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "external_component_id": "externalComponentId",
                        "is_dynamic": True,
                        "name": "name",
                        "source": "customer",
                        "tags": ["string"],
                        "type": "system",
                        "version": 0,
                    }
                ],
                "external_template_id": "externalTemplateId",
                "tags": ["string"],
                "template_id": "123e4567-e89b-12d3-a456-426614174004",
            },
            version_id="123e4567-e89b-12d3-a456-426614174003",
        )
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.messages.with_raw_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                        },
                    ]
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.messages.with_streaming_response.create(
            external_user_id="user-123",
            turns=[
                {
                    "messages": [
                        {
                            "content": "Hello!",
                            "role": "user",
                        },
                        {
                            "content": "Hi there!",
                            "role": "assistant",
                        },
                    ]
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(CreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
