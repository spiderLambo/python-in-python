from type.primitivetype.boolean import Boolean

NUMBER_OF_BYTES = 32

# Function to encode absolute value in binary
def dectobinabs(val):
    value = ""
    for i in range(NUMBER_OF_BYTES):
        if val >= 2**(NUMBER_OF_BYTES-1-i):
            val -= 2**(NUMBER_OF_BYTES-1-i)
            value += "1"
        else:
            value += "0"
    return value

# Function to decode binary absolute value
def bintodecabs(val):
    value = 0
    for i in range(NUMBER_OF_BYTES):
        if val[i] == "1":
            value += 2**(NUMBER_OF_BYTES - 1 - i)
    return value

# Function to adding one to a string value
def adding_one(string):
    for i in range(1, NUMBER_OF_BYTES+1):
        if i != 1:
            if string[-i] == "0":
                return f"{string[:-i]}1{string[-i+1:]}"
            else:
                string = f"{string[:-i]}0{string[-i+1:]}"
        else:
            if string[-i] == "0":
                return f"{string[:-i]}1"
            else:
                string = f"{string[:-i]}0"

# Function to remove one to a string value
def rm_one(string):
    if string[-1] == "1":
        return f"{string[:-1]}0"
    else:
        return f"{rm_one(string[:-1])}1"

# Function to change 1 to 0 and 0 to 1
def change1to0and0to1(string):
    value = ""
    for char in string:
        if char == "0":
            value += "1"
        else:
            value += "0"
    return value

# Function to encode in binary
def dectobin(val):
    if val >= 0:
        return dectobinabs(val)
    else:
        return adding_one(change1to0and0to1(dectobinabs(-val)))

# Function to decode binary
def bintodec(string):
    if string[0] == "0":
        return bintodecabs(string)
    else:
        return - bintodecabs(change1to0and0to1(rm_one(string)))



class Integer:
    def __init__(self, value):
        self.__valuebin = dectobin(int(value))
        if int(value) >= 0:
            self.__valueabs = self.__valuebin
            self.__valueopp = dectobin(-int(value))
        else:
            self.__valueabs = dectobin(-int(value))
            self.__valueopp = self.__valuebin

    def __abs__(self):
        if self.__valuebin[0] == "1":
            return Integer(-bintodec(self.__valuebin))
        return Integer(bintodec(self.__valuebin))

    def __add__(self, other):
        return Integer(bintodec(self.__valuebin) + bintodec(other.get_valuebin()))

    def __and__(self, other):
        if bool(self):
            return other
        else:
            return self

    def __or__(self, other):
        if bool(self):
            return self
        else:
            return other

    def __bool__(self):
        return Boolean(str(bintodec(self.__valuebin))).value

    def __mul__(self, other):
        return Integer(bintodec(self.__valuebin) * bintodec(other.get_valuebin()))

    def __truediv__(self, other):
        return Integer(bintodec(self.__valuebin) / bintodec(other.get_valuebin()))

    def __pow__(self, other):
        return Integer(bintodec(self.__valuebin) ** bintodec(other.get_valuebin()))

    def __sub__(self, other):
        return Integer(bintodec(self.__valuebin) - bintodec(other.get_valuebin()))

    def __mod__(self, other):
        return Integer(bintodec(self.__valuebin) % bintodec(other.get_valuebin()))

    def __floordiv__(self, other):
        return Integer(bintodec(self.__valuebin) // bintodec(other.get_valuebin()))

    def __eq__(self, other):
        return self.__valuebin == other.get_valuebin()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return bintodec(self.__valuebin) < bintodec(other.get_valuebin())

    def __le__(self, other):
        return bintodec(self.__valuebin) <= bintodec(other.get_valuebin())

    def __gt__(self, other):
        return bintodec(self.__valuebin) > bintodec(other.get_valuebin())

    def __ge__(self, other):
        return bintodec(self.__valuebin) >= bintodec(other.get_valuebin())

    def get_valuebin(self):
        return self.__valuebin

    def get_valuedec(self):
        return bintodec(self.__valuebin)

    def __repr__(self):
        return str(bintodec(self.__valuebin))


