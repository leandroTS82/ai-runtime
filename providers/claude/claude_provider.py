from providers.base_provider import (
    BaseProvider
)


class ClaudeProvider(BaseProvider):

    def ask(
        self,
        system_prompt,
        user_prompt
    ):

        raise NotImplementedError(
            "Claude provider not implemented yet."
        )