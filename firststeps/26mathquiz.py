name = input("Please enter your name: ")

# QUESTION 1
num1 = 5
num2 = 7
answer1 = num1 + num2
guess1 = int(input(f"{name}, what is {num1} + {num2}? "))
if guess1 == answer1:
    print("Correct!")
    score = 1
else:
    print("Incorrect.")
    score = 0

# QUESTION 2
num3 = 10
num4 = 3
answer2 = num3 - num4
guess2 = int(input(f"{name}, what is {num3} - {num4}? "))
if guess2 == answer2:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# QUESTION 3
num5 = 4
num6 = 6
answer3 = num5 * num6
guess3 = int(input(f"{name}, what is {num5} * {num6}? "))
if guess3 == answer3:
    print("Correct!")
    score += 1
else:
    print("Incorrect.")
