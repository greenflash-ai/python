# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Participant"]


class Participant(BaseModel):
    id: str
    """The internal ID of the participant."""

    anonymized: bool
    """Whether the participant's personal information is anonymized."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the participant was first created."""

    external_id: str = FieldInfo(alias="externalId")
    """The external ID you provided (matches the externalUserId from the request)."""

    metadata: Dict[str, object]
    """Additional metadata associated with the participant."""

    tenant_id: str = FieldInfo(alias="tenantId")
    """The ID of the tenant this participant belongs to."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the participant was last updated."""

    email: Optional[str] = None
    """The participant's email address."""

    name: Optional[str] = None
    """The participant's full name."""

    phone: Optional[str] = None
    """The participant's phone number."""
