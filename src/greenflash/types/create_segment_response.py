# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateSegmentResponse"]


class CreateSegmentResponse(BaseModel):
    id: str
    """The created segment ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the segment was created."""

    description: Optional[str] = None
    """Segment description."""

    filters: Dict[str, object]
    """The filter configuration."""

    icon: Optional[str] = None
    """Icon identifier."""

    name: str
    """The segment name."""

    type: Literal["custom"]
    """Always "custom" for API-created segments."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the segment was last updated."""
