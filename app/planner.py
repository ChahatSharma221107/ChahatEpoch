class TaskPlanner:
    def __init__(self, model):
        self.model = model

    def create_plan(self, task):
        messages = [
            {"role": "system", "content": "You are an expert AI planner."},
            {"role": "user", "content": f"Break this into structured steps:\n{task}"}
        ]
        return self.model.generate(messages)
