class Boolean:
    def __init__(self, value):
        self.value = not (value == "None" or value == "0" or value == "False")

    def __int__(self):
        if not self.value:
            return 1
        else:
            return 0

    def __float__(self):
        if not self.value:
            return 1
        else:
            return 0

    def __str__(self):
        if self.value:
            return "True"
        else:
            return "False"

    def __repr__(self):
        return str(self)
