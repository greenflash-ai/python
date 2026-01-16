# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import CreateEventResponse
from greenflash._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Greenflash) -> None:
        event = client.events.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
        )
        assert_matches_type(CreateEventResponse, event, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        event = client.events.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_conversation_id="externalConversationId",
            external_organization_id="externalOrganizationId",
            external_user_id="externalUserId",
            force_sample=True,
            influence="positive",
            insert_id="insertId",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "bar"},
            quality_impact_score=-1,
            sample_rate=0,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value_type="currency",
        )
        assert_matches_type(CreateEventResponse, event, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Greenflash) -> None:
        response = client.events.with_raw_response.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(CreateEventResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.events.with_streaming_response.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(CreateEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflash) -> None:
        event = await async_client.events.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
        )
        assert_matches_type(CreateEventResponse, event, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        event = await async_client.events.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            external_conversation_id="externalConversationId",
            external_organization_id="externalOrganizationId",
            external_user_id="externalUserId",
            force_sample=True,
            influence="positive",
            insert_id="insertId",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            properties={"foo": "bar"},
            quality_impact_score=-1,
            sample_rate=0,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value_type="currency",
        )
        assert_matches_type(CreateEventResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.events.with_raw_response.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(CreateEventResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.events.with_streaming_response.create(
            event_type="x",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(CreateEventResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
