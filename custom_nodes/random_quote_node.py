# custom_nodes/random_quote_node.py
"""
Custom Node: Random Quote Generator
----------------------------------
This node returns a random motivational quote.
Useful for demos, UI alerts, notifications, study reminders, etc.
"""

import random

QUOTES = [
    "Believe you can and you're halfway there.",
    "Success doesn’t come from what you do occasionally, but what you do consistently.",
    "Dream big, work hard, stay focused.",
    "Every expert was once a beginner.",
    "Discipline beats motivation."
]

def generate_quote():
    """Returns a random motivational quote."""
    return random.choice(QUOTES)

# Node Interface For NodeBox Engine
class RandomQuoteNode:
    def __init__(self):
        self.output = None

    def execute(self):
        self.output = generate_quote()
        return self.output

# Manual Test (not used in node execution)
if __name__ == "__main__":
    print("✨ Random Quote Node Test")
    print(generate_quote())
