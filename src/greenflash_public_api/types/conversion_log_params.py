# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversionLogParams"]


class ConversionLogParams(TypedDict, total=False):
    action: Required[str]

    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]

    value: Required[str]

    value_type: Required[Annotated[Literal["currency", "numeric", "text"], PropertyInfo(alias="valueType")]]

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]

    converted_at: Annotated[Union[str, datetime], PropertyInfo(alias="convertedAt", format="iso8601")]

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]

    metadata: object

    product_id: Annotated[str, PropertyInfo(alias="productId")]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
