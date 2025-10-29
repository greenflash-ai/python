# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import (
    GetPromptResponse,
    ListPromptsResponse,
    CreatePromptResponse,
    DeletePromptResponse,
    UpdatePromptResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Greenflash) -> None:
        prompt = client.prompts.create(
            components=[{"content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly."}],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
        )
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        prompt = client.prompts.create(
            components=[
                {
                    "content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly.",
                    "component_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_component_id": "externalComponentId",
                    "is_dynamic": False,
                    "name": "Base Instructions",
                    "source": "customer",
                    "type": "system",
                }
            ],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
            description="Standard customer support  prompt",
            external_prompt_id="support-v1",
            source="customer",
        )
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Greenflash) -> None:
        response = client.prompts.with_raw_response.create(
            components=[{"content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly."}],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.prompts.with_streaming_response.create(
            components=[{"content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly."}],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(CreatePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Greenflash) -> None:
        prompt = client.prompts.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Greenflash) -> None:
        prompt = client.prompts.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            components=[
                {
                    "content": "You are a helpful assistant for {{productName}}. Always be polite to {{userName}}.",
                    "component_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_component_id": "externalComponentId",
                    "is_dynamic": True,
                    "name": "Base Instructions V2",
                    "source": "customer",
                    "type": "system",
                }
            ],
            description="Updated description",
            name="Updated Customer Support Prompt",
            role="role",
            source="customer",
        )
        assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Greenflash) -> None:
        response = client.prompts.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Greenflash) -> None:
        with client.prompts.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Greenflash) -> None:
        prompt = client.prompts.list()
        assert_matches_type(ListPromptsResponse, prompt, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Greenflash) -> None:
        prompt = client.prompts.list(
            active_only=True,
            include_archived=True,
            limit=100,
            page=1,
            page_size=1,
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListPromptsResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Greenflash) -> None:
        response = client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(ListPromptsResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Greenflash) -> None:
        with client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(ListPromptsResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Greenflash) -> None:
        prompt = client.prompts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeletePromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Greenflash) -> None:
        response = client.prompts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(DeletePromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Greenflash) -> None:
        with client.prompts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(DeletePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Greenflash) -> None:
        prompt = client.prompts.get(
            "id",
        )
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Greenflash) -> None:
        response = client.prompts.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Greenflash) -> None:
        with client.prompts.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(GetPromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.get(
                "",
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.create(
            components=[{"content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly."}],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
        )
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.create(
            components=[
                {
                    "content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly.",
                    "component_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_component_id": "externalComponentId",
                    "is_dynamic": False,
                    "name": "Base Instructions",
                    "source": "customer",
                    "type": "system",
                }
            ],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
            description="Standard customer support  prompt",
            external_prompt_id="support-v1",
            source="customer",
        )
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.prompts.with_raw_response.create(
            components=[{"content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly."}],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(CreatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.prompts.with_streaming_response.create(
            components=[{"content": "You are a helpful assistant for {{productName}}. Greet {{userName}} warmly."}],
            name="Customer Support Prompt",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(CreatePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            components=[
                {
                    "content": "You are a helpful assistant for {{productName}}. Always be polite to {{userName}}.",
                    "component_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_component_id": "externalComponentId",
                    "is_dynamic": True,
                    "name": "Base Instructions V2",
                    "source": "customer",
                    "type": "system",
                }
            ],
            description="Updated description",
            name="Updated Customer Support Prompt",
            role="role",
            source="customer",
        )
        assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.prompts.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGreenflash) -> None:
        async with async_client.prompts.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(UpdatePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.list()
        assert_matches_type(ListPromptsResponse, prompt, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.list(
            active_only=True,
            include_archived=True,
            limit=100,
            page=1,
            page_size=1,
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListPromptsResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(ListPromptsResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGreenflash) -> None:
        async with async_client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(ListPromptsResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeletePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.prompts.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(DeletePromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGreenflash) -> None:
        async with async_client.prompts.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(DeletePromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncGreenflash) -> None:
        prompt = await async_client.prompts.get(
            "id",
        )
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.prompts.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(GetPromptResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGreenflash) -> None:
        async with async_client.prompts.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(GetPromptResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.get(
                "",
            )
