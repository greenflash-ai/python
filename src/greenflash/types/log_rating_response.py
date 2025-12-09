# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LogRatingResponse"]


class LogRatingResponse(BaseModel):
    """Success response for rating logging."""

    success: bool
    """Whether the API call was successful."""
