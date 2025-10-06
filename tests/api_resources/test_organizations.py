# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from greenflash import Greenflash, AsyncGreenflash
from tests.utils import assert_matches_type
from greenflash.types import (
    CreateOrganizationResponse,
    UpdateOrganizationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Greenflash) -> None:
        organization = client.organizations.create(
            external_organization_id="org-456",
        )
        assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Greenflash) -> None:
        organization = client.organizations.create(
            external_organization_id="org-456",
            metadata={
                "industry": "bar",
                "size": "bar",
            },
            name="Acme Corporation",
        )
        assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Greenflash) -> None:
        response = client.organizations.with_raw_response.create(
            external_organization_id="org-456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Greenflash) -> None:
        with client.organizations.with_streaming_response.create(
            external_organization_id="org-456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Greenflash) -> None:
        organization = client.organizations.update(
            organization_id="organizationId",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Greenflash) -> None:
        organization = client.organizations.update(
            organization_id="organizationId",
            metadata={
                "industry": "bar",
                "size": "bar",
            },
            name="Updated Organization Name",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Greenflash) -> None:
        response = client.organizations.with_raw_response.update(
            organization_id="organizationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Greenflash) -> None:
        with client.organizations.with_streaming_response.update(
            organization_id="organizationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Greenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.organizations.with_raw_response.update(
                organization_id="",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncGreenflash) -> None:
        organization = await async_client.organizations.create(
            external_organization_id="org-456",
        )
        assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGreenflash) -> None:
        organization = await async_client.organizations.create(
            external_organization_id="org-456",
            metadata={
                "industry": "bar",
                "size": "bar",
            },
            name="Acme Corporation",
        )
        assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.organizations.with_raw_response.create(
            external_organization_id="org-456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGreenflash) -> None:
        async with async_client.organizations.with_streaming_response.create(
            external_organization_id="org-456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(CreateOrganizationResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGreenflash) -> None:
        organization = await async_client.organizations.update(
            organization_id="organizationId",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGreenflash) -> None:
        organization = await async_client.organizations.update(
            organization_id="organizationId",
            metadata={
                "industry": "bar",
                "size": "bar",
            },
            name="Updated Organization Name",
        )
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGreenflash) -> None:
        response = await async_client.organizations.with_raw_response.update(
            organization_id="organizationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGreenflash) -> None:
        async with async_client.organizations.with_streaming_response.update(
            organization_id="organizationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(UpdateOrganizationResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncGreenflash) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.organizations.with_raw_response.update(
                organization_id="",
            )
