chocolate_squares = 16
people = 3

chocolates_per_person = chocolate_squares // people
chocolates_left_over = chocolate_squares % people

if chocolates_left_over == 0:
    print("and there will be no chocolates left over")
elif chocolates_left_over == 1:
    print("but there will be only 1 chocolate left over")
else:
    print("but there will be " + str(chocolates_left_over) + " chocolates left over")