import random

from itertools import cycle

from providers.groq.groq_keys_loader import (
    GROQ_KEYS
)

_groq_key_cycle = cycle(
    random.sample(
        GROQ_KEYS,
        len(GROQ_KEYS)
    )
)


def get_next_key():

    return next(_groq_key_cycle)