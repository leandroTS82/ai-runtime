from groq import Groq

from providers.base_provider import (
    BaseProvider
)

from providers.groq.groq_settings import (
    MODEL,
    TEMPERATURE
)

from providers.groq.groq_key_rotation import (
    get_next_key
)


class GroqProvider(BaseProvider):

    def ask(
        self,
        system_prompt,
        user_prompt
    ):

        key_info = get_next_key()

        print(
            f"\n[Groq] Using key: "
            f"{key_info['name']}"
        )

        client = Groq(
            api_key=key_info["key"]
        )

        response = (
            client.chat.completions.create(
                model=MODEL,
                temperature=TEMPERATURE,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )