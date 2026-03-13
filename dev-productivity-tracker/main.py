from git_analyzer import GitAnalyzer
from report_generator import generate_report

def main():
    print("\nDeveloper Productivity Tracker")
    print("-----------------------------------")

    repo_path = input("Enter path to your git repository: ").strip()

    analyzer = GitAnalyzer(repo_path)

    commits = analyzer.get_commit_count()
    lines_added, lines_removed = analyzer.get_line_stats()
    files_changed = analyzer.get_files_changed()

    report = {
        "commits": commits,
        "lines_added": lines_added,
        "lines_removed": lines_removed,
        "files_changed": files_changed
    }

    generate_report(report)


if __name__ == "__main__":
    main()
