class Boolean:
    def __init__(self, value):
        self.__value = value == "None" or value == "0" or value == "False"

    def __int__(self):
        if not self.__value:
            return 1
        else:
            return 0

    def __float__(self):
        if not self.__value:
            return 1
        else:
            return 0

    def __str__(self):
        if self.__value:
            return "True"
        else:
            return "False"

    def __repr__(self):
        return str(self)
