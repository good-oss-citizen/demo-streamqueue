"""Tests for MessageQueue."""

import pytest
from streamqueue.core.queue import MessageQueue


class TestMessageQueue:
    def test_enqueue_dequeue(self):
        q = MessageQueue(capacity=10)
        q.enqueue("hello")
        assert q.dequeue() == "hello"

    def test_dequeue_empty_raises(self):
        q = MessageQueue(capacity=10)
        with pytest.raises(IndexError, match="Queue is empty"):
            q.dequeue()

    def test_size(self):
        q = MessageQueue(capacity=10)
        q.enqueue("a")
        q.enqueue("b")
        assert q.size == 2

    def test_is_full(self):
        q = MessageQueue(capacity=2)
        q.enqueue("a")
        q.enqueue("b")
        assert q.is_full
