# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversionLogParams"]


class ConversionLogParams(TypedDict, total=False):
    action: Required[str]
    """
    The action or event name that represents the conversion (e.g., "purchase",
    "signup", "upgrade").
    """

    external_user_id: Required[Annotated[str, PropertyInfo(alias="externalUserId")]]
    """The external ID of the user who performed the conversion action."""

    value: Required[str]
    """The value of the conversion. Interpretation depends on valueType."""

    value_type: Required[Annotated[Literal["currency", "numeric", "text"], PropertyInfo(alias="valueType")]]
    """The type of the value. Must be one of: 'currency', 'numeric', or 'text'."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """The internal ID of the conversation that led to the conversion."""

    converted_at: Annotated[str, PropertyInfo(alias="convertedAt")]
    """The timestamp when the conversion occurred.

    If not provided, the current time will be used.
    """

    external_conversation_id: Annotated[str, PropertyInfo(alias="externalConversationId")]
    """Your external identifier for the conversation that led to the conversion."""

    metadata: Dict[str, object]
    """Additional metadata about the conversion as key-value pairs."""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """The ID of the product associated with this conversion."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The ID of the project associated with this conversion."""
