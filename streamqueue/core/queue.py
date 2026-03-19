"""Core queue implementation."""

from collections import deque
from typing import Any


class QueueFullError(Exception):
    """Raised when attempting to enqueue to a full queue."""


class MessageQueue:
    """Thread-safe message queue with configurable capacity."""

    def __init__(self, capacity: int = 1000):
        self._queue: deque[Any] = deque(maxlen=capacity)
        self._capacity = capacity

    def enqueue(self, message: Any) -> None:
        """Add a message to the queue.

        BUG: When the queue is at capacity, deque silently drops the oldest
        message due to maxlen. Should raise QueueFullError instead.
        See issue #3.
        """
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

    def peek(self) -> Any:
        """Look at the next message without removing it."""
        if not self._queue:
            raise IndexError("Queue is empty")
        return self._queue[0]

    def clear(self) -> None:
        """Remove all messages from the queue."""
        self._queue.clear()
