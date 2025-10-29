# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .component_update_param import ComponentUpdateParam

__all__ = ["PromptUpdateParams"]


class PromptUpdateParams(TypedDict, total=False):
    components: Iterable[ComponentUpdateParam]
    """Updated components (if provided, creates new immutable prompt and version)."""

    description: str
    """Updated prompt description."""

    name: str
    """Updated prompt name."""

    role: str
    """Role key in the product mapping."""

    source: Literal["customer", "participant", "greenflash", "agent"]
    """Prompt source."""
