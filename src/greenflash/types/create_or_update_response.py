# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .participant import Participant

__all__ = ["CreateOrUpdateResponse"]


class CreateOrUpdateResponse(BaseModel):
    participant: Participant
    """The user profile that was created or updated."""

    success: bool
    """Indicates whether the API call was successful."""
