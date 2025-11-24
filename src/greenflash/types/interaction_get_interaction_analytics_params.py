# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InteractionGetInteractionAnalyticsParams"]


class InteractionGetInteractionAnalyticsParams(TypedDict, total=False):
    mode: Literal["simple", "insights"]
    """
    Analysis mode: "simple" returns only numeric aggregates (no rate limiting),
    "insights" includes topics, keywords, and recommendations (rate limited per
    tenant plan).
    """
