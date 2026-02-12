DOCSTRING_PROMPT = """
You are a senior Python developer.

Add professional docstrings to all:
- Functions
- Classes
- Methods

Handle edge cases like:
- Missing parameters
- Incomplete functions
- Empty files

Return full updated code only.

Code:
{code}
"""

README_PROMPT = """
You are a senior software architect.

Generate a professional README.md including:

- Project Overview
- Architecture
- Installation
- Usage
- File Structure
- Assumptions
- Limitations

Project Content:
{content}
"""
