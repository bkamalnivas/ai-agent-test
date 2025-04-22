from smolagents import CodeAgent, LiteLLMModel, FinalAnswerTool
from tools.write_joke import write_joke
from tools.read_joke import read_joke
from tools.list_jokes import list_total_jokes

# Connect to local Ollama model
llm_local = LiteLLMModel(
    model_id="ollama/gemma3:4b",
    api_base="http://localhost:11434"
)

llm = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash",
    api_key="xxx"
)

agent = CodeAgent(
    tools=[write_joke, read_joke, list_total_jokes, FinalAnswerTool()],
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
)


print("🎭 Joke Agent (smolagents + Gemma via Ollama)\nType 'exit' to quit")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        break
    output = agent.run(user_input)
    print("🤖:", output)

