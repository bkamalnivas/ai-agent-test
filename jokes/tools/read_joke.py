import os
from smolagents import tool

@tool
def read_joke(joke_id: int) -> str:
    """
    Reads (or tell) a joke.
    The joke is read from a file in /var/tmp/joke_.

    Args:
        joke_id: The number used in the joke filename (e.g. 2 → /var/tmp/joke_2.txt).

    Returns:
        The joke text, or a message if not found.
    """
    path = f"/var/tmp/joke_{joke_id}.txt"
    if not os.path.exists(path):
        return f"No joke found with ID {joke_id}."
    with open(path, "r") as f:
        return f"Joke #{joke_id}: {f.read()}"
