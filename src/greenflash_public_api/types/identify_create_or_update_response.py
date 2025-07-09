# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IdentifyCreateOrUpdateResponse", "Participant"]


class Participant(BaseModel):
    id: str

    anonymized: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    external_id: str = FieldInfo(alias="externalId")

    metadata: object

    tenant_id: str = FieldInfo(alias="tenantId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    email: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None


class IdentifyCreateOrUpdateResponse(BaseModel):
    participant: Participant

    success: bool
