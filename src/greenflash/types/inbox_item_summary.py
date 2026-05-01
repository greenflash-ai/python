# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InboxItemSummary"]


class InboxItemSummary(BaseModel):
    conversation_id: str = FieldInfo(alias="conversationId")
    """The conversation ID."""

    message_count: int = FieldInfo(alias="messageCount")
    """Number of chat messages in the conversation."""

    review_status: Literal["unreviewed", "reviewed", "dismissed"] = FieldInfo(alias="reviewStatus")
    """Current review status."""

    timestamp: datetime
    """When the inbox item was created (ISO 8601)."""

    topic: Optional[str] = None
    """Main topic of the conversation."""

    trigger_type: Optional[str] = FieldInfo(alias="triggerType", default=None)
    """Primary trigger type that flagged this conversation."""

    axis: Optional[Literal["attention", "opportunity", "manual"]] = None
    """
    Top-level axis for this item: attention (risk), opportunity (positive signal),
    or manual (team flagged).
    """

    cluster_member_ids: Optional[List[str]] = FieldInfo(alias="clusterMemberIds", default=None)
    """IDs of the other conversations in the cluster."""

    cluster_root_cause: Optional[str] = FieldInfo(alias="clusterRootCause", default=None)
    """Root-cause label that anchors the cluster."""

    cluster_size: Optional[int] = FieldInfo(alias="clusterSize", default=None)
    """
    When this card represents a root-cause cluster, total number of conversations
    sharing the cause.
    """
