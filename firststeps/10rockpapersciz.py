import random

while True:
    user_wins = 0
    computer_wins = 0

    for i in range(3):
        user = input("Choose rock, paper, or scissors: ")
        computer = random.choice(['rock', 'paper', 'scissors'])
        print("You chose " + user + ", computer chose " + computer)

        result = {
            'rock': {'rock': 'Tie', 'paper': 'You lose!', 'scissors': 'You win!'},
            'paper': {'rock': 'You win!', 'paper': 'Tie', 'scissors': 'You lose!'},
            'scissors': {'rock': 'You lose!', 'paper': 'You win!', 'scissors': 'Tie'}
        }

        print(result[user][computer])

        if result[user][computer] == 'You win!':
            user_wins += 1
        elif result[user][computer] == 'You lose!':
            computer_wins += 1

    if user_wins > computer_wins:
        print("You won the best out of 3!")
    elif user_wins < computer_wins:
        print("Computer won the best out of 3!")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play another 3 rounds? (y/n): ")
    if play_again.lower() != 'y':
        break
