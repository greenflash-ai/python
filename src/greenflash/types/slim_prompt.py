# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .slim_prompt_component import SlimPromptComponent

__all__ = ["SlimPrompt"]


class SlimPrompt(BaseModel):
    id: str
    """The Greenflash prompt ID."""

    archived_at: Optional[str] = FieldInfo(alias="archivedAt", default=None)
    """ISO 8601 timestamp when archived, or null if active."""

    components: List[SlimPromptComponent]
    """Array of prompt component IDs that make up this prompt."""

    created_at: str = FieldInfo(alias="createdAt")
    """ISO 8601 timestamp when created."""

    external_prompt_id: Optional[str] = FieldInfo(alias="externalPromptId", default=None)
    """Your external identifier for the prompt."""

    name: Optional[str] = None
    """Prompt name."""

    product_id: Optional[str] = FieldInfo(alias="productId", default=None)
    """The product ID this prompt is associated with."""

    updated_at: str = FieldInfo(alias="updatedAt")
    """ISO 8601 timestamp when last updated."""

    version_id: Optional[str] = FieldInfo(alias="versionId", default=None)
    """
    The version ID this prompt is associated with, or null if the prompt is not part
    of any version.
    """
