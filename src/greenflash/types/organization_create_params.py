# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    external_organization_id: Required[Annotated[str, PropertyInfo(alias="externalOrganizationId")]]
    """Your unique identifier for the organization.

    Use this same ID in other API calls to reference this organization.
    """

    metadata: Dict[str, object]
    """Custom metadata for the organization."""

    name: str
    """The organization's name."""
