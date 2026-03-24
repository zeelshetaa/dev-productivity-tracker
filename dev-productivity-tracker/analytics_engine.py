class AnalyticsEngine:

    def __init__(self, data):
        self.data = data

    def analyze_patterns(self):
        insights = {}

        commits = self.data["commits"]
        added = self.data["lines_added"]
        removed = self.data["lines_removed"]

        if commits > 50:
            insights["commit_pattern"] = "High activity"
        else:
            insights["commit_pattern"] = "Low activity"

        if added > removed:
            insights["code_trend"] = "Growing codebase"
        else:
            insights["code_trend"] = "Refactoring / cleanup"

        return insights