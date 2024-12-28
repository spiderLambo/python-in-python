class NoneType:
    def __eq__(self, other):
        return other == None

    def __repr__(self):
        return "None"