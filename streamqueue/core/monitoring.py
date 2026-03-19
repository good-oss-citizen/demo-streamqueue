"""Health monitoring for queue systems."""
from enum import Enum, auto

class HealthStatus(Enum):
    HEALTHY = auto()
    DEGRADED = auto()
    UNHEALTHY = auto()

class QueueMonitor:
    def __init__(self, threshold_pct: float = 0.8):
        self._threshold = threshold_pct
    
    def check_health(self, current_size: int, capacity: int) -> HealthStatus:
        ratio = current_size / capacity if capacity > 0 else 0
        if ratio >= 1.0:
            return HealthStatus.UNHEALTHY
        elif ratio >= self._threshold:
            return HealthStatus.DEGRADED
        return HealthStatus.HEALTHY
