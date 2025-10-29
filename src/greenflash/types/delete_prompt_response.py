# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DeletePromptResponse"]


class DeletePromptResponse(BaseModel):
    archived_at: str = FieldInfo(alias="archivedAt")
    """ISO 8601 timestamp when archived."""

    prompt_id: str = FieldInfo(alias="promptId")
    """The archived prompt ID."""

    external_prompt_id: Optional[str] = FieldInfo(alias="externalPromptId", default=None)
    """The external prompt ID."""
