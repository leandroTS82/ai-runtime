import random

from itertools import cycle

from groq import Groq

from groq_keys_loader import (
    GROQ_KEYS
)

# ============================================================
# RANDOM KEY ROTATION
# ============================================================

_groq_key_cycle = cycle(
    random.sample(
        GROQ_KEYS,
        len(GROQ_KEYS)
    )
)

# ============================================================
# CLIENT FACTORY
# ============================================================

def _get_client():

    key_info = next(_groq_key_cycle)

    client = Groq(
        api_key=key_info["key"]
    )

    return client, key_info["name"]


# ============================================================
# ASK
# ============================================================

def ask_groq(
    system_prompt: str,
    user_prompt: str
):

    client, key_name = _get_client()

    print(
        f"\n[Groq] Using key: {key_name}"
    )

    response = (
        client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
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