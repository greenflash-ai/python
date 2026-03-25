# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        chat,
        inbox,
        users,
        events,
        models,
        prompts,
        ratings,
        messages,
        products,
        segments,
        interactions,
        organizations,
    )
    from .resources.chat import ChatResource, AsyncChatResource
    from .resources.inbox import InboxResource, AsyncInboxResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.prompts import PromptsResource, AsyncPromptsResource
    from .resources.ratings import RatingsResource, AsyncRatingsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.products import ProductsResource, AsyncProductsResource
    from .resources.segments import SegmentsResource, AsyncSegmentsResource
    from .resources.interactions import InteractionsResource, AsyncInteractionsResource
    from .resources.organizations import OrganizationsResource, AsyncOrganizationsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Greenflash",
    "AsyncGreenflash",
    "Client",
    "AsyncClient",
]


class Greenflash(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Greenflash client instance.

        This automatically infers the `api_key` argument from the `GREENFLASH_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GREENFLASH_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GREENFLASH_BASE_URL")
        if base_url is None:
            base_url = f"https://www.greenflash.ai/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def messages(self) -> MessagesResource:
        """Capture interactions between users and AI"""
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def interactions(self) -> InteractionsResource:
        """Capture interactions between users and AI"""
        from .resources.interactions import InteractionsResource

        return InteractionsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """Manage users"""
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def ratings(self) -> RatingsResource:
        """Capture interactions between users and AI"""
        from .resources.ratings import RatingsResource

        return RatingsResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        """Manage users"""
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def prompts(self) -> PromptsResource:
        """Manage prompts"""
        from .resources.prompts import PromptsResource

        return PromptsResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        """Stream chat and agentic conversations"""
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def inbox(self) -> InboxResource:
        """Review flagged conversations"""
        from .resources.inbox import InboxResource

        return InboxResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        """Manage AI models"""
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        """Manage products"""
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def segments(self) -> SegmentsResource:
        """Manage user segments"""
        from .resources.segments import SegmentsResource

        return SegmentsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """Capture business events"""
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def with_raw_response(self) -> GreenflashWithRawResponse:
        return GreenflashWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreenflashWithStreamedResponse:
        return GreenflashWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGreenflash(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGreenflash client instance.

        This automatically infers the `api_key` argument from the `GREENFLASH_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GREENFLASH_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GREENFLASH_BASE_URL")
        if base_url is None:
            base_url = f"https://www.greenflash.ai/api/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Capture interactions between users and AI"""
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def interactions(self) -> AsyncInteractionsResource:
        """Capture interactions between users and AI"""
        from .resources.interactions import AsyncInteractionsResource

        return AsyncInteractionsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Manage users"""
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def ratings(self) -> AsyncRatingsResource:
        """Capture interactions between users and AI"""
        from .resources.ratings import AsyncRatingsResource

        return AsyncRatingsResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        """Manage users"""
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        """Manage prompts"""
        from .resources.prompts import AsyncPromptsResource

        return AsyncPromptsResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        """Stream chat and agentic conversations"""
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def inbox(self) -> AsyncInboxResource:
        """Review flagged conversations"""
        from .resources.inbox import AsyncInboxResource

        return AsyncInboxResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        """Manage AI models"""
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        """Manage products"""
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def segments(self) -> AsyncSegmentsResource:
        """Manage user segments"""
        from .resources.segments import AsyncSegmentsResource

        return AsyncSegmentsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Capture business events"""
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGreenflashWithRawResponse:
        return AsyncGreenflashWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreenflashWithStreamedResponse:
        return AsyncGreenflashWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GreenflashWithRawResponse:
    _client: Greenflash

    def __init__(self, client: Greenflash) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """Capture interactions between users and AI"""
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def interactions(self) -> interactions.InteractionsResourceWithRawResponse:
        """Capture interactions between users and AI"""
        from .resources.interactions import InteractionsResourceWithRawResponse

        return InteractionsResourceWithRawResponse(self._client.interactions)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """Manage users"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def ratings(self) -> ratings.RatingsResourceWithRawResponse:
        """Capture interactions between users and AI"""
        from .resources.ratings import RatingsResourceWithRawResponse

        return RatingsResourceWithRawResponse(self._client.ratings)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        """Manage users"""
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        """Manage prompts"""
        from .resources.prompts import PromptsResourceWithRawResponse

        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        """Stream chat and agentic conversations"""
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def inbox(self) -> inbox.InboxResourceWithRawResponse:
        """Review flagged conversations"""
        from .resources.inbox import InboxResourceWithRawResponse

        return InboxResourceWithRawResponse(self._client.inbox)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        """Manage AI models"""
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        """Manage products"""
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def segments(self) -> segments.SegmentsResourceWithRawResponse:
        """Manage user segments"""
        from .resources.segments import SegmentsResourceWithRawResponse

        return SegmentsResourceWithRawResponse(self._client.segments)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        """Capture business events"""
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)


class AsyncGreenflashWithRawResponse:
    _client: AsyncGreenflash

    def __init__(self, client: AsyncGreenflash) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """Capture interactions between users and AI"""
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def interactions(self) -> interactions.AsyncInteractionsResourceWithRawResponse:
        """Capture interactions between users and AI"""
        from .resources.interactions import AsyncInteractionsResourceWithRawResponse

        return AsyncInteractionsResourceWithRawResponse(self._client.interactions)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """Manage users"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def ratings(self) -> ratings.AsyncRatingsResourceWithRawResponse:
        """Capture interactions between users and AI"""
        from .resources.ratings import AsyncRatingsResourceWithRawResponse

        return AsyncRatingsResourceWithRawResponse(self._client.ratings)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        """Manage users"""
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        """Manage prompts"""
        from .resources.prompts import AsyncPromptsResourceWithRawResponse

        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        """Stream chat and agentic conversations"""
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def inbox(self) -> inbox.AsyncInboxResourceWithRawResponse:
        """Review flagged conversations"""
        from .resources.inbox import AsyncInboxResourceWithRawResponse

        return AsyncInboxResourceWithRawResponse(self._client.inbox)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        """Manage AI models"""
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        """Manage products"""
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def segments(self) -> segments.AsyncSegmentsResourceWithRawResponse:
        """Manage user segments"""
        from .resources.segments import AsyncSegmentsResourceWithRawResponse

        return AsyncSegmentsResourceWithRawResponse(self._client.segments)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        """Capture business events"""
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)


