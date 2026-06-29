import json
import os


def save_json(data):

    os.makedirs("data/raw", exist_ok=True)

    filename = (
        data["name"]
        .lower()
        .replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
        .replace("/", "_")
    )

    filepath = f"data/raw/{filename}.json"

    with open(filepath, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved: {filepath}")