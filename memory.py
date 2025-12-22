class Memory:
    def __init__(self):
        self.data = {
            "age": None,
            "income": None,
            "state": None
        }

    def update(self, key, value):
        self.data[key] = value

    def get_missing(self):
        return [k for k, v in self.data.items() if v is None]
