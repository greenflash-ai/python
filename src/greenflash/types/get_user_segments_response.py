# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .user_segment_membership import UserSegmentMembership

__all__ = ["GetUserSegmentsResponse"]

GetUserSegmentsResponse: TypeAlias = List[UserSegmentMembership]
