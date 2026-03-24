import subprocess

def run_git_command(command, repo_path):
    try:
        result = subprocess.run(
            command,
            cwd=str(repo_path),   # ensure string
            capture_output=True,
            text=True,
            shell=True            # 🔥 IMPORTANT FIX
        )

        if result.returncode != 0:
            print("Git Error:", result.stderr)
            return ""

        return result.stdout.strip()

    except Exception as e:
        print("Execution Error:", e)
        return ""
