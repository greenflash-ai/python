# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TenantOrganization"]


class TenantOrganization(BaseModel):
    id: str
    """The Greenflash organization ID."""

    metadata: Dict[str, object]
    """Custom metadata for the organization."""

    tenant_id: str = FieldInfo(alias="tenantId")
    """The tenant this organization belongs to."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the organization was first created."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Your external organization ID."""

    name: Optional[str] = None
    """The organization name."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the organization was last updated."""
