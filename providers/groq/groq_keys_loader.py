import json
import os

# GROQ_KEYS_PATH should contain a JSON array of objects with at least a "key" field, for example: [{'name":"your_key_name","key": "your_groq_api_key"}]
GROQ_KEYS_PATH = (
    r"C:\Users\leand\LTS - CONSULTORIA E DESENVOLVtIMENTO DE SISTEMAS\EKF - English Knowledge Framework - Base\FilesHelper\secret_tokens_keys\GroqKeys.json"
)

# fallback and structure of the keys list if the file is not found or invalid

GROQ_KEYS_FALLBACK = [
    {
        "name": "fallback",
        "key": "gsk_xxx"
    }
]


def load_groq_keys():

    if os.path.exists(GROQ_KEYS_PATH):

        try:

            with open(
                GROQ_KEYS_PATH,
                "r",
                encoding="utf-8"
            ) as f:

                keys = json.load(f)

            if (
                isinstance(keys, list)
                and all(
                    isinstance(k, dict)
                    and "key" in k
                    for k in keys
                )
            ):

                return keys

        except Exception:
            pass

    return GROQ_KEYS_FALLBACK


GROQ_KEYS = load_groq_keys()