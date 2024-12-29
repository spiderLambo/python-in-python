from type.type import *

# Remove white spaces
def rm_whitespace(string):
    stri = ""
    for element in string:
        if not element == " ":
            stri += element
    return stri



# Function to making a tuple from a string
def makeTuple(string):
    string = rm_whitespace(string)

    for i in range(len(string)):
        if string[i] == ",":
            return Tuple(evaluate(string[:i]), makeTuple(string[i+1:])) # Create a Tuple
    return Tuple(evaluate(string), NoneType()) # End of Tuple


# Function to making a list from a string
def makeList(string):
    string = rm_whitespace(string)

    for i in range(len(string)):
        if string[i] == ",":
            return List(evaluate(string[:i]), makeList(string[i+1:])) # Create a Tuple
    return List(evaluate(string), NoneType()) # End of Tuple

# Function to making a list from a string
def makeDic(string, d = Dictionary()):
    if string == "":
        return d
    string = rm_whitespace(string)
    key = -1
    for i in range(len(string)):
        if string[i] == ":":
            key = i
            if not "," in string:
                d.add_key(string[:key], evaluate(string[key+1:]))
        if string[i] == "," and key != -1:
            d.add_key(string[:key], evaluate(string[key+1:i])) # Adding value in d
            makeDic(string[i+1:], d)
            break
    return d




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

    # List
    elif value[0] == "[" and value[-1] == "]":
        return makeList(value[1:-1])

    # Dictionnary
    elif value[0] == "{" and value[-1] == "}":
        return makeDic(value[1:-1])