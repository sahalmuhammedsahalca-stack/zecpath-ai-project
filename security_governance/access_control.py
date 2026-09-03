class AccessControl:
    """
    Role-based access control for Zecpath AI governance data.
    """

    ROLE_PERMISSIONS = {
        "admin": {
            "view_scores",
            "view_decisions",
            "view_transcripts",
            "view_reports",
            "manage_consent",
            "view_audit_logs",
        },
        "recruiter": {
            "view_scores",
            "view_decisions",
            "view_reports",
        },
        "analyst": {
            "view_scores",
            "view_decisions",
            "view_audit_logs",
        },
        "auditor": {
            "view_audit_logs",
            "view_decisions",
        },
    }

    def has_permission(
        self,
        role: str,
        permission: str,
    ) -> bool:
        permissions = self.ROLE_PERMISSIONS.get(role, set())

        return permission in permissions

    def check_access(
        self,
        role: str,
        permission: str,
    ) -> None:
        if not self.has_permission(role, permission):
            raise PermissionError(
                f"Role '{role}' does not have permission "
                f"'{permission}'"
            )

    def get_permissions(self, role: str) -> set:
        return self.ROLE_PERMISSIONS.get(role, set()).copy()