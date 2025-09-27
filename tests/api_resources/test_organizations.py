# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import UpdateOrganizationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Greenflash) -> None:
        organization = client.organizations.update(
            name="Updated Organization Name",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Greenflash) -> None:
        organization = client.organizations.update(
            name="Updated Organization Name",
            external_organization_id="externalOrganizationId",
            organization_id="org-greenflash-123",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Greenflash) -> None:
        response = client.organizations.with_raw_response.update(
            name="Updated Organization Name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Greenflash) -> None:
        with client.organizations.with_streaming_response.update(
            name="Updated Organization Name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncGreenflash) -> None:
        organization = await async_client.organizations.update(
            name="Updated Organization Name",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGreenflash) -> None:
        organization = await async_client.organizations.update(
            name="Updated Organization Name",
            external_organization_id="externalOrganizationId",
            organization_id="org-greenflash-123",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.organizations.with_raw_response.update(
            name="Updated Organization Name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGreenflash) -> None:
        async with async_client.organizations.with_streaming_response.update(
            name="Updated Organization Name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
