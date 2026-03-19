"""streamqueue — a lightweight message queue library for Python."""

from streamqueue.core.queue import MessageQueue, QueueFullError

__all__ = ["MessageQueue", "QueueFullError"]
__version__ = "1.8.0"
