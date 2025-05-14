# Operator Precedence
precedence = {'/': 1, '*': 1, '+': 2, '-': 2}

# Function to handle precedence of operators
def precedence_of(op):
    return precedence.get(op, 0)

# Function to generate Three-Address Code for a given expression
def generate_tac(expression):
    stack = []  # Stack for operators
    operands = []  # Stack for operands
    temp_count = 1  # Temporary variable counter

    # Tokenize the expression
    tokens = []
    token = ''
    for char in expression:
        if char in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            token += char  # Continue building operand
        else:
            if token:
                tokens.append(token)
                token = ''
            if char in '*/+-()':
                tokens.append(char)  # Add operators and parentheses
    if token:
        tokens.append(token)

    for token in tokens:
        if token.isalnum():  # Operand (variable or constant)
            operands.append(token)
        elif token == '(':  # Left Parenthesis
            stack.append(token)
        elif token == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                operator = stack.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                temp_var = f't{temp_count}'
                temp_count += 1
                operands.append(temp_var)
                print(f'{temp_var} = {operand1} {operator} {operand2}')
            stack.pop()  # Pop the '('
        else:  # Operator (+, -, *, /)
            while stack and precedence_of(stack[-1]) <= precedence_of(token):
                operator = stack.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                temp_var = f't{temp_count}'
                temp_count += 1
                operands.append(temp_var)
                print(f'{temp_var} = {operand1} {operator} {operand2}')
            stack.append(token)

    # Pop remaining operators from the stack
    while stack:
        operator = stack.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        temp_var = f't{temp_count}'
        temp_count += 1
        operands.append(temp_var)
        print(f'{temp_var} = {operand1} {operator} {operand2}')

# Main Program
expression = input("Please enter a simple expression: ").replace('–', '-')
generate_tac(expression)
