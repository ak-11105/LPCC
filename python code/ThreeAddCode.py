precedence = [['/', '1'], ['*', '1'], ['+', '2'], ['-', '2']]

def precedenceof(s):
    for x in precedence:
        if x[0] == s:
            return x[1]

# Main program
expression = input("Please enter a simple expression: ").replace('–', '-')
expr = expression.replace('(', '').replace(')', '')  # Remove parentheses
l = len(expr)
processed = [False] * l
operator = []

# Detect operators and store their precedence and position
for i in range(0, l):
    x = expr[i]
    for j in range(0, 4):
        if x == precedence[j][0]:
            temp = [precedence[j][1], x, i]
            operator.append(temp)
            break

operator.sort()  # Sort based on precedence

for i in range(0, len(operator)):
    opt1 = ""
    opt2 = ""
    j = operator[i][2]  # location of operator

    if processed[j - 1] == True:
        if i > 0 and operator[i - 1][0] == operator[i][0]:
            opt1 = "t" + str(i)
        else:
            for x in range(0, len(operator)):
                if j - 2 == operator[x][2]:
                    opt1 = "t" + str(x + 1)
    else:
        opt1 = expr[j - 1]

    if processed[j + 1] == True:
        for x in range(0, len(operator)):
            if j + 2 == operator[x][2]:
                opt2 = "t" + str(x + 1)
    else:
        opt2 = expr[j + 1]

    processed[j + 1] = True
    processed[j - 1] = True
    processed[j] = True

    print(f"t{i + 1} = {opt1} {operator[i][1]} {opt2}")