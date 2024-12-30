from evaluateExpression import evaluateExpression
from evaluateLine import evaluateLine

with open("file.couleuvre", "r") as doc:
    document = doc.readlines()
    for i in range(len(document)):
        if document[i][-1:] == "\n":
            document[i] = document[i][:-1]


vars = {}
ifStatement = False
skipIndentation = False

# Line evaluation
for line in document:
    if line[:4] == "    ":
        if ifStatement:
            evaluateLine(line[4:], vars, True)
        continue

    result = evaluateLine(line, vars, ifStatement)

    if result:
        ifStatement = True
    elif not result and line[:4] != "    ":
        ifStatement = False


# Type verification
for key, value in vars.items():
    vars[key] = evaluateExpression(value, vars)


print(vars)