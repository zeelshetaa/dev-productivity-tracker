from git_analyzer import GitAnalyzer
from report_generator import generate_report
from analytics_engine import AnalyticsEngine
from scoring_engine import ScoringEngine
from ai_recommender import AIRecommender


def main():

    repo_path = input("Enter Git Repository Path: ")

    analyzer = GitAnalyzer(repo_path)

    commits = analyzer.get_commit_count()
    added, removed = analyzer.get_line_stats()
    files_changed = analyzer.get_files_changed()

    data = {
        "commits": commits,
        "lines_added": added,
        "lines_removed": removed,
        "files_changed": files_changed   # ✅ FIXED
    }

    analytics = AnalyticsEngine(data)
    insights = analytics.analyze_patterns()

    scoring = ScoringEngine(data)
    score, level = scoring.calculate_score()

    ai = AIRecommender(data)
    recommendations = ai.generate_recommendations()

    generate_report(data, score, level, insights, recommendations)


if __name__ == "__main__":
    main()
