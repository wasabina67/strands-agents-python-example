from strands import Agent
from strands.models.openai import OpenAIModel


def main():
    model = OpenAIModel(model_id="gpt-4o")
    agent = Agent(model=model)
    agent("Please tell me about Agentic AI.")


if __name__ == "__main__":
    main()
