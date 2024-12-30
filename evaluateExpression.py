from errors import raise_error
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
            return Tuple(evaluateExpression(string[:i]), makeTuple(string[i+1:])) # Create a Tuple
    return Tuple(evaluateExpression(string), NoneType()) # End of Tuple


# Function to making a list from a string
def makeList(string):
    string = rm_whitespace(string)

    for i in range(len(string)):
        if string[i] == ",":
            return List(evaluateExpression(string[:i]), makeList(string[i+1:])) # Create a Tuple
    return List(evaluateExpression(string), NoneType()) # End of Tuple

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
                d.add_key(string[:key], evaluateExpression(string[key+1:]))
        if string[i] == "," and key != -1:
            d.add_key(string[:key], evaluateExpression(string[key+1:i])) # Adding value in d
            makeDic(string[i+1:], d)
            break
    return d


# Function to evaluate an expression
def evaluateExpression(value):
    value = rm_whitespace(value)


    # NOT
    if "not" == value[:3]:
        return not evaluateExpression(value[3:])

    # Addition
    elif "+" in value:
        for i in range(len(value)):
            if value[i] == "+":
                return evaluateExpression(value[:i]) + evaluateExpression(value[i+1:])

    # Multiplication or Power
    elif "*" in value:
        for i in range(len(value)):
            if value[i] == "*" and value[i+1] == "*": # Power
                return evaluateExpression(value[:i]) ** evaluateExpression(value[i + 2:])
            elif value[i] == "*": # Multiplication
                return evaluateExpression(value[:i]) * evaluateExpression(value[i+1:])

    # Division
    elif "/" in value:
        for i in range(len(value)):
            if value[i] == "/" and value[i+1] == "/": # Floor div
                div = evaluateExpression(value[i + 2:])
                if div == Integer(0):
                    raise_error("u can't divide by 0")
                return evaluateExpression(value[:i]) // div
            elif value[i] == "/": # True div
                div = evaluateExpression(value[i+1:])
                if div == Integer(0):
                    raise_error("u can't divide by 0")
                return evaluateExpression(value[:i]) / div

    # Modulo
    elif "%" in value:
        for i in range(len(value)):
            if value[i] == "%":
                div = evaluateExpression(value[i + 1:])
                if div == Integer(0):
                    raise_error("u can't modulo by 0")
                return evaluateExpression(value[:i]) % div

    # AND
    elif "and" in value:
        for i in range(len(value)):
            if value[i:i+3] == "and":
                return evaluateExpression(value[:i]).__and__(evaluateExpression(value[i+3:]))

    # OR
    elif "or" in value:
        for i in range(len(value)):
            if value[i:i + 2] == "or":
                return evaluateExpression(value[:i]).__or__(evaluateExpression(value[i + 2:]))

    # Equality
    elif "==" in value:
        for i in range(len(value)):
            if value[i:i + 2] == "==":
                return evaluateExpression(value[:i]) == evaluateExpression(value[i + 2:])

    # Inequality
    elif "!=" in value:
        for i in range(len(value)):
            if value[i:i + 2] == "!=":
                return evaluateExpression(value[:i]) != evaluateExpression(value[i + 2:])

    # Superior
    elif ">" in value:
        for i in range(len(value)):
            if value[i:i + 2] == ">=": # Superior and Equal
                return evaluateExpression(value[:i]) >= evaluateExpression(value[i + 2:])
            if value[i:i + 1] == ">": # Just Superior
                return evaluateExpression(value[:i]) > evaluateExpression(value[i + 1:])

    # Inferior
    elif "<" in value:
        for i in range(len(value)):
            if value[i:i + 2] == "<=":  # Inferior and Equal
                return evaluateExpression(value[:i]) <= evaluateExpression(value[i + 2:])
            if value[i:i + 1] == "<":  # Just Inferior
                return evaluateExpression(value[:i]) < evaluateExpression(value[i + 1:])

    # Subtraction
    elif "-" in value[1:]:
        for i in range(1, len(value)):
            if value[i] == "-":
                return evaluateExpression(value[:i]) - evaluateExpression(value[i + 1:])



    # Type evaluation
    else:
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

        # Error
        else:
            raise_error(f"{value} doesn't mean anythig")