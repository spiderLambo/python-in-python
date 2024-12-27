from type.type import NoneType

class Tuple:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self, i = True):
        if type(self.next) == NoneType:
            return str(self.value) + ")"
        if i:
            return "(" + str(self.value) + ", " + str(self.next.__repr__(False))
        else:
            return str(self.value) + ", " + str(self.next.__repr__(False))
