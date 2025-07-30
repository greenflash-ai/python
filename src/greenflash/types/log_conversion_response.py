# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LogConversionResponse"]


class LogConversionResponse(BaseModel):
    conversion_id: str = FieldInfo(alias="conversionId")
    """The unique Greenflash ID of the conversion record that was created."""

    success: bool
    """Whether the API call was successful."""
