# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GenericSuccess"]


class GenericSuccess(BaseModel):
    success: bool

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    system_prompt_component_ids: Optional[List[str]] = FieldInfo(alias="systemPromptComponentIds", default=None)

    system_prompt_template_id: Optional[str] = FieldInfo(alias="systemPromptTemplateId", default=None)
