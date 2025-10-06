# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    metadata: Dict[str, object]
    """Custom metadata for the organization."""

    name: str
    """The organization's name."""
