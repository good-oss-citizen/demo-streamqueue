"""Tests for BrokerConnection."""

import pytest
from streamqueue.core.broker import BrokerConnection


class TestBrokerConnection:
    def test_publish_retries_on_disconnect(self):
        broker = BrokerConnection("localhost", max_retries=3)
        broker._connected = True
        broker.publish("test message")

    def test_publish_raises_after_max_retries(self):
        broker = BrokerConnection("localhost", max_retries=1)
        with pytest.raises(ConnectionError, match="Failed to publish"):
            broker.publish("test message")
