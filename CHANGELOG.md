# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.8.0] - 2024-11-15

### Added
- Broker connection management with retry and exponential backoff

### Fixed
- Broker reconnection during publish now retries instead of dropping messages

## [1.7.0] - 2024-09-20

### Added
- `is_full` property on MessageQueue
- Configurable capacity parameter

### Fixed
- Thread safety issue in dequeue under high concurrency
