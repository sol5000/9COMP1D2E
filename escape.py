print("welcome to the escape room")
print("there is a monkey somewhere")
print("you have to enter the correct cage number to escape")
print("you have infinte tries")
print("good luck!")
def main():
    while True:
        print()
        print("There is a a box in front of you")
        ans = input("Do you want to open it? (yes/no): ")
        if ans == "yes":
            print("There is a monkey")
            break
        else:
            print()
            print("you gotta open it dude")
    while True:
        print()
        print("you see some cages")
        ans = input("which hole do you want to drop the monkey in? (1-14904): ")
        if ans == "9118":
            print("The cage unlocks."
                "you start pulling.")
            break
        else:
            for i in range(1, 4559):
                print("look who is stuck in here forever")
                print("hint: the number of lines just printed is the answer")
    while True:
        push = input("pull the cage door more? ")
        if push == "yes":
            return False
        else:
            return True
    print("you got out...")
main()




