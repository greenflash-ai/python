# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .prompt_component import PromptComponent

__all__ = ["Prompt"]


class Prompt(BaseModel):
    """The full prompt object with components."""

    id: str
    """The Greenflash prompt ID."""

    archived_at: Optional[str] = FieldInfo(alias="archivedAt", default=None)
    """ISO 8601 timestamp when archived, or null if active."""

    components: List[PromptComponent]
    """Array of prompt components that make up this prompt."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601 timestamp when created."""

    description: Optional[str] = None
    """Prompt description."""

    name: Optional[str] = None
    """Prompt name."""

    product_id: Optional[str] = FieldInfo(alias="productId", default=None)
    """The product ID this prompt is associated with."""

    source: Optional[str] = None
    """Prompt source."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601 timestamp when last updated."""

    external_prompt_id: Optional[str] = FieldInfo(alias="externalPromptId", default=None)
    """Your external identifier for the prompt."""
