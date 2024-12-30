from type.primitivetype.Nonetype import NoneType
from type.primitivetype.integer import Integer, NUMBER_OF_BYTES, bintodec
from  errors import raise_error

class Floating:
    def __init__(self, value = NoneType(), integerpart = NoneType(), decpart = NoneType()):
        if NoneType() != value:
            self.__is_negative = value[0] == "-"
            for i in range(len(value)):
                if value[i] == ".":
                    self.__integerpart = Integer(value[:i])
                    if i+1 < len(value):
                        self.__decpart = Integer(value[i+1:])
                    else:
                        raise_error("plz put something after the .")
        else:
            self.__is_negative = integerpart < Integer(0)
            self.__integerpart = integerpart
            self.__decpart = decpart

    def __abs__(self):
        self.__integerpart = abs(self.__integerpart)
        if self.__is_negative:
            self.__is_negative = False

    def __add__(self, other):
        return Floating(integerpart= self.__integerpart + other.get_integerpart(),
                        decpart= self.__decpart + other.get_decpart())

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
        return not (self.__integerpart == Integer(0) and self.__decpart == Integer(0))

    def __mul__(self, other):
        return Floating(integerpart= self.__integerpart * other.get_integerpart(),
                        decpart= (self.__decpart * other.get_decpart()) +
                        self.__integerpart * other.get_decpart() +
                        self.__decpart * self.__integerpart)

    def __sub__(self, other):
        return Floating(integerpart=self.__integerpart - other.get_integerpart(),
                        decpart=self.__decpart - other.get_decpart())

    def __eq__(self, other):
        return self.__integerpart == other.get_integerpart() and self.__decpart == other.get_decpart()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.__integerpart < other.get_integerpart() and self.__decpart < other.get_decpart()

    def __le__(self, other):
        return self.__integerpart <= other.get_integerpart() and self.__decpart <= other.get_decpart()

    def __gt__(self, other):
        return self.__integerpart > other.get_integerpart() and self.__decpart > other.get_decpart()

    def __ge__(self, other):
        return self.__integerpart >= other.get_integerpart() and self.__decpart >= other.get_decpart()

    def get_decpart(self):
        return self.__decpart

    def get_integerpart(self):
        return self.__integerpart

    def __repr__(self):
        if self.__is_negative and self.__integerpart.get_valuebin() == "0" * NUMBER_OF_BYTES:
            return f"-{self.__integerpart}.{self.__decpart}"
        else:
            return f"{self.__integerpart}.{self.__decpart}"

