# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .participant import Participant

__all__ = ["ListUsersResponse"]

ListUsersResponse: TypeAlias = List[Participant]
