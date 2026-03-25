# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .inbox_item_summary import InboxItemSummary

__all__ = ["ListInboxResponse"]

ListInboxResponse: TypeAlias = List[InboxItemSummary]
