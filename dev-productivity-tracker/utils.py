#(git command helper)
import subprocess


def run_git_command(command, repo_path):

    result = subprocess.run(
        command,
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout