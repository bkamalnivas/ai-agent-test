from smolagents import CodeAgent, LiteLLMModel, FinalAnswerTool
from tools.write_joke import write_joke
from tools.read_joke import read_joke
from tools.list_jokes import list_total_jokes
from smolagents import tool

# Connect to local Ollama model
llm_local = LiteLLMModel(
    model_id="ollama/gemma3:4b",
    api_base="http://localhost:11434"
)

llm = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",
)

@tool
def unknown_request_handler() -> str:
    """
    Handles unrecognized or irrelevant user requests.

    Returns:
        A polite message saying the request can't be handled.
    """
    return "Sorry, I can only write, read, or list jokes. I can't help with that request."


@tool
def unknown_request_handler() -> str:
    """
    Handles unrecognized or unsupported user requests.

    Returns:
        A message telling the user what this assistant can do.
    """
    return (
        "Sorry, I can't help with that. "
        "I can only write a joke, read a joke by ID, or list how many jokes are saved."
    )

agent = CodeAgent(
    tools=[write_joke, read_joke, list_total_jokes, unknown_request_handler, FinalAnswerTool()],
    model=llm
)

# Override the default system prompt
agent.system_prompt = (
    "You are a tool-using assistant that manages jokes stored in /var/tmp.\n"
    "You can use the tools 'write_joke', 'read_joke', and 'list_total_jokes'.\n"
    "Each tool performs exactly one job.\n"
    "Once the task is complete, ALWAYS call FinalAnswerTool with the final response.\n"
    "Do NOT keep calling tools endlessly.\n"
    "Avoid chatting — always respond through tools."
    "If a user request doesn't match any of these tools, respond by calling unknown_request_handler()."
)


print("🎭 Joke Agent (smolagents + Gemma via Ollama)\nType 'exit' to quit")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        break
    output = agent.run(user_input)
    print("🤖:", output)

