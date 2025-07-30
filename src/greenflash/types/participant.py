# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Participant"]


class Participant(BaseModel):
    id: str
    """The Greenflash participant ID."""

    anonymized: bool
    """Whether the participant's personal information is anonymized."""

    created_at: str = FieldInfo(alias="createdAt")
    """When the participant was first created."""

    external_id: str = FieldInfo(alias="externalId")
    """Your external user ID (matches the externalUserId from the request)."""

    metadata: Dict[str, object]
    """Additional data about the participant."""

    tenant_id: str = FieldInfo(alias="tenantId")
    """The tenant this participant belongs to."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """When the participant was last updated."""

    email: Optional[str] = None
    """The participant's email address."""

    name: Optional[str] = None
    """The participant's full name."""

    phone: Optional[str] = None
    """The participant's phone number."""
