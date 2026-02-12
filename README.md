# AI Documentation Agent

## Overview
This project implements two AI Agents:

1. Docstring Generation Agent
2. Project README Generation Agent

The system follows a multi-agent architecture with planning and validation stages.

## Architecture

User Input
    ↓
Planner Agent
    ↓
Generator Agent
    ↓
Validator Agent
    ↓
Final Output

## Features

- Modular design
- Multi-agent orchestration
- Self-validation loop
- Handles empty files
- Supports nested project folders
- CLI-based execution

## Installation

pip install -r requirements.txt

## Usage

Generate docstrings:
python -m app --docstring path/to/file.py

Generate README:
python -m app --readme path/to/project

## Assumptions

- Python-based projects
- OpenAI API key available

## Limitations

- Very large projects may require chunking
- Non-Python files are ignored
