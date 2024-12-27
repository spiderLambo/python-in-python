from type.type import *

# Function to making a tuple from a string
def makeTuple(string):
    # Remove white spaces
    stri = ""
    for element in string:
        if not element == " ":
            stri += element
    string = stri


    for i in range(len(string)):
        if string[i] == ",":
            return Tuple(evaluate(string[:i]), makeTuple(string[i+1:])) # Create a Tuple
    return Tuple(evaluate(string), NoneType()) # End of Tuple



def evaluate(value):
    # Boolean
    if value == "True" or value == "False":
        return Boolean(value)

    # String
    elif (value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'"):
        return String(value[1:-1])

    # Integer
    elif ((value[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or
           (value[0] == "-" and value[1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])) and not
          "." in value):
        return Integer(value)

    # Floating
    elif ((value[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or
           (value[0] == "-" and value[1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])) and
          "." in value):
        return Floating(value)

    # None type
    elif value == "None":
        return NoneType()

    # Tuple
    elif value[0] == "(" and value[-1] == ")":
        return makeTuple(value[1:-1])