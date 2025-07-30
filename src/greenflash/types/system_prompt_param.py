# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SystemPromptParam", "SystemPromptTemplate", "SystemPromptTemplateComponent"]


class SystemPromptTemplateComponent(TypedDict, total=False):
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
    """Component source: customer, participant, greenflash, or agent.

    Defaults to customer.
    """

    tags: List[str]
    """Tags to categorize the component."""

    type: Literal["system", "endUser", "userModified", "rag", "agent"]
    """Component type: system, endUser, userModified, rag, or agent.

    Defaults to system.
    """

    version: float
    """Component version number."""


class SystemPromptTemplate(TypedDict, total=False):
    components: Required[Iterable[SystemPromptTemplateComponent]]
    """Array of component objects."""

    external_template_id: Annotated[str, PropertyInfo(alias="externalTemplateId")]
    """Your external identifier for the template."""

    tags: List[str]
    """Tags to categorize the template."""

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
    """The Greenflash template ID."""


SystemPromptParam: TypeAlias = Union[str, SystemPromptTemplate]
