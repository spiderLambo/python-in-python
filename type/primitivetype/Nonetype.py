class NoneType:
    def __eq__(self, other):
        return other == None

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "None"