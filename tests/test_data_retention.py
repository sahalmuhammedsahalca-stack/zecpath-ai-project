from datetime import datetime, timedelta, timezone

from security_governance.data_retention import DataRetentionPolicy


def test_retention_period():
    policy = DataRetentionPolicy()

    assert policy.get_retention_days("audit_logs") == 365
    assert policy.get_retention_days("transcripts") == 180
    assert policy.get_retention_days("reports") == 365


def test_expired_data():
    policy = DataRetentionPolicy()

    old_date = datetime.now(timezone.utc) - timedelta(days=400)

    assert policy.is_expired(old_date, "audit_logs") is True


def test_non_expired_data():
    policy = DataRetentionPolicy()

    recent_date = datetime.now(timezone.utc) - timedelta(days=30)

    assert policy.is_expired(recent_date, "audit_logs") is False


def test_unknown_data_type():
    policy = DataRetentionPolicy()

    try:
        policy.get_retention_days("unknown")
        assert False
    except ValueError:
        assert True