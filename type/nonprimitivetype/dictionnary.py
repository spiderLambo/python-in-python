from type.type import NoneType, List


# Hash Table
HWIDTH = 109
def Hash_table(key):
    code = 0
    for char in key:
        code += ord(char)

    return code % HWIDTH

class Dictionary:
    def __init__(self):
        self.dict = List(NoneType()) * HWIDTH

    def add_key(self, key, value):
        h = Hash_table(str(key))
        if self.dict[h] == NoneType():
            self.dict[h] = List()
        self.dict[h].insert(0, List(key, List(value)))

    def get_value(self, key):
        h = Hash_table(str(key))
        if self.dict[h] == NoneType():
            return NoneType()
        for k, v in self.dict[h]:
            if key == k:
                return v
        return NoneType()

    def keys(self):
        t = List()
        i = 0
        while i < len(self.dict):
            list = self.dict[i]
            if not list == NoneType():
                j = 0
                while j < len(list):
                    key = list[j]
                    t.append(key)
                    j += 1
            i+=1
        return t

    def __repr__(self):
        text = "{"
        i = 0
        while i < len(self.keys()):
            key = self.keys()[i]
            if type(key) == List:
                text += f'{key[0]} : {key[1]}, '
            i += 1
        if i == 1:
            return "{}"
        else:
            return text[:-2] + "}"