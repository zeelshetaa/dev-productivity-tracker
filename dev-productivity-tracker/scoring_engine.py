class ScoringEngine:

    def __init__(self, data):
        self.data = data

    def calculate_score(self):
        commits = self.data["commits"]
        added = self.data["lines_added"]
        removed = self.data["lines_removed"]

        score = 0

        score += commits * 2
        score += (added - removed) * 0.5

        if score > 1000:
            level = "High"
        elif score > 300:
            level = "Moderate"
        else:
            level = "Low"

        return score, level