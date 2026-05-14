import subprocess

from config import PROJECT_ROOT


def get_git_diff():

    commands = [
        ["git", "diff", "HEAD"],
        ["git", "diff"]
    ]

    for command in commands:

        try:

            output = subprocess.check_output(
                command,
                text=True,
                cwd=PROJECT_ROOT
            )

            if output.strip():

                print(
                    f"\n[Git] Using: {' '.join(command)}"
                )

                return output

        except Exception:
            pass

    return "NO_DIFF_FOUND"