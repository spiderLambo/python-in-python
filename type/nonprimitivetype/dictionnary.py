from type.type import NoneType


# Hash Table
HWIDTH = 109
def Hash_table(key):
    code = 0
    for char in key:
        code += ord(char)

    return code % HWIDTH

class Dictionary:
    def __init__(self):
        self.dict = [NoneType()] * HWIDTH

    def add_key(self, key, value):
        h = Hash_table(key)
        if self.dict[h] == NoneType():
            self.dict[h] = []
        self.dict[h].insert(1, [key, value])

    def get_value(self, key):
        h = Hash_table(key)
        if self.dict[h] == NoneType():
            return NoneType()
        for k, v in self.dict[h]:
            if key == k:
                return v
        return NoneType()

    def keys(self):
        t = []
        for list in self.dict:
            if not list == NoneType():
                for key, _ in list:
                    t.append(key)
        return t

