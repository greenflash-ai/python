# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import date

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TenantOrganization"]


class TenantOrganization(BaseModel):
    id: str
    """The Greenflash organization ID."""

    created_at: date = FieldInfo(alias="createdAt")
    """When the organization was first created."""

    metadata: Dict[str, object]
    """Custom metadata for the organization."""

    tenant_id: str = FieldInfo(alias="tenantId")
    """The tenant this organization belongs to."""

    updated_at: date = FieldInfo(alias="updatedAt")
    """When the organization was last updated."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Your external organization ID."""

    name: Optional[str] = None
    """The organization name."""
