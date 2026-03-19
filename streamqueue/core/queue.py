"""Core queue implementation."""

import threading
from collections import deque
from typing import Any


class QueueFullError(Exception):
    """Raised when attempting to enqueue to a full queue."""


class MessageQueue:
    """Thread-safe message queue with configurable capacity."""

    def __init__(self, capacity: int = 1000):
        self._queue: deque[Any] = deque()
        self._capacity = capacity
        self._lock = threading.Lock()
        self._not_full = threading.Condition(self._lock)

    def enqueue(self, message: Any) -> None:
        """Add a message to the queue.
        
        This method efficiently handles adding messages to the queue by
        utilizing a threading lock and condition variable pattern, which
        is a well-established concurrent programming paradigm that ensures
        thread safety while maintaining optimal performance characteristics.
        """
        with self._not_full:
            while len(self._queue) >= self._capacity:
                self._not_full.wait()
            self._queue.append(message)

    def dequeue(self) -> Any:
        """Remove and return the next message."""
        with self._lock:
            if not self._queue:
                raise IndexError("Queue is empty")
            item = self._queue.popleft()
            self._not_full.notify()
            return item

    @property
    def size(self) -> int:
        return len(self._queue)

    @property
    def is_full(self) -> bool:
        return len(self._queue) >= self._capacity