class GreenflashWithStreamedResponse:
    _client: Greenflash

    def __init__(self, client: Greenflash) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """Capture interactions between users and AI"""
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def interactions(self) -> interactions.InteractionsResourceWithStreamingResponse:
        """Capture interactions between users and AI"""
        from .resources.interactions import InteractionsResourceWithStreamingResponse

        return InteractionsResourceWithStreamingResponse(self._client.interactions)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """Manage users"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def ratings(self) -> ratings.RatingsResourceWithStreamingResponse:
        """Capture interactions between users and AI"""
        from .resources.ratings import RatingsResourceWithStreamingResponse

        return RatingsResourceWithStreamingResponse(self._client.ratings)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        """Manage users"""
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        """Manage prompts"""
        from .resources.prompts import PromptsResourceWithStreamingResponse

        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        """Stream chat and agentic conversations"""
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def inbox(self) -> inbox.InboxResourceWithStreamingResponse:
        """Review flagged conversations"""
        from .resources.inbox import InboxResourceWithStreamingResponse

        return InboxResourceWithStreamingResponse(self._client.inbox)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        """Manage AI models"""
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        """Manage products"""
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def segments(self) -> segments.SegmentsResourceWithStreamingResponse:
        """Manage user segments"""
        from .resources.segments import SegmentsResourceWithStreamingResponse

        return SegmentsResourceWithStreamingResponse(self._client.segments)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        """Capture business events"""
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)


class AsyncGreenflashWithStreamedResponse:
    _client: AsyncGreenflash

    def __init__(self, client: AsyncGreenflash) -> None:
        self._client = client

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """Capture interactions between users and AI"""
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def interactions(self) -> interactions.AsyncInteractionsResourceWithStreamingResponse:
        """Capture interactions between users and AI"""
        from .resources.interactions import AsyncInteractionsResourceWithStreamingResponse

        return AsyncInteractionsResourceWithStreamingResponse(self._client.interactions)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """Manage users"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def ratings(self) -> ratings.AsyncRatingsResourceWithStreamingResponse:
        """Capture interactions between users and AI"""
        from .resources.ratings import AsyncRatingsResourceWithStreamingResponse

        return AsyncRatingsResourceWithStreamingResponse(self._client.ratings)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        """Manage users"""
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        """Manage prompts"""
        from .resources.prompts import AsyncPromptsResourceWithStreamingResponse

        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        """Stream chat and agentic conversations"""
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def inbox(self) -> inbox.AsyncInboxResourceWithStreamingResponse:
        """Review flagged conversations"""
        from .resources.inbox import AsyncInboxResourceWithStreamingResponse

        return AsyncInboxResourceWithStreamingResponse(self._client.inbox)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        """Manage AI models"""
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        """Manage products"""
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def segments(self) -> segments.AsyncSegmentsResourceWithStreamingResponse:
        """Manage user segments"""
        from .resources.segments import AsyncSegmentsResourceWithStreamingResponse

        return AsyncSegmentsResourceWithStreamingResponse(self._client.segments)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        """Capture business events"""
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)


Client = Greenflash

AsyncClient = AsyncGreenflash
