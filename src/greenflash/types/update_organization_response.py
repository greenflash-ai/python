# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UpdateOrganizationResponse", "Organization"]


class Organization(BaseModel):
    id: str
    """The Greenflash organization ID."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Your external organization ID."""

    name: Optional[str] = None
    """The organization name."""


class UpdateOrganizationResponse(BaseModel):
    organization: Organization
    """The organization that was updated."""

    success: bool
    """Whether the API call was successful."""
