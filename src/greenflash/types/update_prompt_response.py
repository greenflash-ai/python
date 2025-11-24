# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UpdatePromptResponse"]


class UpdatePromptResponse(BaseModel):
    prompt_id: str = FieldInfo(alias="promptId")
    """The updated prompt ID."""

    version_id: Optional[str] = FieldInfo(alias="versionId", default=None)
    """The version ID.

    Version is created/updated but not activated (activation happens via UI). Null
    if only prompt metadata was updated without components.
    """

    external_prompt_id: Optional[str] = FieldInfo(alias="externalPromptId", default=None)
    """The external prompt ID."""
