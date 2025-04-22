import os
from smolagents import tool

@tool
def list_total_jokes() -> str:
    """
    Counts the number of joke files in /var/tmp.

    Returns:
        A message with the total number of saved jokes.
    """
    count = len([f for f in os.listdir("/var/tmp") if f.startswith("joke_") and f.endswith(".txt")])
    return f"There are {count} joke(s) saved."

