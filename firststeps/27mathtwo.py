def add_score_to_file(name, score):
    with open("quiz_scores.txt", "a") as f:
        f.write(f"{name}: {score}/3\n")

def read_scores_from_file():
    with open("quiz_scores.txt", "r") as f:
        scores = f.readlines()
        for score in scores:
            print(score)

name = input("Please enter your name: ")

read_scores_from_file()

score = 0

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

print(f"{name}, your score is {score}/3")

with open("quiz_scores.txt", "r") as f:
    scores = f.readlines()
    for score_line in scores:
        if name in score_line:
            old_score = int(score_line.split(":")[1].split("/")[0])
            if score >= old_score:
                print(f"Congratulations {name}, you have beaten or matched your old high score of {old_score}!")
            else:
                print(f"Sorry {name}, you did not beat your old high score of {old_score}.")

add_score_to_file(name, score)
