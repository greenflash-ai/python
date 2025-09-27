# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    name: Required[str]
    """The organization's name to update."""

    external_organization_id: Annotated[str, PropertyInfo(alias="externalOrganizationId")]
    """Your external organization ID.

    Either organizationId or externalOrganizationId must be provided.
    """

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """The Greenflash organization ID."""
