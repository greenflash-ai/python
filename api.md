# Messages

Types:

```python
from greenflash.types import CreateParams, CreateResponse, MessageItem, SystemPrompt, TurnItem
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/greenflash/resources/messages.py">create</a>(\*\*<a href="src/greenflash/types/message_create_params.py">params</a>) -> <a href="./src/greenflash/types/create_response.py">CreateResponse</a></code>

# Identify

Types:

```python
from greenflash.types import CreateOrUpdateParams, CreateOrUpdateResponse, Participant
```

Methods:

- <code title="post /identify">client.identify.<a href="./src/greenflash/resources/identify.py">create_or_update</a>(\*\*<a href="src/greenflash/types/identify_create_or_update_params.py">params</a>) -> <a href="./src/greenflash/types/create_or_update_response.py">CreateOrUpdateResponse</a></code>

# Ratings

Types:

```python
from greenflash.types import LogRatingParams, LogRatingResponse
```

Methods:

- <code title="post /ratings">client.ratings.<a href="./src/greenflash/resources/ratings.py">log</a>(\*\*<a href="src/greenflash/types/rating_log_params.py">params</a>) -> <a href="./src/greenflash/types/log_rating_response.py">LogRatingResponse</a></code>

# Conversions

Types:

```python
from greenflash.types import LogConversionParams, LogConversionResponse
```

Methods:

- <code title="post /conversions">client.conversions.<a href="./src/greenflash/resources/conversions.py">log</a>(\*\*<a href="src/greenflash/types/conversion_log_params.py">params</a>) -> <a href="./src/greenflash/types/log_conversion_response.py">LogConversionResponse</a></code>
