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
    """The ID of the component."""

    external_component_id: Annotated[str, PropertyInfo(alias="externalComponentId")]
    """Your own external identifier for the component."""

    is_dynamic: Annotated[bool, PropertyInfo(alias="isDynamic")]
    """Whether the component is dynamic."""

    name: str
    """Name of the component."""

    source: Literal["customer", "participant", "greenflash", "agent"]
    """Source of the component.

    One of: 'customer', 'participant', 'greenflash', 'agent'. Defaults to
    'customer'.
    """

    tags: List[str]
    """Array of string tags associated with the component."""

    type: Literal["system", "endUser", "userModified", "rag", "agent"]
    """Type of the component.

    One of: 'system', 'endUser', 'userModified', 'rag', 'agent'. Defaults to
    'system'.
    """

    version: float
    """Version of the component."""


class SystemPromptTemplate(TypedDict, total=False):
    components: Required[Iterable[SystemPromptTemplateComponent]]
    """Array of component objects."""

    external_template_id: Annotated[str, PropertyInfo(alias="externalTemplateId")]
    """Your own external identifier for the template."""

    tags: List[str]
    """Array of string tags associated with the template."""

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
    """The ID of the template."""


SystemPromptParam: TypeAlias = Union[str, SystemPromptTemplate]
