from pathlib import Path

# ============================================================
# TARGET PROJECT
# ============================================================

PROJECT_ROOT = Path(
    r"C:\Dev\AllSetra\allsetra-platform-backend"
)

CLAUDE_DIR = PROJECT_ROOT / ".claude"

AGENTS_DIR = CLAUDE_DIR / "agents"

OUTPUT_DIR = (
    Path(__file__).parent
    / "outputs"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)