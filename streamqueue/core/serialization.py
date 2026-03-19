"""Message serialization helpers."""
import json
from typing import Any

def serialize(message: Any) -> bytes:
    return json.dumps(message).encode("utf-8")

def deserialize(data: bytes) -> Any:
    return json.loads(data.decode("utf-8"))
