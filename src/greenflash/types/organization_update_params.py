# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    name: str
    """The organization's name."""

    properties: Dict[str, object]
    """Custom organization properties."""
