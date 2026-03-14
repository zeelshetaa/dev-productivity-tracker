from git_analyzer import GitAnalyzer
from activity_estimator import estimate_coding_hours
from report_generator import print_console_report
from dashboard_generator import generate_commit_graph, generate_html_dashboard


def main():

    print("\nDeveloper Productivity Tracker V2")
    print("------------------------------------")

    repo = input("Enter Git Repository Path: ").strip()

    analyzer = GitAnalyzer(repo)

    commits = analyzer.get_commit_count()
    added, removed = analyzer.get_line_stats()
    activity = analyzer.get_commit_activity()

    hours, level = estimate_coding_hours(commits)

    data = {
        "commits": commits,
        "lines_added": added,
        "lines_removed": removed,
        "hours": hours,
        "activity_level": level
    }

    print_console_report(data)

    generate_commit_graph(activity)
    generate_html_dashboard(data)

    print("Dashboard generated → dashboard.html")


if __name__ == "__main__":
    main()
