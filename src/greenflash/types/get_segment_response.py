# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GetSegmentResponse"]


class GetSegmentResponse(BaseModel):
    id: str
    """The segment ID."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the segment was created."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """The user ID who created this segment."""

    description: Optional[str] = None
    """A description of the segment."""

    filters: Dict[str, object]
    """The filter/rule configuration for the segment."""

    icon: Optional[str] = None
    """Icon identifier for the segment."""

    is_favorited: bool = FieldInfo(alias="isFavorited")
    """Whether the segment is favorited."""

    member_count: float = FieldInfo(alias="memberCount")
    """Number of participants in this segment."""

    name: str
    """The segment name."""

    preset_id: Optional[str] = FieldInfo(alias="presetId", default=None)
    """Preset identifier for system segments."""

    type: Literal["system", "custom"]
    """Whether the segment is system-defined or custom."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """When the segment was last updated."""
