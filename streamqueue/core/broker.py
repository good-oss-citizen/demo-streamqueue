"""Broker connection handling."""

import time
from typing import Any


class BrokerConnection:
    """Manages connection to message broker with reconnection support."""

    def __init__(self, host: str, port: int = 5672, max_retries: int = 3):
        self._host = host
        self._port = port
        self._max_retries = max_retries
        self._connected = False

    def publish(self, message: Any) -> None:
        """Publish a message, retrying on connection failure."""
        for attempt in range(self._max_retries):
            try:
                self._send(message)
                return
            except ConnectionError:
                backoff = min(2**attempt, 30)
                time.sleep(backoff)
                self._reconnect()
        raise ConnectionError(
            f"Failed to publish after {self._max_retries} retries to {self._host}:{self._port}"
        )

    def _send(self, message: Any) -> None:
        if not self._connected:
            raise ConnectionError("Not connected")
        # actual send logic would go here

    def _reconnect(self) -> None:
        self._connected = False
        # actual reconnect logic would go here
        self._connected = True
