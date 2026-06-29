from rag.retrieve import retrieve_schemes

results = retrieve_schemes(
    "Business loan for women"
)

print()

print("=" * 50)

for scheme in results:

    print(scheme)

    print("-" * 50)