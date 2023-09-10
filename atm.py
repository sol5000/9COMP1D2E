balance = 43110
pin = "000000"
tries = 3
#i want to die

print("Welcome to the ATM.")
while tries > 0:
    entered_pin = input("Enter your 6-digit PIN: ")
    if entered_pin == pin:
        print("Welcome!")
        while True:
            try:
                withdrawal = int(input("How much would you like to withdraw? "))
            except ValueError:
                print("Please enter a valid amount.")
                continue

            if withdrawal > balance:
                print("Insufficient funds.")
            elif withdrawal % 10 != 0:
                print("Please enter an amount in multiples of 10.")
            else:
                notes = []
                for bill in [100, 50, 20, 10]:
                    while withdrawal >= bill:
                        notes.append(bill)
                        withdrawal -= bill
                balance -= sum(notes)
                print("Dispensing notes:", notes)
                print("Your new balance is:", balance)
                
                while True:
                    choice = input("Would you like to make another withdrawal? (y/n) ")
                    if choice.lower() == "y":
                        break
                    elif choice.lower() == "n":
                        print("see you again!")
                        exit()
                    else:
                        print("Invalid choice.")
                
                withdrawal = 0
    else:
        tries -= 1
        if tries == 0:
            print("Account locked.")
            break
        else:
            print(f"Incorrect PIN. {tries} tries left.")
            
