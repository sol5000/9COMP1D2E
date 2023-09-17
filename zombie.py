import random

def zombies_arrive():
    return random.randrange(40) + 11

def one_fight():
    if random.random() < 0.2:
        return "human"
    elif random.random() < 0.5:
        return "zombie"
    elif random.random() < 0.33:
        return "human"
    else:
        return "zombie"

def fight(food):
    result = one_fight()
    if result == "human":
        return "You fought bravely, but the zombies overwhelmed you. You died.", food
    elif result == "zombie":
        food -= 10
        return "You fought the zombies and survived, but you were injured in the process.", food
    else:
        food -= 10
        return "You fought the zombies and emerged victorious!", food

def run():
    if random.random() < 0.5:
        return "You tried to run, but the zombies caught you. You died.", 0
    else:
        return "You ran away from the zombies and escaped unharmed.", 0

def hide(food):
    if random.random() < 0.2:
        return "You hid from the zombies, but they found you. You died.", food
    else:
        food += 20
        return "You hid from the zombies and they passed you by.", food

def scavenge(food):
    if random.random() < 0.5:
        food += 30
        return "You found a stash of food and added it to your supplies.", food
    else:
        return "You searched for food but found nothing.", food

def play_game():
    health = 100
    zombies_left = 100
    food = 100
    while health > 0 and zombies_left > 0:
        zombies = zombies_arrive()
        print(f"Zombies have arrived! There are {zombies} zombies.")
        choice = input("What do you want to do? (fight/run/hide/scavenge) ")
        if choice == "fight":
            outcome, food = fight(food)
        elif choice == "run":
            outcome, food = run()
        elif choice == "hide":
            outcome, food = hide(food)
        elif choice == "scavenge":
            outcome, food = scavenge(food)
        else:
            print("Invalid choice. Try again.")
            continue
        print(outcome)
        if outcome == "You fought the zombies and emerged victorious!":
            zombies_left -= zombies
        elif outcome == "You fought the zombies and survived, but you were injured in the process.":
            zombies_left -= zombies
            health -= 20
        elif outcome in ["You tried to run, but the zombies caught you. You died.", "You hid from the zombies, but they found you. You died."]:
            health = 0
            break
        print(f"You have {health} health left, there are {zombies_left} zombies left, and you have {food} food left.")
    if health <= 0:
        print("You have died. Game over.")
        end_game()
    else:
        print("You have killed all the zombies. Congratulations, you win!")
        end_game()

def end_game():
    choice = input("Do you want to play again? (y/n) ")
    if choice == "y":
        play_game()
    else:
        print("Thanks for playing!")
play_game()

