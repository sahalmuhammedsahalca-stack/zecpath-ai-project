from .logging_system import ObservabilityLogger
from .metrics_tracker import MetricsTracker
from .alert_manager import AlertManager
from .dashboard_monitor import DashboardMonitor
from .decision_audit import DecisionAuditLogger


class ObservabilityController:
    def __init__(self):
        self.logger = ObservabilityLogger()
        self.metrics = MetricsTracker()
        self.alerts = AlertManager()
        self.dashboard = DashboardMonitor()
        self.audit = DecisionAuditLogger()

    def record_api_request(
        self,
        endpoint,
        method,
        status,
        response_time,
    ):
        self.logger.log_api(
            endpoint,
            method,
            status,
            response_time,
        )

        if status == "error":
            self.metrics.record_failure()
        else:
            self.metrics.record_response_time(response_time)

    def record_model_result(self, model, output, score=None):
        return self.logger.log_model_output(
            model,
            output,
            score,
        )

    def record_error(self, error_type, message):
        return self.logger.log_error(
            error_type,
            message,
        )

    def record_accuracy(self, correct):
        self.metrics.record_accuracy(correct)

    def record_decision(
        self,
        candidate_id,
        score,
        recommendation,
        reason,
    ):
        return self.audit.record_decision(
            candidate_id,
            score,
            recommendation,
            reason,
        )

    def get_monitoring_report(
        self,
        candidate_stats,
        interview_stats,
    ):
        metrics = self.metrics.summary()
        alert_report = self.alerts.evaluate(metrics)

        dashboard = self.dashboard.build_dashboard(
            metrics,
            alert_report,
            candidate_stats,
            interview_stats,
        )

        return {
            "metrics": metrics,
            "alerts": alert_report,
            "dashboard": dashboard,
            "audit_log_count": self.audit.count(),
            "log_count": self.logger.count(),
        }