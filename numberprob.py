while True:
    try:
        num = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#  odd even no1
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# dec int no2
if num.is_integer():
    print("The number is an integer.")
else:
    print("The number is a decimal.")

# sq 3
if num >= 0 and int(num**0.5)**2 == int(num):
    print("The number is a square number.")
else:
    print("The number is not a square number.")

# tri 4
if ((8*num + 1)**0.5 - 1) % 2 == 0:
    print("The number is a triangle number.")
else:
    print("The number is not a triangle number.")

# Check if the number is prime
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number.")
