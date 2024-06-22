""" 
author: H24111057 姚博瀚
"""

class calculator:
    def __init__(self):
        self.first_num = 0
        self.second_num = 0
        self.operation = None
        
    def calculate(self, first, second, operation):
        if operation == '+':
            return first + second
        elif operation == '-':
            return first - second
        elif operation == '*':
            return first * second
        else:
            if second != 0:
                return first / second
        
    def main(self):
        print("Welcome to simple calculator program!")
        while True:
            self.first_num = float(input("Enter the first number: "))
            self.second_num = float(input("Enter the second number: "))
            self.operation = str(input("Select an arithmetic operation (+, -, *, /): ")).rstrip().lstrip()
            
            # Check if operation is avaliable
            while self.operation not in ['+', '-', '*', '/']:
                print("Not an avaliable operation! Enter again!")
                self.operation = str(input("Select an arithmetic operation (+, -, *, /): ")).rstrip().lstrip()
            
            # Calculation result 
            if self.operation == '/' and self.second_num == 0:
                print("Error: Division by zero!")
            else:
                result = self.calculate(self.first_num, self.second_num, self.operation)
                print(f"Result: {result}")
            
            # Ask if perform anothor
            next_round = str(input("Do you want to perform anothor calculation? (yes or no): ")).lower()
            
            if next_round in ['yes', 'y']:
                continue
            else:
                print("Goodbye!")
                break

# Instance of calculation and run
if __name__ == '__main__':
    calculation = calculator()
    calculation.main()
            