from app.core.config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def generate_multimodal_response(query: str, context: str):
    prompt = f"""
Tu es un assistant multimodal utilisant un système RAG.

CONTEXTE MULTIMODAL :
{context}

INSTRUCTIONS :
- Utilise uniquement les informations du contexte
- Ne fais aucune supposition.
- Ne mentionne pas le système interne.

QUESTION :
{query}

RÉPONSE :
"""

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant multimodal RAG strict."},
            {"role": "user", "content": prompt}
        ]
    )

    return resp.choices[0].message.content.strip()