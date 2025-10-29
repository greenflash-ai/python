# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PromptComponent"]


class PromptComponent(BaseModel):
    id: str
    """The Greenflash component ID."""

    content: str
    """The content of the component."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601 timestamp when created."""

    is_dynamic: Optional[bool] = FieldInfo(alias="isDynamic", default=None)
    """Whether the component content changes dynamically."""

    name: Optional[str] = None
    """Component name."""

    source: str
    """Component source (e.g., customer, participant, greenflash)."""

    type: str
    """Component type (e.g., system, endUser, rag, agent)."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601 timestamp when last updated."""

    external_component_id: Optional[str] = FieldInfo(alias="externalComponentId", default=None)
    """Your external identifier for the component."""
