# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ParticipantInfo"]


class ParticipantInfo(BaseModel):
    """Participant information."""

    id: str
    """Participant ID."""

    email: Optional[str] = None
    """Participant email."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """External participant ID."""

    name: Optional[str] = None
    """Participant name."""
