# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "SegmentCreateParams",
    "Filters",
    "FiltersRule",
    "FiltersRuleUnionMember0",
    "FiltersRuleUnionMember1",
    "FiltersRuleUnionMember2",
    "FiltersRuleUnionMember3",
    "FiltersRuleUnionMember4",
    "FiltersRuleUnionMember5",
    "FiltersDateRange",
]


class SegmentCreateParams(TypedDict, total=False):
    filters: Required[Filters]
    """Filter configuration defining segment membership."""

    description: str
    """A description of the segment purpose."""

    icon: str
    """Icon identifier for the segment (e.g. "Users", "Tag")."""

    name: str
    """Segment name. If omitted, an auto-generated name will be assigned."""


class FiltersRuleUnionMember0(TypedDict, total=False):
    field: Required[Literal["sentiment", "frustration", "struggle", "commercialIntent", "cqi", "rating"]]
    """The analysis metric to filter on."""

    operator: Required[Literal["gt", "lt", "eq", "gte", "lte"]]
    """Comparison operator."""

    type: Required[Literal["analysis"]]
    """Rule based on conversation analysis metrics."""

    value: Required[float]
    """Threshold value for the metric (0-1 scale for most metrics)."""


class FiltersRuleUnionMember1(TypedDict, total=False):
    field: Required[
        Literal[
            "jailbreakDetected",
            "hallucinationDetected",
            "userToxicityDetected",
            "modelToxicityDetected",
            "userBiasDetected",
            "modelBiasDetected",
            "missingCapabilityDetected",
        ]
    ]
    """The flag to filter on."""

    type: Required[Literal["analysis_flag"]]
    """Rule based on detected flags."""

    value: Required[bool]
    """Whether the flag should be true or false."""


class FiltersRuleUnionMember2(TypedDict, total=False):
    key: Required[str]
    """The property key (alphanumeric, dots, hyphens, underscores)."""

    operator: Required[Literal["eq", "neq", "contains", "gt", "lt"]]
    """Comparison operator."""

    type: Required[Literal["property"]]
    """Rule based on user properties."""

    value: Required[Union[str, float, bool]]
    """Value to compare against."""


class FiltersRuleUnionMember3(TypedDict, total=False):
    key: Required[str]
    """The conversation property key."""

    operator: Required[Literal["eq", "neq", "contains", "gt", "lt"]]
    """Comparison operator."""

    type: Required[Literal["conversation_property"]]
    """Rule based on conversation-level properties."""

    value: Required[Union[str, float, bool]]
    """Value to compare against."""


class FiltersRuleUnionMember4(TypedDict, total=False):
    operator: Required[Literal["gte", "lte"]]
    """Comparison operator."""

    type: Required[Literal["conversation_count"]]
    """Rule based on number of conversations."""

    value: Required[int]
    """Conversation count threshold."""


class FiltersRuleUnionMember5(TypedDict, total=False):
    operator: Required[Literal["within", "before"]]
    """Time comparison operator."""

    type: Required[Literal["last_seen"]]
    """Rule based on when the user was last active."""

    value: Required[str]
    """Time duration (e.g. "7d", "24h", "30m")."""


FiltersRule: TypeAlias = Union[
    FiltersRuleUnionMember0,
    FiltersRuleUnionMember1,
    FiltersRuleUnionMember2,
    FiltersRuleUnionMember3,
    FiltersRuleUnionMember4,
    FiltersRuleUnionMember5,
]

_FiltersDateRangeReservedKeywords = TypedDict(
    "_FiltersDateRangeReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class FiltersDateRange(_FiltersDateRangeReservedKeywords, total=False):
    """Optional date range filter."""

    preset: Literal["7d", "30d", "90d", "all"]
    """Preset date range."""

    to: str
    """End date (ISO 8601)."""


class Filters(TypedDict, total=False):
    """Filter configuration defining segment membership."""

    rules: Required[Iterable[FiltersRule]]
    """Array of filter rules. At least one rule is required."""

    date_range: Annotated[FiltersDateRange, PropertyInfo(alias="dateRange")]
    """Optional date range filter."""

    product_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="productIds")]
    """Scope the segment to specific product IDs."""
