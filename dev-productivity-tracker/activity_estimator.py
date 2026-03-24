class AIRecommender:

    def __init__(self, data):
        self.data = data

    def generate_recommendations(self):
        recommendations = []

        if self.data["commits"] < 5:
            recommendations.append("Increase commit frequency")

        if self.data["lines_removed"] > self.data["lines_added"]:
            recommendations.append("Too much deletion, check stability")

        if self.data["files_changed"] > 50:
            recommendations.append("High file changes, risk of instability")

        return recommendations
