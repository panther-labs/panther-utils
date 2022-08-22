## panther-utils
Panther Config SDK utilities repo


### Match Filters

`deep_equal` allows you to filter events based on a field match:

```python
from panther_config import detection
from panther_utils import match_filters

# example: match server logs with insecure POST requests
detection.Rule(
    rule_id="My.Custom.Rule",
    log_types=["ServerLogs.HTTP"],
    filters=[
        match_filters.deep_equal(path="request.method", value="POST"),
        match_filters.deep_equal(path="request.use_ssl", value=False),
    ]
)
```

```python
from panther_config import detection
from panther_utils import detections as utl_detections

# example: match server logs with insecure POST requests
utl_detections.aws_admin_role_assumed("Megacorp.GodKing", "Catman", "TheGothInTheServerRoom")

```
