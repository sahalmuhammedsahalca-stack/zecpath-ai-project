# Error and Retry Strategy

## Error Categories

### Validation Errors

Examples:

- Missing required field
- Invalid data type
- Invalid request

These should normally not be retried.

### Temporary Errors

Examples:

- Timeout
- Temporary service unavailability
- Connection failure
- Rate limiting

These may be retried.

## Retry Policy

Default maximum retries:

3

## Retry Flow

Request
    |
    v
AI API
    |
    +---- Success → Response
    |
    +---- Temporary Error
              |
              v
         Retry Policy
              |
       +------+------+
       |             |
    Retry         Max Attempts
       |             |
       v             v
    Request        Error Response

## Important Principle

Retries should not be used for permanent validation errors.