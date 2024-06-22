""" 
author: H24111057 姚博瀚
"""

# Find n-th fibonacci sequence number by recursion.
def fibonacci(n):
    x0 = 0
    x1 = 1
    if n == 0:
        return x0
    elif n == 1:
        return x1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Check if input is non-negative.
while True:
    n = int(input("Input an integer number(non-negative):"))
    if n < 0 or :
        print("Invaid input! On non-negative integer avalible.\nPlease enter again!")
        continue
    else:
        print(f"The {n}-th Fibonacci sequence number is: {fibonacci(n)}")
        break