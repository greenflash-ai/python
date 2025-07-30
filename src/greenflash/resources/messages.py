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
from ..types.message_item_param import MessageItemParam
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
        messages: Iterable[MessageItemParam],
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
        Record conversations between your users and AI, supporting both simple chat and
        complex agentic workflows.

        **Simple Chat:** Use `role` with values like "user", "assistant", or "system"
        for basic conversations.

        **Agentic Workflows:** Use `messageType` for complex scenarios including tool
        calls, thoughts, observations, and more.

        **Message Ordering:** Messages are stored with sequential timestamps. You can
        provide explicit `createdAt` timestamps for historical data.

        **Message Threading:** Reference parent messages using `parentMessageId`
        (internal ID) or `parentExternalMessageId` (your external ID) to create threaded
        conversations.

        The simplest way to log a message is to provide the `role` and `content` along
        with an `externalConversationId` and your `productId`.

        For agentic workflows, include structured data via `input`/`output` fields, tool
        names for `tool_call` messages, and various message types to represent the full
        execution trace.

        Args:
          external_user_id: Your external user ID that will be mapped to a participant in our system.

          messages: Array of conversation messages.

          conversation_id: The Greenflash conversation ID. When provided, updates an existing conversation
              instead of creating a new one. Either conversationId, externalConversationId,
              productId, or projectId must be provided.

          external_conversation_id: Your external identifier for the conversation. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          metadata: Additional data about the conversation.

          model: The AI model used for the conversation.

          product_id: The Greenflash product this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          project_id: The Greenflash project this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          system_prompt: System prompt for the conversation. Can be a simple string or a template object
              with components.

          version_id: The product version ID.

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
                    "messages": messages,
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
        messages: Iterable[MessageItemParam],
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
        Record conversations between your users and AI, supporting both simple chat and
        complex agentic workflows.

        **Simple Chat:** Use `role` with values like "user", "assistant", or "system"
        for basic conversations.

        **Agentic Workflows:** Use `messageType` for complex scenarios including tool
        calls, thoughts, observations, and more.

        **Message Ordering:** Messages are stored with sequential timestamps. You can
        provide explicit `createdAt` timestamps for historical data.

        **Message Threading:** Reference parent messages using `parentMessageId`
        (internal ID) or `parentExternalMessageId` (your external ID) to create threaded
        conversations.

        The simplest way to log a message is to provide the `role` and `content` along
        with an `externalConversationId` and your `productId`.

        For agentic workflows, include structured data via `input`/`output` fields, tool
        names for `tool_call` messages, and various message types to represent the full
        execution trace.

        Args:
          external_user_id: Your external user ID that will be mapped to a participant in our system.

          messages: Array of conversation messages.

          conversation_id: The Greenflash conversation ID. When provided, updates an existing conversation
              instead of creating a new one. Either conversationId, externalConversationId,
              productId, or projectId must be provided.

          external_conversation_id: Your external identifier for the conversation. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          metadata: Additional data about the conversation.

          model: The AI model used for the conversation.

          product_id: The Greenflash product this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          project_id: The Greenflash project this conversation belongs to. Either conversationId,
              externalConversationId, productId, or projectId must be provided.

          system_prompt: System prompt for the conversation. Can be a simple string or a template object
              with components.

          version_id: The product version ID.

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
                    "messages": messages,
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
