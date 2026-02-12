from app.models import LLMModel

llm = LLMModel()

response = llm.generate([
    {"role": "user", "content": "Hello"}
])

print(response)
