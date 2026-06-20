from langchain_community.llms import Ollama
from config import OLLAMA_MODEL

llm = Ollama(model=OLLAMA_MODEL)

def ask_llm(question, context):
    prompt = f"""
You are a Banking Assistant. Answer ONLY using the context below.

STRICT RULES:
- ONLY use information from the Context provided
- If answer is NOT in context say: "I don't have that information in my documents."
- Do NOT use your own knowledge or make up numbers
- Be specific with exact amounts and figures from context

Context:
{context}

Question:
{question}

Answer (based only on context above):
"""
    return llm.invoke(prompt)