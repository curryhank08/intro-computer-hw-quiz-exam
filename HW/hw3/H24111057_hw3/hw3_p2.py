"""
author: H24111057 統計系 姚博瀚
"""
def evaluate_polynomial(poly_str, x_value):
    # Convert the polynomial string into a list of tokens
    tokens = []
    i = 0
    while i < len(poly_str):
        if poly_str[i].isdigit():
            # Combine consecutive digits into a single number
            num = ""
            while i < len(poly_str) and poly_str[i].isdigit():
                num += poly_str[i]
                i += 1
            tokens.append(int(num))
            continue
        tokens.append(poly_str[i])
        i += 1

    # Replace 'X' with the given value
    for i in range(len(tokens)):
        if tokens[i] == "X":
            tokens[i] = x_value

    # Evaluate the expression
    operators = ['^', '*', '+', '-']
    for op in operators:
        i = 0
        while i < len(tokens):
            if tokens[i] == op:
                if op == '^':
                    result = tokens[i - 1] ** tokens[i + 1]
                elif op == '*':
                    result = tokens[i - 1] * tokens[i + 1]
                elif op == '+':
                    result = tokens[i - 1] + tokens[i + 1]
                elif op == '-':
                    result = tokens[i - 1] - tokens[i + 1]
                # Replace the operator and operands with the result
                tokens[i] = result
                del tokens[i + 1]
                del tokens[i - 1]
                # Reset index for re-evaluating the expression
                i = 0
                continue
            i += 1

    # The final result will be the only remaining element in the list
    return tokens[0]

# Input polynomial and value of X
poly = input("Input polynomial: ")
x = int(input("Input the value of X: "))

# Evaluate the polynomial and print the result
result = evaluate_polynomial(poly, x)
print("Evaluated Result:", result)
