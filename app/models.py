from openai import OpenAI
from .config import Config

class LLMModel:
    def __init__(self):
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def generate(self, messages):
        response = self.client.chat.completions.create(
            model=Config.MODEL_NAME,
            messages=messages,
            temperature=Config.TEMPERATURE,
            max_tokens=Config.MAX_TOKENS
        )
        return response.choices[0].message.content
