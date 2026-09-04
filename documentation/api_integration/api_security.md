# API Authentication and Security

## Authentication

The proposed integration supports:

- API keys
- Bearer tokens
- Service tokens

## Security Controls

### Authentication Required

All protected AI API calls should require authentication.

### Encryption

Communication should use encrypted transport.

### Secret Storage

API keys and tokens should not be hard-coded.

Secrets should be stored using environment variables or a secure secret
management system.

### Token Rotation

Credentials should be rotated regularly.

### Least Privilege

Each service should receive only the permissions required for its task.

### Sensitive Logging

Passwords, API keys, tokens and sensitive candidate information should not
be written into application logs.

## Governance

API integration must remain consistent with the project's existing security,
audit and governance architecture.