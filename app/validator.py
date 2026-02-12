class OutputValidator:
    def __init__(self, model):
        self.model = model

    def improve(self, content):
        messages = [
            {"role": "system", "content": "You are a senior code reviewer."},
            {"role": "user", "content": f"Improve this output and fix issues:\n{content}"}
        ]
        return self.model.generate(messages)
