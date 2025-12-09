# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .participant import Participant

__all__ = ["UpdateUserResponse"]


class UpdateUserResponse(BaseModel):
    """Success response for user update."""

    participant: Participant
    """The user profile."""

    success: bool
    """Whether the API call was successful."""
