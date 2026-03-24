import requests

class GitHubIntegration:

    def __init__(self, username):
        self.username = username

    def get_repo_stats(self):
        url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        repos = response.json()

        total_stars = sum(repo["stargazers_count"] for repo in repos)
        total_repos = len(repos)

        return {
            "repos": total_repos,
            "stars": total_stars
        }