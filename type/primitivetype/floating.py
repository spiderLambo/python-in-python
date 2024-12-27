from type.primitivetype.integer import NUMBER_OF_BYTES
from type.type import Integer
from  errors import raise_error

class Floating:
    def __init__(self, value):
        self.__is_negative = value[0] == "-"
        for i in range(len(value)):
            if value[i] == ".":
                self.__integerpart = Integer(value[:i])
                if i+1 < len(value):
                    self.__decpart = Integer(value[i+1:])
                else:
                    raise_error("plz put something after the .")

    def __repr__(self):
        if self.__is_negative and self.__integerpart.get_valuebin() == "0" * NUMBER_OF_BYTES:
            return f"-{self.__integerpart}.{self.__decpart}"
        else:
            return f"{self.__integerpart}.{self.__decpart}"