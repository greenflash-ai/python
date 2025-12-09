# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreateEventResponse"]


class CreateEventResponse(BaseModel):
    """Success response for event creation."""

    event_id: str = FieldInfo(alias="eventId")
    """The unique Greenflash ID of the event record that was created."""

    success: bool
    """Whether the API call was successful."""
