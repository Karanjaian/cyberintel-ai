from app.ai.client import generate
from app.ai.prompts import build_summary_prompt


def summarize(article_text: str) -> str:
    prompt = build_summary_prompt(article_text)
    return generate(prompt)
