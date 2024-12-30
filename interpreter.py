from evaluateExpression import evaluateExpression
from evaluateLine import evaluateLine

with open("file.couleuvre", "r") as doc:
    document = doc.readlines()
    for i in range(len(document)):
        if document[i][-1:] == "\n":
            document[i] = document[i][:-1]


vars = {}

# Line evaluation
for line in document:
    evaluateLine(line, vars)


# Type verification
for key, value in vars.items():
    vars[key] = evaluateExpression(value)


print(vars)