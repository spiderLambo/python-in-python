from errors import raise_error

# Comment

def evaluateLine(line, vars):
    # Comment
    if line[0] == "#":
        return


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