"""Core queue implementation."""

from collections import deque
from typing import Any
import logging

logger = logging.getLogger(__name__)


class QueueFullError(Exception):
    """Raised when attempting to enqueue to a full queue."""


class MessageQueue:
    """Thread-safe message queue with configurable capacity."""

    def __init__(self, capacity: int = 1000):
        self._queue: deque[Any] = deque(maxlen=capacity)
        self._capacity = capacity

    def enqueue(self, message: Any) -> None:
        """Add a message to the queue."""
        if self.is_full:
            logger.warning("Queue full, dropping oldest message to make room")
            self._queue.popleft()
        self._queue.append(message)

    def dequeue(self) -> Any:
        """Remove and return the next message."""
        if not self._queue:
            raise IndexError("Queue is empty")
        return self._queue.popleft()

    @property
    def size(self) -> int:
        return len(self._queue)

    @property
    def is_full(self) -> bool:
        return len(self._queue) >= self._capacity
