""" 
author: H24111057 姚博瀚
"""

class Solution:
    def calculate(self, s):
        def update(op, v):
            # This function updates the stack based on the current operation
            if op == "+":
                stack.append(v)
            if op == "-":
                stack.append(-v)
            if op == "*":
                stack.append(stack.pop() * v)
            if op == "/":
                stack.append(float(stack.pop() / v))

        it, num, stack, sign = 0, 0, [], "+"  # Initialize iterator, current number, stack, and sign

        while it < len(s):
            if s[it].isdigit() or s[it] == '.':
                # If the character is a digit or a decimal point, build the current number
                num = num * 10 + float(s[it]) if s[it] != '.' else num
            elif s[it] in "+-*/":
                # If the character is an operator, update the stack with the current number
                update(sign, num)
                num, sign = 0, s[it]  # Reset number and update sign
            elif s[it] == "(":
                # If the character is '(', recursively calculate the expression inside parentheses
                num, j = self.calculate(s[it + 1:])
                it += j  # Move the iterator past the closing ')'
            elif s[it] == ")":
                # If the character is ')', update the stack and return the result and the iterator position
                update(sign, num)
                return sum(stack), it + 1
            elif s[it] == "q":
                # If the character is 'q', return the quit signal and the iterator position
                return "quit", it + 1
            elif s[it] != " ":
                # If the character is not a space and not recognized, return an error
                return "Unsupported character error: {}".format(s[it]), it
            it += 1
        update(sign, num)  # Final update for the last number in the expression
        return sum(stack), it

def validate_expression(expression):
    # This function validates the expression for common errors

    # Check for unbalanced parentheses
    if expression.count('(') != expression.count(')'):
        return "Error: Unbalanced parentheses"
    
    # Check for incomplete operators
    operators = set("+-*/")
    last_char = ""
    for i, char in enumerate(expression):
        if char in operators:
            # If an operator is at the start, after another operator, or after an opening parenthesis, it's an error
            if i == 0 or (last_char in operators or last_char == "(" or last_char == ""):
                return "Error: Operand error"
        last_char = char
    
    if last_char in operators:
        # If the expression ends with an operator, it's an error
        return "Error: Operand error"

    return "Valid"

def evaluate_expression(expression):
    # This function evaluates the expression after validating it

    solution = Solution()
    validation_result = validate_expression(expression)
    if validation_result != "Valid":
        return validation_result  # Return the validation error if any
    result, index = solution.calculate(expression)
    return result

while True:
    expression = input("Enter an arithmetic expression (or 'q' to quit): ")
    if expression == "q":
        print("Quitting...")
        break
    try:
        result = evaluate_expression(expression)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except IndexError:
        print("Error: Unbalanced parentheses")
    except ValueError:
        print("Error: Operand error")
    except Exception as e:
        print("Error:", e)
