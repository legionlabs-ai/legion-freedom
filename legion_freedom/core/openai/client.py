from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client = OpenAI()


def ask_ai(prompt: str, model: str = "gpt-4.1-mini") -> str:
    response = _client.responses.create(
        model=model,
        input=prompt
    )
    return response.output_text