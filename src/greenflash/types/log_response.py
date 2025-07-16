# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LogResponse"]


class LogResponse(BaseModel):
    success: bool
    """Indicates whether the API call was successful."""
