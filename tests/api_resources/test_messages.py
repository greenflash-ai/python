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
            messages=[{}, {}, {}, {}, {}],
        )
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        message = client.messages.create(
            external_user_id="user-123",
            messages=[
                {
                    "content": "Hello!",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "user-msg-1",
                    "input": {"foo": "bar"},
                    "message_type": "user_message",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
                {
                    "content": "Hi there! How can I help you?",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "assistant-msg-1",
                    "input": {"foo": "bar"},
                    "message_type": "user_message",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "assistant",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
                {
                    "content": "Calling search tool",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "tool-call-1",
                    "input": {"query": "bar"},
                    "message_type": "tool_call",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "web_search",
                },
                {
                    "content": "Search completed",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "tool-result-1",
                    "input": {"foo": "bar"},
                    "message_type": "observation",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"results": "bar"},
                    "parent_external_message_id": "tool-call-1",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
                {
                    "content": "Based on the search, today will be sunny with a high of 75°F.",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "final-1",
                    "input": {"foo": "bar"},
                    "message_type": "final_response",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
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
            messages=[{}, {}, {}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.messages.with_streaming_response.create(
            external_user_id="user-123",
            messages=[{}, {}, {}, {}, {}],
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
            messages=[{}, {}, {}, {}, {}],
        )
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        message = await async_client.messages.create(
            external_user_id="user-123",
            messages=[
                {
                    "content": "Hello!",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "user-msg-1",
                    "input": {"foo": "bar"},
                    "message_type": "user_message",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
                {
                    "content": "Hi there! How can I help you?",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "assistant-msg-1",
                    "input": {"foo": "bar"},
                    "message_type": "user_message",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "assistant",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
                {
                    "content": "Calling search tool",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "tool-call-1",
                    "input": {"query": "bar"},
                    "message_type": "tool_call",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "web_search",
                },
                {
                    "content": "Search completed",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "tool-result-1",
                    "input": {"foo": "bar"},
                    "message_type": "observation",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"results": "bar"},
                    "parent_external_message_id": "tool-call-1",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
                {
                    "content": "Based on the search, today will be sunny with a high of 75°F.",
                    "context": "context",
                    "created_at": "createdAt",
                    "external_message_id": "final-1",
                    "input": {"foo": "bar"},
                    "message_type": "final_response",
                    "metadata": {"foo": "bar"},
                    "model_override": "modelOverride",
                    "output": {"foo": "bar"},
                    "parent_external_message_id": "parentExternalMessageId",
                    "parent_message_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "role": "user",
                    "system_prompt_override": "x",
                    "tool_name": "toolName",
                },
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
            messages=[{}, {}, {}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(CreateResponse, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.messages.with_streaming_response.create(
            external_user_id="user-123",
            messages=[{}, {}, {}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(CreateResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
