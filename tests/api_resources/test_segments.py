# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import (
    GetSegmentResponse,
    ListSegmentsResponse,
    CreateSegmentResponse,
    GetSegmentAnalyticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSegments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Greenflash) -> None:
        segment = client.segments.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ]
            },
        )
        assert_matches_type(CreateSegmentResponse, segment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        segment = client.segments.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ],
                "date_range": {
                    "from": "from",
                    "preset": "7d",
                    "to": "to",
                },
                "product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            description="Users with high commercial intent from the enterprise plan",
            icon="Users",
            name="High-Intent Enterprise Users",
        )
        assert_matches_type(CreateSegmentResponse, segment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Greenflash) -> None:
        response = client.segments.with_raw_response.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = response.parse()
        assert_matches_type(CreateSegmentResponse, segment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.segments.with_streaming_response.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = response.parse()
            assert_matches_type(CreateSegmentResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Greenflash) -> None:
        segment = client.segments.list()
        assert_matches_type(ListSegmentsResponse, segment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Greenflash) -> None:
        segment = client.segments.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(ListSegmentsResponse, segment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Greenflash) -> None:
        response = client.segments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = response.parse()
        assert_matches_type(ListSegmentsResponse, segment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Greenflash) -> None:
        with client.segments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = response.parse()
            assert_matches_type(ListSegmentsResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Greenflash) -> None:
        segment = client.segments.get(
            "segmentId",
        )
        assert_matches_type(GetSegmentResponse, segment, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Greenflash) -> None:
        response = client.segments.with_raw_response.get(
            "segmentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = response.parse()
        assert_matches_type(GetSegmentResponse, segment, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Greenflash) -> None:
        with client.segments.with_streaming_response.get(
            "segmentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = response.parse()
            assert_matches_type(GetSegmentResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `segment_id` but received ''"):
            client.segments.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_segment_analytics(self, client: Greenflash) -> None:
        segment = client.segments.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

    @parametrize
    def test_method_get_segment_analytics_with_all_params(self, client: Greenflash) -> None:
        segment = client.segments.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

    @parametrize
    def test_raw_response_get_segment_analytics(self, client: Greenflash) -> None:
        response = client.segments.with_raw_response.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = response.parse()
        assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

    @parametrize
    def test_streaming_response_get_segment_analytics(self, client: Greenflash) -> None:
        with client.segments.with_streaming_response.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = response.parse()
            assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_segment_analytics(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `segment_id` but received ''"):
            client.segments.with_raw_response.get_segment_analytics(
                segment_id="",
            )


class TestAsyncSegments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ]
            },
        )
        assert_matches_type(CreateSegmentResponse, segment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ],
                "date_range": {
                    "from": "from",
                    "preset": "7d",
                    "to": "to",
                },
                "product_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            description="Users with high commercial intent from the enterprise plan",
            icon="Users",
            name="High-Intent Enterprise Users",
        )
        assert_matches_type(CreateSegmentResponse, segment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.segments.with_raw_response.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ]
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = await response.parse()
        assert_matches_type(CreateSegmentResponse, segment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.segments.with_streaming_response.create(
            filters={
                "rules": [
                    {
                        "field": "commercialIntent",
                        "operator": "gte",
                        "type": "analysis",
                        "value": 0.6,
                    },
                    {
                        "key": "plan",
                        "operator": "eq",
                        "type": "property",
                        "value": "enterprise",
                    },
                ]
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = await response.parse()
            assert_matches_type(CreateSegmentResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.list()
        assert_matches_type(ListSegmentsResponse, segment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(ListSegmentsResponse, segment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.segments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = await response.parse()
        assert_matches_type(ListSegmentsResponse, segment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGreenflash) -> None:
        async with async_client.segments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = await response.parse()
            assert_matches_type(ListSegmentsResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.get(
            "segmentId",
        )
        assert_matches_type(GetSegmentResponse, segment, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.segments.with_raw_response.get(
            "segmentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = await response.parse()
        assert_matches_type(GetSegmentResponse, segment, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncGreenflash) -> None:
        async with async_client.segments.with_streaming_response.get(
            "segmentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = await response.parse()
            assert_matches_type(GetSegmentResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `segment_id` but received ''"):
            await async_client.segments.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_segment_analytics(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

    @parametrize
    async def test_method_get_segment_analytics_with_all_params(self, async_client: AsyncGreenflash) -> None:
        segment = await async_client.segments.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            product_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

    @parametrize
    async def test_raw_response_get_segment_analytics(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.segments.with_raw_response.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        segment = await response.parse()
        assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

    @parametrize
    async def test_streaming_response_get_segment_analytics(self, async_client: AsyncGreenflash) -> None:
        async with async_client.segments.with_streaming_response.get_segment_analytics(
            segment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            segment = await response.parse()
            assert_matches_type(GetSegmentAnalyticsResponse, segment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_segment_analytics(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `segment_id` but received ''"):
            await async_client.segments.with_raw_response.get_segment_analytics(
                segment_id="",
            )
