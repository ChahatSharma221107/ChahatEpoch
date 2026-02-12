import argparse
from .agents import DocstringAgent, ReadmeAgent

def main():
    parser = argparse.ArgumentParser(description="AI Agent CLI")
    parser.add_argument("--docstring", type=str, help="Path to Python file")
    parser.add_argument("--readme", type=str, help="Path to project folder")

    args = parser.parse_args()

    if args.docstring:
        DocstringAgent().generate(args.docstring)

    elif args.readme:
        ReadmeAgent().generate(args.readme)

    else:
        print("Please provide --docstring or --readme option.")

if __name__ == "__main__":
    main()
