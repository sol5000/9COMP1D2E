# Ask the user for the two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num2 // num1

remainder = num2 % num1

print(f"{num1} goes into {num2} {result} times with a remainder of {remainder}.")
