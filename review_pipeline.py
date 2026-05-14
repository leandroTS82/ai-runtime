from agent_loader import (
    load_agent
)

from state_manager import (
    save_output_markdown
)

from tools.git_tools import (
    get_git_diff
)

from providers.provider_factory import (
    get_provider
)

provider = get_provider()


def run_review():

    print("\n[Pipeline] review")

    diff = get_git_diff()

    if diff == "NO_DIFF_FOUND":

        return {
            "pipeline": "review",
            "status": "NO_CHANGES"
        }

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

    response = provider.ask(
        system_prompt=security_prompt,
        user_prompt=user_prompt
    )

    result = {
        "pipeline": "review",
        "provider": provider.__class__.__name__,
        "agent": "security",
        "response": response
    }

    output_file = save_output_markdown(result)

    print(
        f"\nSaved output:\n{output_file}"
    )

    return result