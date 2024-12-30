class String:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return String(self.value + other.value)

    def __mul__(self, other):
        return String(self.value * other.get_valuedec())

    def __repr__(self):
        return self.value