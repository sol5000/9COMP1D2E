import math

numerator = float(input("Please enter the numerator: "))
denominator = float(input("Please enter the denominator: "))

rationalized = numerator * math.sqrt(denominator) / denominator

print("The rationalized denominator is:", rationalized)
