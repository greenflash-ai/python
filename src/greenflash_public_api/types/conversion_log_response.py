# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .generic_success import GenericSuccess

__all__ = ["ConversionLogResponse"]


class ConversionLogResponse(GenericSuccess):
    conversion_id: str = FieldInfo(alias="conversionId")
