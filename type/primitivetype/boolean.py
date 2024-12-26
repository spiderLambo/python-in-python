class Boolean:
    def __init__(self, value):
        self.value = value == "None" or value == "0" or value == "False"

    def __repr__(self):
        return str(self.value)