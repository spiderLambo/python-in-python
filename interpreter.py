from errors import *
from evaluate import evaluate

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
print(vars)
# Type verification
for key, value in vars.items():
    vars[key] = evaluate(value)


print(vars)
print(type(vars['o'].next.value))