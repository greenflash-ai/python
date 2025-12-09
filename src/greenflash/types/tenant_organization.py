# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TenantOrganization"]


class TenantOrganization(BaseModel):
    """The organization that was created or updated."""

    id: str
    """The Greenflash organization ID."""

    properties: Dict[str, object]
    """Custom organization properties."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the organization was first created."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Your external organization ID."""

    name: Optional[str] = None
    """The organization name."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the organization was last updated."""
