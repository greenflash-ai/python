# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import chat_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    """Stream chat and agentic conversations"""

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        question: str,
        context: str | Omit = omit,
        conversation_id: str | Omit = omit,
        messages: Iterable[chat_create_params.Message] | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Start a streaming chat session with the Greenflash AI agent.

        **Requires a Growth or Enterprise plan.**

        The response is a Server-Sent Events (SSE) stream
        (`Content-Type: text/event-stream`). Each event follows the format:

        ```
        event: <type>
        data: <json>
        ```

        **Event types:**

        - `tool_call` — The agent is invoking a tool. Data:
          `{"step": 1, "toolName": "...", "displayName": "..."}`
        - `tool_result` — A tool returned its result. Data:
          `{"step": 1, "toolName": "...", "displayName": "..."}`
        - `text_delta` — A chunk of the agent's text response. Concatenate all deltas to
          build the full message. Data: `{"text": "..."}`
        - `done` — The stream completed successfully. Data:
          `{"conversationId": "...", "status": "complete", "usage": {"toolCalls": N, "tools": ["..."]}}`
        - `error` — An error occurred during processing. Data:
          `{"error": "...", "code": "..."}`

        **Multi-turn conversations:** Pass previous messages in the `messages` array and
        reuse the `conversationId` returned in the `done` event.

        **Rate limits:** This endpoint is rate-limited per tenant (requests/hour) and
        subject to token usage limits.

        Args:
          question: The current user question to send to the AI agent.

          context: Free-form hint injected into the system prompt for this turn only.

          conversation_id: Stable identifier for multi-turn conversations. If omitted, a new ID is
              generated.

          messages: Prior conversation history (NOT including the current question). Used for
              multi-turn context.

          product_id: Scope the chat to a specific product. If omitted, the agent can access all
              products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/chat",
            body=maybe_transform(
                {
                    "question": question,
                    "context": context,
                    "conversation_id": conversation_id,
                    "messages": messages,
                    "product_id": product_id,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChatResource(AsyncAPIResource):
    """Stream chat and agentic conversations"""

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/greenflash-ai/python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/greenflash-ai/python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        question: str,
        context: str | Omit = omit,
        conversation_id: str | Omit = omit,
        messages: Iterable[chat_create_params.Message] | Omit = omit,
        product_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Start a streaming chat session with the Greenflash AI agent.

        **Requires a Growth or Enterprise plan.**

        The response is a Server-Sent Events (SSE) stream
        (`Content-Type: text/event-stream`). Each event follows the format:

        ```
        event: <type>
        data: <json>
        ```

        **Event types:**

        - `tool_call` — The agent is invoking a tool. Data:
          `{"step": 1, "toolName": "...", "displayName": "..."}`
        - `tool_result` — A tool returned its result. Data:
          `{"step": 1, "toolName": "...", "displayName": "..."}`
        - `text_delta` — A chunk of the agent's text response. Concatenate all deltas to
          build the full message. Data: `{"text": "..."}`
        - `done` — The stream completed successfully. Data:
          `{"conversationId": "...", "status": "complete", "usage": {"toolCalls": N, "tools": ["..."]}}`
        - `error` — An error occurred during processing. Data:
          `{"error": "...", "code": "..."}`

        **Multi-turn conversations:** Pass previous messages in the `messages` array and
        reuse the `conversationId` returned in the `done` event.

        **Rate limits:** This endpoint is rate-limited per tenant (requests/hour) and
        subject to token usage limits.

        Args:
          question: The current user question to send to the AI agent.

          context: Free-form hint injected into the system prompt for this turn only.

          conversation_id: Stable identifier for multi-turn conversations. If omitted, a new ID is
              generated.

          messages: Prior conversation history (NOT including the current question). Used for
              multi-turn context.

          product_id: Scope the chat to a specific product. If omitted, the agent can access all
              products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/chat",
            body=await async_maybe_transform(
                {
                    "question": question,
                    "context": context,
                    "conversation_id": conversation_id,
                    "messages": messages,
                    "product_id": product_id,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_raw_response_wrapper(
            chat.create,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_raw_response_wrapper(
            chat.create,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_streamed_response_wrapper(
            chat.create,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_streamed_response_wrapper(
            chat.create,
        )
