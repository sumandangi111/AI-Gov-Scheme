import chromadb
from sentence_transformers import SentenceTransformer

# ==========================================
# Load Embedding Model
# ==========================================
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# ==========================================
# Connect to ChromaDB
# ==========================================
client = chromadb.PersistentClient(
    path="rag/vector_db"
)

collection = client.get_collection(
    name="government_schemes"
)


# ==========================================
# Retrieve from Main Database
# ==========================================
def retrieve_schemes(query, top_k=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    retrieved = []

    for doc, metadata in zip(documents, metadatas):

        retrieved.append({
            "name": metadata.get("name", ""),
            "ministry": metadata.get("ministry", ""),
            "url": metadata.get("url", ""),
            "document": doc
        })

    return retrieved


# ==========================================
# Retrieve from Eligible Schemes
# ==========================================
def retrieve_from_eligible_schemes(question, schemes, top_k=3):

    temp_client = chromadb.Client()

    try:
        temp_client.delete_collection("eligible_schemes")
    except Exception:
       pass
 
    temp_collection = temp_client.create_collection(
        name="eligible_schemes"
    )

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

        temp_collection.add(
            ids=[str(i)],
            documents=[document],
            embeddings=[embedding],
            metadatas=[{
                "name": scheme.get("name", ""),
                "ministry": scheme.get("ministry", ""),
                "url": scheme.get("official_link", "")
            }]
        )

    query_embedding = model.encode(question).tolist()

    results = temp_collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, len(schemes))
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    retrieved = []

    for doc, metadata in zip(documents, metadatas):

        retrieved.append({
            "name": metadata.get("name", ""),
            "ministry": metadata.get("ministry", ""),
            "url": metadata.get("url", ""),
            "document": doc
        })

    return retrieved