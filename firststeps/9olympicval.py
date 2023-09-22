while True:
    value = input("Please name one of the Olympic Values: ")
    if value.lower() in ['respect', 'excellence', 'friendship']:
        print("That's correct")
        break
    else:
        print("Try again")