riddle = "What's black, and white, and read all over?"
acceptable_answers = ["newspaper", "an embarrassed zebra", "an angry mime"]

while True:
    user_answer = input(riddle + " ")
    if user_answer.lower() in acceptable_answers:
        print("you solved it")
        break
    print("incorrect try again")
1