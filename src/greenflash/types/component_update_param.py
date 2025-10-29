# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComponentUpdateParam"]


class ComponentUpdateParam(TypedDict, total=False):
    content: Required[str]
    """Updated component content."""

    component_id: Annotated[str, PropertyInfo(alias="componentId")]
    """The Greenflash component ID."""

    external_component_id: Annotated[str, PropertyInfo(alias="externalComponentId")]
    """External component identifier."""

    is_dynamic: Annotated[bool, PropertyInfo(alias="isDynamic")]
    """Dynamic flag."""

    name: str
    """Component name."""

    source: Literal["customer", "participant", "greenflash", "agent"]
    """Component source."""

    type: Literal["system", "endUser", "userModified", "rag", "agent"]
    """Component type."""
