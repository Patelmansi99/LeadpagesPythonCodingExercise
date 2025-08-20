# Design Notes

## Overview

This project is modularized for clarity and maintainability:
- `animal_api.py` abstracts all HTTP and API logic, including retries and pagination.
- `animal_transformer.py` handles all transformation logic for animal data.
- `etl.py` orchestrates the ETL process, batching, and logging.

## Error Handling
- All HTTP requests are retried on 5xx errors and random server delays.
- Batching is used to avoid overloading the server.

## Extensibility
- Each module can be extended or replaced independently.
- Tests use mocks and dummy classes for isolation.

## Testing
- Each module has its own test file for focused unit testing.
- Run all tests with `python -m unittest discover`.
