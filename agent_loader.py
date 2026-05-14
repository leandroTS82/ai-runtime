from config import AGENTS_DIR


def load_agent(agent_name: str):

    path = (
        AGENTS_DIR
        / agent_name
        / f"{agent_name}.md"
    )

    if not path.exists():

        raise Exception(
            f"Agent not found: {path}"
        )

    return path.read_text(
        encoding="utf-8"
    )