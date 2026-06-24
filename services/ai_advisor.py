import ollama

from services.eligibility import find_schemes


def ask_ai(user_data):

    # User question
    question = user_data["question"]

    # Convert income to integer
    user_data["income"] = int(user_data["income"])

    # Find eligible schemes
    eligible_schemes = find_schemes(user_data)

    # No schemes found
    if len(eligible_schemes) == 0:

        return """
Sorry, no matching schemes were found based on your profile.

Try changing income, occupation, or other details.
"""

    # Create clean scheme text
    scheme_text = ""

    for scheme in eligible_schemes:

        benefits = ", ".join(
            scheme.get("benefits", [])
        )

        documents = ", ".join(
            scheme.get("documents", [])
        )

        scheme_text += f"""
Scheme Name: {scheme['name']}

Benefits:
{benefits}

Documents:
{documents}

"""

    # Build clean prompt
    prompt = f"""
You are a Government Scheme Advisor.

User Profile:

Age: {user_data['age']}
Income: {user_data['income']}
Occupation: {user_data['occupation']}
Gender: {user_data['gender']}
Category: {user_data['category']}
State: {user_data['state']}

User Question:
{question}

Eligible Schemes:

{scheme_text}

Instructions:

- Use ONLY the provided schemes.
- Do NOT repeat the user profile.
- Do NOT explain your reasoning.
- Use simple bullet points.
- Maximum 80 words.
- Format exactly like:

Scheme: PM Kisan
Benefits:
• ₹6000 per year
• Direct Benefit Transfer

Documents:
• Aadhaar Card
• Land Record
• Bank Passbook
"""

    # Debug prompt
    print("========== PROMPT ==========")
    print(prompt)
    print("============================")

    # Call TinyLlama
    response = ollama.chat(
       model="qwen2.5:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]