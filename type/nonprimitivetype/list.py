from type.type import NoneType

class List:
    def __init__(self, value = "" , next = NoneType()):
        self.value = value
        self.next = next

    def __len__(self):
        last = self
        i = 1
        while NoneType() != last.next:
            last = last.next
            i += 1
        return i

    def __mul__(self, other):
        if other <= 1:
            return List(self.value)
        else:
            return List(self.value, self * (other-1))

    def append(self, value):
        last = self
        while NoneType() != last.next:
            last = last.next
        last.next = List(value, NoneType())
        return last.next

    def clear(self):
        self.value = ""
        self.next = NoneType()

    def copy(self):
        if NoneType() == self.next:
            return List(self.value)
        else:
            return List(self.value, self.next.copy())

    def count(self, val, i = 0):
        if self.value == val:
            i += 1
        if NoneType() == self.next:
            return i
        else:
            return self.next.count(val, i)

    def extend(self, other):
        last = self
        while NoneType() != last.next:
            last = last.next
        last.next = other

    def index(self, val, i = 0):
        if val == self.value:
            return i
        if NoneType() == self.next:
            return False
        else:
            return self.next.index(val, i + 1)

    def insert(self, pos, val):
        if pos == 0:
            self.next = List(self.value, self.next)
            self.value = val
        else:
            self.next.insert(pos-1, val)

    def pop(self, pos = 0):
        if pos == 1 and NoneType() == self.next.next:
            self.next = NoneType()
        elif pos == 0:
            self.value = self.next.value
            self.next = self.next.next
        else:
            self.next.pop(pos-1)

    def remove(self, key):
        if self.next.value == key and NoneType() == self.next.next:
            self.next = NoneType()
        elif self.value == key:
            self.value = self.next.value
            self.next = self.next.next
        else:
            self.next.remove(key)

    def __repr__(self):
        if len(self) == 1:
            return "[" + str(self.value) + "]"
        else:
            return "[" + str(self.value) + ", " + str(self.next.__repr__())[1:]

    def __getitem__(self, item):
        if item == 0:
            return self.value
        else:
            last = self
            for i in range(item):
                if NoneType() != last.next:
                    last = last.next
            return last.value

    def __setitem__(self, key, value):
        if key == 0:
            self.value = value
        else:
            self.next[key-1] = value

    def __contains__(self, item):
        if self.value == item:
            return True
        elif NoneType() == self.next:
            return False
        else:
            return item in self.next