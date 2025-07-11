# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SystemPromptParam", "Component"]


class Component(TypedDict, total=False):
    content: Required[str]

    source: Required[Literal["customer", "participant", "greenflash", "agent"]]

    type: Required[Literal["system", "endUser", "userModified", "rag", "agent"]]

    is_dynamic: Annotated[bool, PropertyInfo(alias="isDynamic")]

    name: str

    tags: List[str]

    version: int


class SystemPromptParam(TypedDict, total=False):
    components: Iterable[Component]

    external_template_id: Annotated[str, PropertyInfo(alias="externalTemplateId")]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
