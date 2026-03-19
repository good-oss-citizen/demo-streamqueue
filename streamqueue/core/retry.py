"""Retry logic for queue operations."""
import time
from typing import Callable, Any

def with_retry(fn: Callable, max_attempts: int = 3, backoff: float = 1.0) -> Any:
    for attempt in range(max_attempts):
        try:
            return fn()
        except Exception:
            if attempt == max_attempts - 1:
                raise
            time.sleep(backoff * (2 ** attempt))
