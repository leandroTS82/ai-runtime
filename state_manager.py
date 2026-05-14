from datetime import datetime

from config import OUTPUT_DIR


def save_output_markdown(result):

    filename = (
        datetime.now()
        .strftime("%Y%m%d-%H%M%S")
    )

    output_file = (
        OUTPUT_DIR
        / f"{filename}-review.md"
    )

    markdown = f"""
# AI Runtime Review

## Pipeline
{result.get("pipeline")}

## Provider
{result.get("provider")}

## Agent
{result.get("agent")}

---

# Response

{result.get("response")}
"""

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(markdown)

    return output_file