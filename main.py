import importlib
import sys

from review_pipeline import (
    run_review
)

# ============================================================
# REQUIRED PACKAGES
# ============================================================

REQUIRED_PACKAGES = [
    "groq",
    "anthropic"
]

# ============================================================
# VALIDATE DEPENDENCIES
# ============================================================

def validate_dependencies():

    missing = []

    for package in REQUIRED_PACKAGES:

        try:

            importlib.import_module(package)

        except ImportError:

            missing.append(package)

    if missing:

        print("\n[ERROR] Missing packages:\n")

        for pkg in missing:

            print(f" - {pkg}")

        print(
            "\nRun:\n"
            "pip install -r requirements.txt\n"
        )

        sys.exit(1)

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("\n===================================")
    print(" AI Runtime")
    print("===================================\n")

    validate_dependencies()

    result = run_review()

    print("\n========== RESULT ==========\n")

    print(result)