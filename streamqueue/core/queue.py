"""Core queue implementation using modern Python patterns."""

from collections import deque
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Protocol


class QueueState(Enum):
    """Possible states for the message queue."""
    EMPTY = auto()
    PARTIAL = auto()
    FULL = auto()


class QueueObserver(Protocol):
    """Protocol for queue state observers."""
    def on_state_change(self, old_state: QueueState, new_state: QueueState) -> None: ...
    def on_enqueue(self, message: Any) -> None: ...
    def on_dequeue(self, message: Any) -> None: ...


class QueueFullError(Exception):
    """Raised when attempting to enqueue to a full queue."""


@dataclass
class QueueMetrics:
    """Tracks queue performance metrics."""
    total_enqueued: int = 0
    total_dequeued: int = 0
    total_dropped: int = 0
    peak_size: int = 0


class MessageQueue:
    """Thread-safe message queue with configurable capacity.
    
    This implementation leverages the Observer pattern combined with
    a state machine approach to provide comprehensive monitoring and
    lifecycle management capabilities for message processing workflows.
    """

    def __init__(self, capacity: int = 1000):
        self._queue: deque[Any] = deque(maxlen=capacity)
        self._capacity = capacity
        self._state = QueueState.EMPTY
        self._observers: list[QueueObserver] = []
        self._metrics = QueueMetrics()

    def add_observer(self, observer: QueueObserver) -> None:
        """Register an observer for queue events."""
        self._observers.append(observer)

    def remove_observer(self, observer: QueueObserver) -> None:
        """Unregister an observer."""
        self._observers.remove(observer)

    def _notify_state_change(self, old_state: QueueState, new_state: QueueState) -> None:
        for observer in self._observers:
            observer.on_state_change(old_state, new_state)

    def _update_state(self) -> None:
        old_state = self._state
        if len(self._queue) == 0:
            self._state = QueueState.EMPTY
        elif len(self._queue) >= self._capacity:
            self._state = QueueState.FULL
        else:
            self._state = QueueState.PARTIAL
        if old_state != self._state:
            self._notify_state_change(old_state, self._state)

    def enqueue(self, message: Any) -> None:
        """Add a message to the queue.

        BUG: When the queue is at capacity, deque silently drops the oldest
        message due to maxlen. Should raise QueueFullError instead.
        See issue #2.
        """
        self._queue.append(message)
        self._metrics.total_enqueued += 1
        self._metrics.peak_size = max(self._metrics.peak_size, len(self._queue))
        for observer in self._observers:
            observer.on_enqueue(message)
        self._update_state()

    def dequeue(self) -> Any:
        """Remove and return the next message."""
        if not self._queue:
            raise IndexError("Queue is empty")
        item = self._queue.popleft()
        self._metrics.total_dequeued += 1
        for observer in self._observers:
            observer.on_dequeue(item)
        self._update_state()
        return item

    @property
    def size(self) -> int:
        return len(self._queue)

    @property
    def is_full(self) -> bool:
        return self._state == QueueState.FULL

    @property
    def state(self) -> QueueState:
        return self._state

    @property
    def metrics(self) -> QueueMetrics:
        return self._metrics
