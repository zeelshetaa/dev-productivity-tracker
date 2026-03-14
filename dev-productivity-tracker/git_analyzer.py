from utils import run_git_command
from collections import defaultdict

class GitAnalyzer:

    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_commit_count(self):
        command = ["git", "rev-list", "--count", "HEAD"]
        output = run_git_command(command, self.repo_path)
        return int(output.strip())

    def get_line_stats(self):
        command = ["git", "log", "--pretty=tformat:", "--numstat"]
        output = run_git_command(command, self.repo_path)

        added = 0
        removed = 0

        for line in output.split("\n"):
            parts = line.split()

            if len(parts) >= 2 and parts[0].isdigit():
                added += int(parts[0])
                removed += int(parts[1])

        return added, removed

    def get_commit_activity(self):
        command = ["git", "log", "--pretty=format:%ad", "--date=short"]
        output = run_git_command(command, self.repo_path)

        activity = defaultdict(int)

        for date in output.split("\n"):
            if date.strip():
                activity[date.strip()] += 1

        return dict(activity)
