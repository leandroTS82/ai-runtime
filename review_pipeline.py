import subprocess

from config import PROJECT_ROOT

from client import ask_groq

from agent_loader import (
    load_agent
)

from state_manager import (
    save_output
)


def get_git_diff():

    try:

        output = subprocess.check_output(
            ["git", "diff"],
            text=True,
            cwd=PROJECT_ROOT
        )

        return output

    except Exception as ex:

        return str(ex)


def run_review():

    print("\n[Pipeline] review")

    diff = get_git_diff()

    security_prompt = load_agent(
        "security"
    )

    user_prompt = f"""
Review the following git diff.

Focus on:
- security
- multi tenancy
- auth
- secrets
- vulnerabilities

Return concise findings.

GIT DIFF:

{diff}
"""

    response = ask_groq(
        system_prompt=security_prompt,
        user_prompt=user_prompt
    )

    result = {
        "pipeline": "review",
        "agent": "security",
        "response": response
    }

    output_file = save_output(result)

    print(
        f"\nSaved output:\n{output_file}"
    )

    return result