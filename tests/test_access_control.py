from security_governance.access_control import AccessControl


def test_admin_permissions():
    access = AccessControl()

    assert access.has_permission(
        "admin",
        "view_audit_logs",
    )

    assert access.has_permission(
        "admin",
        "manage_consent",
    )


def test_recruiter_permissions():
    access = AccessControl()

    assert access.has_permission(
        "recruiter",
        "view_reports",
    )

    assert not access.has_permission(
        "recruiter",
        "view_transcripts",
    )


def test_auditor_permissions():
    access = AccessControl()

    assert access.has_permission(
        "auditor",
        "view_audit_logs",
    )

    assert not access.has_permission(
        "auditor",
        "manage_consent",
    )


def test_denied_access():
    access = AccessControl()

    try:
        access.check_access(
            "recruiter",
            "view_transcripts",
        )
        assert False
    except PermissionError:
        assert True


def test_unknown_role():
    access = AccessControl()

    assert access.has_permission(
        "unknown",
        "view_reports",
    ) is False