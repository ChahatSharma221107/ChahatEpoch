from .models import LLMModel
from .tools import FileTools
from .prompts import DOCSTRING_PROMPT, README_PROMPT
from .planner import TaskPlanner
from .validator import OutputValidator


class DocstringAgent:

    def __init__(self):
        self.model = LLMModel()
        self.validator = OutputValidator(self.model)

    def generate(self, file_path):
        code = FileTools.read_file(file_path)

        if not code.strip():
            print("File is empty.")
            return

        draft = self.model.generate([
            {"role": "system", "content": "You generate docstrings."},
            {"role": "user", "content": DOCSTRING_PROMPT.format(code=code)}
        ])

        improved = self.validator.improve(draft)
        FileTools.write_file(file_path, improved)
        print("Docstrings added successfully.")


class ReadmeAgent:

    def __init__(self):
        self.model = LLMModel()
        self.planner = TaskPlanner(self.model)
        self.validator = OutputValidator(self.model)

    def generate(self, folder_path):
        project_content = FileTools.read_project(folder_path)

        if not project_content.strip():
            print("No Python files found.")
            return

        plan = self.planner.create_plan("Generate comprehensive README")

        draft = self.model.generate([
            {"role": "system", "content": "You generate project documentation."},
            {"role": "user", "content": f"Plan:\n{plan}\n\n{README_PROMPT.format(content=project_content)}"}
        ])

        improved = self.validator.improve(draft)

        FileTools.write_file(f"{folder_path}/README.md", improved)
        print("README generated successfully.")
