import os
import json
import chromadb
from sentence_transformers import SentenceTransformer

# ==========================================
# Load Embedding Model
# ==========================================
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ==========================================
# ChromaDB
# ==========================================
client = chromadb.PersistentClient(path="rag/vector_db")

collection = client.get_or_create_collection(
    name="government_schemes"
)

# ==========================================
# Delete old embeddings
# ==========================================
try:
    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

except:
    pass

scheme_count = 0

# ==========================================
# 1. Load Manual Schemes
# ==========================================
print("\nLoading manual schemes...")

with open(
    "data/schemes.json",
    "r",
    encoding="utf-8"
) as file:

    manual_schemes = json.load(file)

print(f"{len(manual_schemes)} manual schemes loaded.")

for scheme in manual_schemes:

    document = f"""
Scheme Name:
{scheme.get('name','')}

Occupation:
{scheme.get('occupation','')}

Maximum Income:
{scheme.get('max_income','')}

Minimum Age:
{scheme.get('min_age','')}

Maximum Age:
{scheme.get('max_age','')}

Gender:
{scheme.get('gender','')}

Category:
{scheme.get('category','')}

State:
{scheme.get('state','')}

Benefits:
{', '.join(scheme.get('benefits',[]))}

Required Documents:
{', '.join(scheme.get('documents',[]))}

Official Link:
{scheme.get('apply_link','')}
"""

    embedding = model.encode(document).tolist()

    collection.add(
        ids=[str(scheme_count)],
        documents=[document],
        embeddings=[embedding],
        metadatas=[{
            "name": scheme.get("name",""),
            "ministry": "Government of India",
            "url": scheme.get("apply_link","")
        }]
    )

    print(f"✓ Added: {scheme['name']}")

    scheme_count += 1

# ==========================================
# 2. Load Scraped Schemes
# ==========================================
print("\nLoading scraped schemes...")

raw_folder = "data/raw"

files = [
    f for f in os.listdir(raw_folder)
    if f.endswith(".json")
]

print(f"{len(files)} scraped schemes found.")

for filename in files:

    filepath = os.path.join(raw_folder, filename)

    with open(filepath, "r", encoding="utf-8") as file:

        scheme = json.load(file)

    document = f"""
Scheme Name:
{scheme.get('name','')}

Ministry:
{scheme.get('ministry','')}

Description:
{scheme.get('description','')}

Benefits:
{' '.join(scheme.get('benefits',[]))}

Eligibility:
{' '.join(scheme.get('eligibility',[]))}

Exclusions:
{' '.join(scheme.get('exclusions',[]))}

Application Process:
{scheme.get('application_process','')}

Official Link:
{scheme.get('official_link','')}
"""

    embedding = model.encode(document).tolist()

    collection.add(

        ids=[str(scheme_count)],

        documents=[document],

        embeddings=[embedding],

        metadatas=[{

            "name": scheme.get("name",""),

            "ministry": scheme.get("ministry",""),

            "url": scheme.get("official_link","")

        }]
    )

    print(f"✓ Added: {scheme['name']}")

    scheme_count += 1

print("\n=========================================")
print("Embeddings Created Successfully")
print("Collection Name : government_schemes")
print(f"Total Schemes   : {scheme_count}")
print("=========================================")