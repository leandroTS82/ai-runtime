from review_pipeline import (
    run_review
)

if __name__ == "__main__":

    result = run_review()

    print("\n========== RESULT ==========\n")

    print(result["response"])