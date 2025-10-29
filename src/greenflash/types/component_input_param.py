# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComponentInputParam"]


class ComponentInputParam(TypedDict, total=False):
    content: Required[str]
    """The content of the component."""

    component_id: Annotated[str, PropertyInfo(alias="componentId")]
    """The Greenflash component ID."""

    external_component_id: Annotated[str, PropertyInfo(alias="externalComponentId")]
    """Your external identifier for the component."""

    is_dynamic: Annotated[bool, PropertyInfo(alias="isDynamic")]
    """Whether the component content changes dynamically."""

    name: str
    """Component name."""

    source: Literal["customer", "participant", "greenflash", "agent"]
    """Component source: customer, participant, greenflash, or agent."""

    type: Literal["system", "endUser", "userModified", "rag", "agent"]
    """Component type: system, endUser, userModified, rag, or agent."""
