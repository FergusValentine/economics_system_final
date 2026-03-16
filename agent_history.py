class AgentHistory:
    def __init__(self):
        self.history = {}

    def get_history(self):
        return self.history

    def record_value(self, category: str, subcategory: str, value):
        if category not in self.history:
            self.history[category] = {}

        if subcategory not in self.history[category]:
            self.history[category][subcategory] = []

        self.history[category][subcategory].append(value)