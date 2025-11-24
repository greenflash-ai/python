# Messages

Types:

```python
from greenflash.types import CreateMessageParams, CreateMessageResponse, MessageItem, SystemPrompt
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/greenflash/resources/messages.py">create</a>(\*\*<a href="src/greenflash/types/message_create_params.py">params</a>) -> <a href="./src/greenflash/types/create_message_response.py">CreateMessageResponse</a></code>

# Interactions

Types:

```python
from greenflash.types import (
    GetInteractionAnalyticsParams,
    GetInteractionAnalyticsResponse,
    ListInteractionsParams,
    ListInteractionsResponse,
)
```

Methods:

- <code title="get /interactions">client.interactions.<a href="./src/greenflash/resources/interactions.py">list</a>(\*\*<a href="src/greenflash/types/interaction_list_params.py">params</a>) -> <a href="./src/greenflash/types/list_interactions_response.py">ListInteractionsResponse</a></code>
- <code title="get /interactions/{interactionId}/analytics">client.interactions.<a href="./src/greenflash/resources/interactions.py">get_interaction_analytics</a>(interaction_id, \*\*<a href="src/greenflash/types/interaction_get_interaction_analytics_params.py">params</a>) -> <a href="./src/greenflash/types/get_interaction_analytics_response.py">GetInteractionAnalyticsResponse</a></code>

# Users

Types:

```python
from greenflash.types import (
    CreateUserParams,
    CreateUserResponse,
    GetUserAnalyticsParams,
    GetUserAnalyticsResponse,
    ListUsersParams,
    ListUsersResponse,
    Participant,
    UpdateUserParams,
    UpdateUserResponse,
)
```

Methods:

- <code title="post /users">client.users.<a href="./src/greenflash/resources/users.py">create</a>(\*\*<a href="src/greenflash/types/user_create_params.py">params</a>) -> <a href="./src/greenflash/types/create_user_response.py">CreateUserResponse</a></code>
- <code title="put /users/{userId}">client.users.<a href="./src/greenflash/resources/users.py">update</a>(user_id, \*\*<a href="src/greenflash/types/user_update_params.py">params</a>) -> <a href="./src/greenflash/types/update_user_response.py">UpdateUserResponse</a></code>
- <code title="get /users">client.users.<a href="./src/greenflash/resources/users.py">list</a>(\*\*<a href="src/greenflash/types/user_list_params.py">params</a>) -> <a href="./src/greenflash/types/list_users_response.py">ListUsersResponse</a></code>
- <code title="get /users/{userId}/analytics">client.users.<a href="./src/greenflash/resources/users.py">get_user_analytics</a>(user_id, \*\*<a href="src/greenflash/types/user_get_user_analytics_params.py">params</a>) -> <a href="./src/greenflash/types/get_user_analytics_response.py">GetUserAnalyticsResponse</a></code>

# Ratings

Types:

```python
from greenflash.types import LogRatingParams, LogRatingResponse
```

Methods:

- <code title="post /ratings">client.ratings.<a href="./src/greenflash/resources/ratings.py">log</a>(\*\*<a href="src/greenflash/types/rating_log_params.py">params</a>) -> <a href="./src/greenflash/types/log_rating_response.py">LogRatingResponse</a></code>

# Organizations

Types:

```python
from greenflash.types import (
    CreateOrganizationParams,
    CreateOrganizationResponse,
    GetOrganizationAnalyticsParams,
    GetOrganizationAnalyticsResponse,
    ListOrganizationsParams,
    ListOrganizationsResponse,
    TenantOrganization,
    UpdateOrganizationParams,
    UpdateOrganizationResponse,
)
```

Methods:

- <code title="post /organizations">client.organizations.<a href="./src/greenflash/resources/organizations.py">create</a>(\*\*<a href="src/greenflash/types/organization_create_params.py">params</a>) -> <a href="./src/greenflash/types/create_organization_response.py">CreateOrganizationResponse</a></code>
- <code title="put /organizations/{organizationId}">client.organizations.<a href="./src/greenflash/resources/organizations.py">update</a>(organization_id, \*\*<a href="src/greenflash/types/organization_update_params.py">params</a>) -> <a href="./src/greenflash/types/update_organization_response.py">UpdateOrganizationResponse</a></code>
- <code title="get /organizations">client.organizations.<a href="./src/greenflash/resources/organizations.py">list</a>(\*\*<a href="src/greenflash/types/organization_list_params.py">params</a>) -> <a href="./src/greenflash/types/list_organizations_response.py">ListOrganizationsResponse</a></code>
- <code title="get /organizations/{organizationId}/analytics">client.organizations.<a href="./src/greenflash/resources/organizations.py">get_organization_analytics</a>(organization_id, \*\*<a href="src/greenflash/types/organization_get_organization_analytics_params.py">params</a>) -> <a href="./src/greenflash/types/get_organization_analytics_response.py">GetOrganizationAnalyticsResponse</a></code>

# Prompts

Types:

```python
from greenflash.types import (
    ComponentInput,
    ComponentUpdate,
    CreatePromptParams,
    CreatePromptResponse,
    DeletePromptResponse,
    GetPromptParams,
    GetPromptResponse,
    ListPromptsParams,
    ListPromptsResponse,
    Prompt,
    PromptComponent,
    SlimPrompt,
    SlimPromptComponent,
    UpdatePromptParams,
    UpdatePromptResponse,
)
```

Methods:

- <code title="post /prompts">client.prompts.<a href="./src/greenflash/resources/prompts.py">create</a>(\*\*<a href="src/greenflash/types/prompt_create_params.py">params</a>) -> <a href="./src/greenflash/types/create_prompt_response.py">CreatePromptResponse</a></code>
- <code title="put /prompts/{id}">client.prompts.<a href="./src/greenflash/resources/prompts.py">update</a>(id, \*\*<a href="src/greenflash/types/prompt_update_params.py">params</a>) -> <a href="./src/greenflash/types/update_prompt_response.py">UpdatePromptResponse</a></code>
- <code title="get /prompts">client.prompts.<a href="./src/greenflash/resources/prompts.py">list</a>(\*\*<a href="src/greenflash/types/prompt_list_params.py">params</a>) -> <a href="./src/greenflash/types/list_prompts_response.py">ListPromptsResponse</a></code>
- <code title="delete /prompts/{id}">client.prompts.<a href="./src/greenflash/resources/prompts.py">delete</a>(id) -> <a href="./src/greenflash/types/delete_prompt_response.py">DeletePromptResponse</a></code>
- <code title="get /prompts/{id}">client.prompts.<a href="./src/greenflash/resources/prompts.py">get</a>(id) -> <a href="./src/greenflash/types/get_prompt_response.py">GetPromptResponse</a></code>

# Events

Types:

```python
from greenflash.types import CreateEventParams, CreateEventResponse
```

Methods:

- <code title="post /events">client.events.<a href="./src/greenflash/resources/events.py">create</a>(\*\*<a href="src/greenflash/types/event_create_params.py">params</a>) -> <a href="./src/greenflash/types/create_event_response.py">CreateEventResponse</a></code>
