"""Queue metrics collection."""
from dataclasses import dataclass, field
from typing import Any
import time

@dataclass
class QueueMetrics:
    total_enqueued: int = 0
    total_dequeued: int = 0
    total_dropped: int = 0
    peak_size: int = 0
    avg_wait_time: float = 0.0
    _timestamps: list = field(default_factory=list)
    
    def record_enqueue(self) -> None:
        self.total_enqueued += 1
        self._timestamps.append(time.time())
    
    def record_dequeue(self) -> None:
        self.total_dequeued += 1
    
    def record_drop(self) -> None:
        self.total_dropped += 1
    
    def snapshot(self) -> dict:
        return {
            "total_enqueued": self.total_enqueued,
            "total_dequeued": self.total_dequeued,
            "total_dropped": self.total_dropped,
            "peak_size": self.peak_size,
        }
