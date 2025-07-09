# Messages

Types:

```python
from greenflash_public_api.types import GenericSuccess
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/greenflash_public_api/resources/messages.py">create</a>(\*\*<a href="src/greenflash_public_api/types/message_create_params.py">params</a>) -> <a href="./src/greenflash_public_api/types/generic_success.py">GenericSuccess</a></code>

# Identify

Types:

```python
from greenflash_public_api.types import IdentifyCreateOrUpdateResponse
```

Methods:

- <code title="post /identify">client.identify.<a href="./src/greenflash_public_api/resources/identify.py">create_or_update</a>(\*\*<a href="src/greenflash_public_api/types/identify_create_or_update_params.py">params</a>) -> <a href="./src/greenflash_public_api/types/identify_create_or_update_response.py">IdentifyCreateOrUpdateResponse</a></code>

# Ratings

Methods:

- <code title="post /ratings">client.ratings.<a href="./src/greenflash_public_api/resources/ratings.py">log</a>(\*\*<a href="src/greenflash_public_api/types/rating_log_params.py">params</a>) -> <a href="./src/greenflash_public_api/types/generic_success.py">GenericSuccess</a></code>

# Conversions

Types:

```python
from greenflash_public_api.types import ConversionLogResponse
```

Methods:

- <code title="post /conversions">client.conversions.<a href="./src/greenflash_public_api/resources/conversions.py">log</a>(\*\*<a href="src/greenflash_public_api/types/conversion_log_params.py">params</a>) -> <a href="./src/greenflash_public_api/types/conversion_log_response.py">ConversionLogResponse</a></code>
