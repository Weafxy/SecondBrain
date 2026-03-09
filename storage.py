import json
import os

class Storage:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                content = f.read().strip()
                return json.loads(content) if content else []
        except json.JSONDecodeError:
            return []

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)
            