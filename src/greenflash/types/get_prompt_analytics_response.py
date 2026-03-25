# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["GetPromptAnalyticsResponse"]


class GetPromptAnalyticsResponse(BaseModel):
    avg_quality_index: Optional[float] = FieldInfo(alias="avgQualityIndex", default=None)
    """Average conversation quality index across all conversations using this prompt."""

    effective_suggestion_count: float = FieldInfo(alias="effectiveSuggestionCount")
    """Suggestion count scoped to active versions only.

    Zero if the prompt is not part of an active version.
    """

    last_used_at: Optional[str] = FieldInfo(alias="lastUsedAt", default=None)
    """ISO 8601 timestamp of the most recent conversation using this prompt."""

    needs_review: bool = FieldInfo(alias="needsReview")
    """Whether the prompt has effective suggestions that need review."""

    suggestion_count: float = FieldInfo(alias="suggestionCount")
    """Total number of suggestions from prompt analyses."""

    total_conversations: float = FieldInfo(alias="totalConversations")
    """Total number of conversations using this prompt."""
