# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserSegmentMembership"]


class UserSegmentMembership(BaseModel):
    id: str
    """The segment ID."""

    name: str
    """The segment name."""

    preset_id: Optional[str] = FieldInfo(alias="presetId", default=None)
    """The preset identifier for system segments, or null for custom segments."""

    type: str
    """The segment type (system or custom)."""
