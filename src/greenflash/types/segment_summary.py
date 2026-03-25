# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SegmentSummary"]


class SegmentSummary(BaseModel):
    id: str
    """The segment ID."""

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
