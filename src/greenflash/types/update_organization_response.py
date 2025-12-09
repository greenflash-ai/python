# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .tenant_organization import TenantOrganization

__all__ = ["UpdateOrganizationResponse"]


class UpdateOrganizationResponse(BaseModel):
    """Success response for organization update."""

    organization: TenantOrganization
    """The organization that was created or updated."""

    success: bool
    """Whether the API call was successful."""
