import ollama

from rag.retrieve import retrieve_schemes


def ask_ai(user_data):

    question = user_data["question"]

    retrieved_schemes = retrieve_schemes(
        question,
        top_k=3
    )

    if len(retrieved_schemes) == 0:
        return "Sorry, I couldn't find any relevant government scheme."

    print("\n========== RETRIEVED SCHEMES ==========\n")

    for scheme in retrieved_schemes:
        print(scheme["name"])

    print("\n=======================================\n")

    
    context = ""

    for scheme in retrieved_schemes:

        context += f"""

Scheme Name:
{scheme['name']}

Ministry:
{scheme['ministry']}

Official Link:
{scheme['url']}

Details:

{scheme['document']}

"""

    
    prompt = f"""
You are an AI Government Scheme Advisor.

Answer ONLY using the information provided in the context.

Never use outside knowledge.

If the answer is not available in the context, reply exactly:

"I couldn't find that information in the available government scheme data."

========================================

Context:

{context}

========================================

User Question:

{question}

========================================

Instructions:

- Answer only from the given context.
- Keep the answer short, professional, and easy to understand.
- Use Markdown formatting.
- Use headings and bullet points.
- Mention only the information relevant to the user's question.
- Do not repeat the full scheme description.
- If the user asks about benefits, answer only the benefits.
- If the user asks about eligibility, answer only the eligibility.
- If the user asks about exclusions, answer only the exclusions.
- If the user asks about the application process, answer only the application process.
- If the user asks about required documents, mention them only if available.
- Always include the official link at the end if available.
- Never invent information.
"""

    
    response = ollama.chat(

        model="qwen2.5:1.5b",

        options={
            "temperature": 0.0,
            "num_predict": 250
        },

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]