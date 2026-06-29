import json
import os

print("Original Scheme Names:")
with open("data/schemes.json", "r", encoding="utf-8") as f:
    original = json.load(f)

for s in original:
    print("-", s["name"])

print("\nScraped Scheme Names:")
for file in os.listdir("data/raw"):
    if file.endswith(".json"):
        with open(os.path.join("data/raw", file), "r", encoding="utf-8") as f:
            scheme = json.load(f)
            print("-", scheme["name"])