# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InboxListParams"]


class InboxListParams(TypedDict, total=False):
    min_severity: Annotated[int, PropertyInfo(alias="minSeverity")]
    """Minimum severity level to include (1-5)."""

    status: Literal["unreviewed", "reviewed", "dismissed"]
    """Filter by review status. Defaults to "unreviewed"."""

    trigger_type: Annotated[
        Literal["guardrail", "expectation_check", "novelty", "manual_review", "revenue_risk"],
        PropertyInfo(alias="triggerType"),
    ]
    """Filter by trigger type."""
