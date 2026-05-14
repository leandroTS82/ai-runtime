from settings import AI_PROVIDER

from providers.groq.groq_provider import (
    GroqProvider
)

from providers.claude.claude_provider import (
    ClaudeProvider
)


def get_provider():

    if AI_PROVIDER == "groq":
        return GroqProvider()

    if AI_PROVIDER == "claude":
        return ClaudeProvider()

    raise Exception(
        f"Unsupported provider: {AI_PROVIDER}"
    )