"""
Day 64 - Internal Review Report Generator
"""


class ReviewReportGenerator:
    """Generate a structured internal review report."""

    REVIEW_CATEGORIES = [
        "accuracy",
        "ux",
        "performance",
    ]

    PRIORITY_LEVELS = [
        "High",
        "Medium",
        "Low",
    ]

    def create_finding(self, category, issue, priority, recommendation):
        """Create a structured review finding."""

        if category not in self.REVIEW_CATEGORIES:
            raise ValueError(f"Unknown review category: {category}")

        if priority not in self.PRIORITY_LEVELS:
            raise ValueError(f"Unknown priority: {priority}")

        return {
            "category": category,
            "issue": issue,
            "priority": priority,
            "recommendation": recommendation,
        }

    def summarize(self, findings):
        """Summarize review findings by category and priority."""

        summary = {
            "total_findings": len(findings),
            "accuracy": 0,
            "ux": 0,
            "performance": 0,
            "high_priority": 0,
            "medium_priority": 0,
            "low_priority": 0,
        }

        for finding in findings:
            category = finding["category"]
            priority = finding["priority"]

            summary[category] += 1

            if priority == "High":
                summary["high_priority"] += 1
            elif priority == "Medium":
                summary["medium_priority"] += 1
            elif priority == "Low":
                summary["low_priority"] += 1

        return summary


if __name__ == "__main__":
    generator = ReviewReportGenerator()

    findings = [
        generator.create_finding(
            "accuracy",
            "Review scoring consistency across hiring stages.",
            "Medium",
            "Run additional candidate validation scenarios.",
        ),
        generator.create_finding(
            "ux",
            "Review clarity of candidate evaluation outputs.",
            "Medium",
            "Improve result presentation and explanations.",
        ),
        generator.create_finding(
            "performance",
            "Review response time under larger workloads.",
            "Low",
            "Continue performance benchmarking.",
        ),
    ]

    print(generator.summarize(findings))