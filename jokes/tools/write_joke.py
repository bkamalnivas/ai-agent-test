import os
import random
from smolagents import tool

@tool
def write_joke() -> str:
    """
    Writes a random joke to a new file in /var/tmp.

    Returns:
        A confirmation message with the saved joke and its ID.
    """
    jokes = [
        "Why did the computer show up late? It had a hard drive!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "How many programmers does it take to change a light bulb? None, it's a hardware issue."
    ]
    joke = random.choice(jokes)
    existing = [f for f in os.listdir("/var/tmp") if f.startswith("joke_") and f.endswith(".txt")]
    new_id = len(existing)
    path = f"/var/tmp/joke_{new_id}.txt"
    with open(path, "w") as f:
        f.write(joke)
    return f"Saved joke #{new_id}: {joke}"

