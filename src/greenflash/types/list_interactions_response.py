# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ListInteractionsResponse", "ListInteractionsResponseItem"]


class ListInteractionsResponseItem(BaseModel):
    id: str
    """The interaction ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the interaction was created."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """Your external identifier for the interaction."""

    external_participant_id: Optional[str] = FieldInfo(alias="externalParticipantId", default=None)
    """Your external identifier for the participant."""

    feedback: Optional[str] = None
    """User feedback text."""

    model: Optional[str] = None
    """The AI model used."""

    organization_external_id: Optional[str] = FieldInfo(alias="organizationExternalId", default=None)
    """Your external identifier for the organization."""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """The organization ID."""

    participant_id: str = FieldInfo(alias="participantId")
    """The user who participated in this interaction."""

    product_id: str = FieldInfo(alias="productId")
    """The product ID."""

    rating: Optional[float] = None
    """User rating for this interaction."""

    rating_max: Optional[float] = FieldInfo(alias="ratingMax", default=None)
    """Maximum rating value."""

    rating_min: Optional[float] = FieldInfo(alias="ratingMin", default=None)
    """Minimum rating value."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the interaction was last updated."""

    version_id: str = FieldInfo(alias="versionId")
    """The version ID."""

    properties: Optional[Dict[str, object]] = None
    """Custom interaction properties."""


ListInteractionsResponse: TypeAlias = List[ListInteractionsResponseItem]
