import json
import os


def load_tasks(filename="tasks.json"):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print(
            "⚠️  Warning: tasks.json is corrupted or invalid. Starting with an empty list.")
        return []


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)
