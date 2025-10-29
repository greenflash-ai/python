# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SlimPromptComponent"]


class SlimPromptComponent(BaseModel):
    id: str
    """The Greenflash component ID."""

    external_component_id: Optional[str] = FieldInfo(alias="externalComponentId", default=None)
    """Your external identifier for the component."""
