# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .component_input_param import ComponentInputParam

__all__ = ["SystemPromptParam", "SystemPromptObject"]


class SystemPromptObject(TypedDict, total=False):
    """System prompt as a prompt object.

    Can reference an existing prompt by ID or define new components inline.
    """

    components: Iterable[ComponentInputParam]
    """Array of component objects.

    When provided with promptId/externalPromptId, will upsert the prompt. When
    omitted with promptId/externalPromptId, will reference an existing prompt.
    """

    content: str
    """Simple string content (shorthand for a single system component).

    Mutually exclusive with components.
    """

    external_prompt_id: Annotated[str, PropertyInfo(alias="externalPromptId")]
    """Your external identifier for the prompt.

    Can be used to reference an existing prompt created via system prompt APIs.
    """

    prompt_id: Annotated[str, PropertyInfo(alias="promptId")]
    """Greenflash's internal prompt ID.

    Can be used to reference an existing prompt created via system prompt APIs.
    """

    variables: Dict[str, str]
    """Template variables for {{placeholder}} interpolation in component content."""


SystemPromptParam: TypeAlias = Union[str, SystemPromptObject]
