# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreatePromptResponse"]


class CreatePromptResponse(BaseModel):
    component_ids: List[str] = FieldInfo(alias="componentIds")
    """The IDs of the created prompt components."""

    prompt_id: str = FieldInfo(alias="promptId")
    """The created prompt ID."""

    version_id: str = FieldInfo(alias="versionId")
    """The created version ID.

    Version is created but not activated (activation happens via UI or Messages
    API).
    """

    external_prompt_id: Optional[str] = FieldInfo(alias="externalPromptId", default=None)
    """The external prompt ID."""
