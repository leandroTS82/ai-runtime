class BaseProvider:

    def ask(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:

        raise NotImplementedError