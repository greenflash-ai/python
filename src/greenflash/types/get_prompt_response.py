# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .prompt import Prompt
from .._models import BaseModel

__all__ = ["GetPromptResponse"]


class GetPromptResponse(BaseModel):
    composed_prompt: str = FieldInfo(alias="composedPrompt")
    """The prompt with variables interpolated from query parameters."""

    prompt: Prompt
    """The full prompt object with components."""
