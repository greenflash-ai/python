# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .component_input_param import ComponentInputParam

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    components: Required[Iterable[ComponentInputParam]]
    """Array of component objects."""

    name: Required[str]
    """Prompt name."""

    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """Product this prompt will map to."""

    role: Required[str]
    """Role key in the product mapping (e.g. "agent tool")."""

    description: str
    """Prompt description."""

    external_prompt_id: Annotated[str, PropertyInfo(alias="externalPromptId")]
    """Your external identifier for the prompt."""

    source: Literal["customer", "participant", "greenflash", "agent"]
    """Prompt source."""
