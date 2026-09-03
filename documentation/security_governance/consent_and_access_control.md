# Consent and Access Control

## 1. Consent Management

Candidate processing is linked to an explicit consent record.

## 2. Supported Consent Purposes

- Recruitment evaluation
- Interview analysis
- Report generation
- Audit

## 3. Consent Status

The consent manager tracks:

- Candidate ID
- Approved purposes
- Consent status
- Consent timestamp
- Revocation timestamp when applicable

## 4. Revocation

A candidate's consent can be revoked.

After revocation, the corresponding processing check returns false.

## 5. Role-Based Access

The access-control layer uses predefined roles.

### Admin

Full governance access.

### Recruiter

Access to scores, decisions and reports.

### Analyst

Access to scores, decisions and audit logs.

### Auditor

Access to audit logs and decisions.

## 6. Least Privilege

Users should receive only the permissions necessary for their role.

## 7. Unauthorized Access

Unauthorized permission checks return false and explicit access checks
raise a PermissionError.