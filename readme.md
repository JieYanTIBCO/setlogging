# Setlogging

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/setlogging.svg)](https://badge.fury.io/py/setlogging)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A flexible Python logging utility with JSON support and timezone awareness.

## Author
- **Name:** Jie Yan
- **Contact:** kiki3890528@gmail.com

## Features

- JSON and plain text log formats
- Log file rotation with size limits
- Console output options
- Timezone-aware logging
- Customizable formatting
- Type-safe configuration

## Installation

```bash
pip install setlogging
```

## Usage

```python
from setlogging import get_logger

# Basic logging
logger = get_logger()
logger.info("Basic log message")

# JSON logging with indentation
logger = get_logger(json_format=True, indent=2)
logger.info("Structured logging")

# Custom file and rotation
logger = get_logger(
    log_file="/tmp/app.log",
    max_bytes=10*1024*1024,  # 10MB
```

## Project Structure

```
setlogging/
├── src/
│   └── setlogging/
│       ├── __init__.py
│       └── logger.py
├── tests/
│   ├── __init__.py
│   └── test_logger.py
├── pyproject.toml
├── README.md
└── LICENSE
```

## Configuration Options

| Option         | Type   | Default    | Description                          |
|----------------|--------|------------|--------------------------------------|
| log_level      | int    | DEBUG      | Logging level                        |
| log_file       | str    | None       | Log file path                        |
| max_bytes      | int    | 25MB       | Max file size before rotation        |
| backup_count   | int    | 7          | Number of backup files               |
| console_output | bool   | True       | Enable console logging               |
| log_format     | str    | None       | Custom log format string             |
| date_format    | str    | None       | Custom date format string            |
| json_format    | bool   | False      | Enable JSON formatting               |
| indent         | int    | None       | JSON indentation level               |



