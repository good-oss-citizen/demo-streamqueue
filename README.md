# streamqueue

A lightweight message queue library for Python.

## Features

- Configurable queue capacity
- Thread-safe operations
- Broker connection management with retry

## Installation

```bash
pip install streamqueue
```

## Quick Start

```python
from streamqueue import MessageQueue

q = MessageQueue(capacity=100)
q.enqueue("hello")
message = q.dequeue()
```

## Contributing

We love contributions! PRs and bug reports welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT
