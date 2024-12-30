from errors import raise_error
from evaluateExpression import evaluateExpression



def evaluateLine(line, vars, ifstatement):
    # Comment
    if line[0] == "#":
        return

    if not ifstatement and line[:4] == "    ":
        return False

    # If statement
    if line[:2] == "if" and line[-1] == ":":
        global condition
        condition = bool(evaluateExpression(line[2:-1]))
        return condition

    # Else
    if line[:4] == "else":
        return not condition


    # Equality
    for i in range(len(line)):
        if line[i] == "=":
            # Before equality verification
            if i != 0:
                if line[i - 1] == " ":
                    if i - 1 == 0:
                        raise_error("plz put somthing before the =")
                    else:
                        vars[line[:i - 1]] = None
                else:
                    vars[line[:i]] = None
            elif i == 0:
                raise_error("plz put somthing before the =")

            # After equality verification
            if i + 1 <= len(line) - 1:
                if line[i + 1] == "=":
                    raise_error("plz don't enter a comparison operator alone")
                elif line[i + 1] == " ":
                    if i + 1 == len(line) - 1:
                        raise_error("plz put somthing after the =")
                    else:
                        if line[:i] in vars:
                            vars[line[:i]] = line[i + 2:]
                        else:
                            vars[line[:i - 1]] = line[i + 2:]
                else:
                    if line[:i] in vars:
                        vars[line[:i]] = line[i + 1:]
                    else:
                        vars[line[:i - 1]] = line[i + 1:]
            else:
                raise_error("plz put somthing after the =")
            break
