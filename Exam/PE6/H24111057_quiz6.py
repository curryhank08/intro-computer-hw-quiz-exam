"""  
author: H24111057 姚博瀚
"""
import random 

num = random.randint(97, 122)
guesses = []
n = 0

def print_histogram(guesses_list):
    
    histogram_list = [[0, i] for i in range(7)]
    for item in guesses_list:
        ord_string = ord(item)
        index = (ord_string - 97) // 4
        '''
        if (ord_string - 97) % 4 == 0:
            index -= 1
        '''
        histogram_list[index][0] += 1
    
    # debug use:
    # print(f"histogram_list; {histogram_list}")
    
    print()
    print("Guess Histogram:")
    for item in histogram_list:
        num, index = item[0], item[1]
        if index == 6:
            row = "%s - %s: %s" % (chr(121), chr(122), '*'*num)
        else:
            row = "%s - %s: %s" % (chr(97+4*index), chr(100+4*index), '*'*num)
        print(row)
    print()
    

while True:
    guess = str(input("Guess the lowercase alphabet: "))
    guesses.append(guess)
    n += 1
    while True:
        if 97 <= ord(guess) <= 122:
            if ord(guess) < num:
                guess = str(input("The alphabet you are looking for is alphabetically higher: "))
                guesses.append(guess)
                n += 1
            elif ord(guess) > num:
                guess = str(input("The alphabet you are looking for is alphabetically lower: "))
                guesses.append(guess)
                n += 1
            else:
                print(f"Congratulations! You guessed the number in {n} tries.")
                # degub use:
                # print(f"Previous guesses: {guesses}")
                
                print_histogram(guesses)
                end = True
                break
        else:
            guess = str(input("Invalid input. Guess again: "))
    if end:
        break
        