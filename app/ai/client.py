from ollama import Client

client = Client(host="http://localhost:11434")


def generate(prompt: str, model: str = "qwen3:8b") -> str:
    response = client.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a cybersecurity analyst. "
                    "Return only the final answer. "
                    "Never reveal your reasoning or thinking."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"].strip()
