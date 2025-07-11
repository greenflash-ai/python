# Messages

Types:

```python
from greenflash.types import SystemPrompt, MessageCreateResponse
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/greenflash/resources/messages.py">create</a>(\*\*<a href="src/greenflash/types/message_create_params.py">params</a>) -> <a href="./src/greenflash/types/message_create_response.py">MessageCreateResponse</a></code>

# Identify

Types:

```python
from greenflash.types import IdentifyCreateOrUpdateResponse
```

Methods:

- <code title="post /identify">client.identify.<a href="./src/greenflash/resources/identify.py">create_or_update</a>(\*\*<a href="src/greenflash/types/identify_create_or_update_params.py">params</a>) -> <a href="./src/greenflash/types/identify_create_or_update_response.py">IdentifyCreateOrUpdateResponse</a></code>

# Ratings

Types:

```python
from greenflash.types import GenericSuccess
```

Methods:

- <code title="post /ratings">client.ratings.<a href="./src/greenflash/resources/ratings.py">log</a>(\*\*<a href="src/greenflash/types/rating_log_params.py">params</a>) -> <a href="./src/greenflash/types/generic_success.py">GenericSuccess</a></code>

# Conversions

Types:

```python
from greenflash.types import ConversionLogResponse
```

Methods:

- <code title="post /conversions">client.conversions.<a href="./src/greenflash/resources/conversions.py">log</a>(\*\*<a href="src/greenflash/types/conversion_log_params.py">params</a>) -> <a href="./src/greenflash/types/conversion_log_response.py">ConversionLogResponse</a></code>
