# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .component_input_param import ComponentInputParam

__all__ = ["SystemPromptParam"]


class SystemPromptParam(TypedDict, total=False):
    """System prompt as a prompt object.

    Can reference an existing prompt by ID or define new components inline.
    """

    components: Iterable[ComponentInputParam]
    """Array of component objects.

    When provided with promptId/externalPromptId, will upsert the prompt. When
    omitted with promptId/externalPromptId, will reference an existing prompt.
    """

    external_prompt_id: Annotated[str, PropertyInfo(alias="externalPromptId")]
    """Your external identifier for the prompt.

    Can be used to reference an existing prompt created via system prompt APIs.
    """

    prompt_id: Annotated[str, PropertyInfo(alias="promptId")]
    """Greenflash's internal prompt ID.

    Can be used to reference an existing prompt created via system prompt APIs.
    """
