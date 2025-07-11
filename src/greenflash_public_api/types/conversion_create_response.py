# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .generic_success import GenericSuccess

__all__ = ["ConversionCreateResponse"]


class ConversionCreateResponse(GenericSuccess):
    conversion_id: str = FieldInfo(alias="conversionId")
