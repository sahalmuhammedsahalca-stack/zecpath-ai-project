from monitoring_observability.dashboard_monitor import DashboardMonitor


def test_dashboard_monitor():
    dashboard = DashboardMonitor()

    candidates = dashboard.candidate_processing_stats(
        100,
        90,
        10,
    )

    interviews = dashboard.interview_success_stats(
        50,
        40,
    )

    assert candidates["total_candidates"] == 100
    assert candidates["successful"] == 90
    assert interviews["success_rate_percent"] == 80.0