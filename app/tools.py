import os

class FileTools:

    @staticmethod
    def read_file(path):
        if not os.path.exists(path):
            return ""
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def read_project(folder_path):
        content = ""
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    content += f"\n\n# File: {full_path}\n"
                    content += FileTools.read_file(full_path)
        return content

    @staticmethod
    def write_file(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
