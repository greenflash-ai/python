# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import message_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.create_response import CreateResponse
from ..types.turn_item_param import TurnItemParam
from ..types.system_prompt_param import SystemPromptParam

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_user_id: str,
        turns: Iterable[TurnItemParam],
        conversation_id: str | NotGiven = NOT_GIVEN,
        external_conversation_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        system_prompt: SystemPromptParam | NotGiven = NOT_GIVEN,
        version_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateResponse:
        """
        The `/messages` endpoint allows you to log messages between your users and your
        products.

        Full conversations can be logged all at once in a single request with multiple
        turns, or sequentially over multiple requests with a single turn per request.

        The simplest way to log a message is to pass the `role` and `content` of the
        message to the API along with an `externalConversationId` for the converasation
        and your `productId`.

        However, we recommend that you pass as much information about the conversation
        as possible to allow you to analyze and optimize your prompts, models, and more.

        Args:
          external_user_id: The external user ID that will be mapped to a participant in our system.

          turns: An array of conversation turns, each containing messages exchanged during that
              turn.

          conversation_id: The conversation ID. When provided, this will update an existing conversation
              instead of creating a new one. Either conversationId, externalConversationId,
              productId, or projectId must be provided.

          external_conversation_id: Your own external identifier for the conversation. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          metadata: Additional metadata for the conversation.

          model: The AI model used for the conversation.

          product_id: The ID of the product this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          project_id: The ID of the project this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          system_prompt: System prompt for the conversation. Can be a simple string or a template object
              with components.

          version_id: The ID of the product version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages",
            body=maybe_transform(
                {
                    "external_user_id": external_user_id,
                    "turns": turns,
                    "conversation_id": conversation_id,
                    "external_conversation_id": external_conversation_id,
                    "metadata": metadata,
                    "model": model,
                    "product_id": product_id,
                    "project_id": project_id,
                    "system_prompt": system_prompt,
                    "version_id": version_id,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_user_id: str,
        turns: Iterable[TurnItemParam],
        conversation_id: str | NotGiven = NOT_GIVEN,
        external_conversation_id: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, object] | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        system_prompt: SystemPromptParam | NotGiven = NOT_GIVEN,
        version_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateResponse:
        """
        The `/messages` endpoint allows you to log messages between your users and your
        products.

        Full conversations can be logged all at once in a single request with multiple
        turns, or sequentially over multiple requests with a single turn per request.

        The simplest way to log a message is to pass the `role` and `content` of the
        message to the API along with an `externalConversationId` for the converasation
        and your `productId`.

        However, we recommend that you pass as much information about the conversation
        as possible to allow you to analyze and optimize your prompts, models, and more.

        Args:
          external_user_id: The external user ID that will be mapped to a participant in our system.

          turns: An array of conversation turns, each containing messages exchanged during that
              turn.

          conversation_id: The conversation ID. When provided, this will update an existing conversation
              instead of creating a new one. Either conversationId, externalConversationId,
              productId, or projectId must be provided.

          external_conversation_id: Your own external identifier for the conversation. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          metadata: Additional metadata for the conversation.

          model: The AI model used for the conversation.

          product_id: The ID of the product this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          project_id: The ID of the project this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          system_prompt: System prompt for the conversation. Can be a simple string or a template object
              with components.

          version_id: The ID of the product version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages",
            body=await async_maybe_transform(
                {
                    "external_user_id": external_user_id,
                    "turns": turns,
                    "conversation_id": conversation_id,
                    "external_conversation_id": external_conversation_id,
                    "metadata": metadata,
                    "model": model,
                    "product_id": product_id,
                    "project_id": project_id,
                    "system_prompt": system_prompt,
                    "version_id": version_id,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
