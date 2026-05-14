import json

from datetime import datetime

from config import OUTPUT_DIR


def save_output(data):

    filename = (
        datetime.now()
        .strftime("%Y%m%d-%H%M%S")
    )

    output_file = (
        OUTPUT_DIR
        / f"{filename}.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )

    return output_file