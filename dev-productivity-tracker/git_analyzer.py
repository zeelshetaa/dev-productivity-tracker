#this is core logic file for git analyzer
import subprocess
from utils import run_git_command


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

    def get_files_changed(self):
        command = ["git", "log", "--name-only", "--pretty=format:"]
        output = run_git_command(command, self.repo_path)

        files = set()

        for line in output.split("\n"):
            if line.strip():
                files.add(line.strip())

        return len(files)