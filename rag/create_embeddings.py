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
# Create/Open ChromaDB
# ==========================================
client = chromadb.PersistentClient(
    path="rag/vector_db"
)

collection = client.get_or_create_collection(
    name="government_schemes"
)

# ==========================================
# Load All Scraped JSON Files
# ==========================================
print("Loading scraped schemes...")

RAW_FOLDER = "data/raw"

schemes = []

for filename in os.listdir(RAW_FOLDER):

    if filename.endswith(".json"):

        filepath = os.path.join(RAW_FOLDER, filename)

        with open(filepath, "r", encoding="utf-8") as file:

            scheme = json.load(file)

            schemes.append(scheme)

print(f"{len(schemes)} scraped schemes loaded.")

# ==========================================
# Delete Old Embeddings
# ==========================================
try:

    existing = collection.get()

    if existing["ids"]:

        collection.delete(ids=existing["ids"])

except Exception:
    pass

# ==========================================
# Create Embeddings
# ==========================================
print("\nCreating embeddings...\n")

for i, scheme in enumerate(schemes):

    document = f"""
Scheme Name:
{scheme.get('name', '')}

Ministry:
{scheme.get('ministry', '')}

Description:
{scheme.get('description', '')}

Benefits:
{' '.join(scheme.get('benefits', []))}

Eligibility:
{' '.join(scheme.get('eligibility', []))}

Exclusions:
{' '.join(scheme.get('exclusions', []))}

Application Process:
{scheme.get('application_process', '')}

Official Link:
{scheme.get('official_link', '')}
"""

    embedding = model.encode(document).tolist()

    collection.add(

        ids=[str(i)],

        documents=[document],

        embeddings=[embedding],

        metadatas=[

            {
                "name": scheme.get("name", ""),
                "ministry": scheme.get("ministry", ""),
                "url": scheme.get("official_link", "")
            }

        ]

    )

    print(f"✓ Added: {scheme.get('name', '')}")

# ==========================================
# Finished
# ==========================================
print("\n=========================================")
print("Embeddings Created Successfully")
print("Collection Name : government_schemes")
print("Database Folder : rag/vector_db")
print(f"Total Schemes   : {len(schemes)}")
print("=========================================")