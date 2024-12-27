from errors import *
from type.type import *

# Function to making a tuple from a string
def makeTuple(string):
    for i in range(len(string)):
        if string[i] == ",":
            return Tuple(string[:i], makeTuple(string[i+1:]))
    return Tuple(string, NoneType())



with open("file.couleuvre", "r") as doc:
    document = doc.readlines()
    for i in range(len(document)):
        if document[i][-1:] == "\n":
            document[i] = document[i][:-1]


vars = {}
for line in document:
    for i in range(len(line)):
        # Equality
        if line[i] == "=":
            # Before equality verification
            if i != 0:
                if line[i-1] == " ":
                    if i - 1 == 0:
                        raise_error("plz put somthing before the =")
                    else:
                        vars[line[:i-1]] = None
                else:
                    vars[line[:i]] = None
            elif i == 0:
                raise_error("plz put somthing before the =")

            # After equality verification
            if i+1 <= len(line)-1:
                if line[i+1] == "=":
                    raise_error("plz don't enter a comparaison operator alone")
                elif line[i+1] == " ":
                    if i+1 == len(line)-1:
                        raise_error("plz put somthing after the =")
                    else:
                        if line[:i] in vars:
                            vars[line[:i]] = line[i+2:]
                        else:
                            vars[line[:i-1]] = line[i + 2:]
                else:
                    if line[:i] in vars:
                        vars[line[:i]] = line[i + 1:]
                    else:
                        vars[line[:i - 1]] = line[i + 1:]
            else:
                raise_error("plz put somthing after the =")

# Type verification
for key, value in vars.items():
    # Boolean
    if value == "True" or value == "False":
        vars[key] = Boolean(value)

    # String
    elif (value[0] == '"'and value[-1] == '"') or (value[0] == "'" and value[-1] == "'"):
        vars[key] = String(value[1:-1])

    # Integer
    elif ((value[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or
          (value[0] == "-" and value[1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])) and not
          "." in value):
        vars[key] = Integer(value)

    # Floating
    elif ((value[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or
          (value[0] == "-" and value[1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])) and
          "." in value):
        vars[key] = Floating(value)

    # None type
    elif value == "None":
        vars[key] = NoneType()

    # Tuple
    elif value[0] == "(" and value[-1] == ")":
        vars[key] = makeTuple(value[1:-1])





print(vars)