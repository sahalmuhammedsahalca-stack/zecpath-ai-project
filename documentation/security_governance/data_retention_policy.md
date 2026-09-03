# Data Retention Policy

## 1. Purpose

The retention policy defines how long different categories of Zecpath AI
data should remain available.

## 2. Default Retention Periods

| Data | Retention |
|---|---:|
| Audit logs | 365 days |
| Transcripts | 180 days |
| Reports | 365 days |

## 3. Expiry

A data item is considered expired when its retention period has elapsed
from its creation timestamp.

## 4. Policy Enforcement

The retention module provides:

- Retention-period lookup
- Expiry calculation
- Expiry detection
- File expiration checks

## 5. Configuration

Retention periods are configurable so that future deployment requirements
can be applied without changing the core retention logic.

## 6. Governance Principle

Data should not be retained indefinitely without a defined operational
purpose or applicable retention requirement.