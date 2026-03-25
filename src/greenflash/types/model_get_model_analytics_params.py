# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ModelGetModelAnalyticsParams"]


class ModelGetModelAnalyticsParams(TypedDict, total=False):
    period: Literal["7d", "30d", "90d"]
    """Time period for analytics data: 7d, 30d (default), or 90d."""
