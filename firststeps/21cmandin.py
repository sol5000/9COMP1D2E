num = float(input("Enter a number: "))

conversion_type = input("Convert to cm or inches? ")

if conversion_type.lower() == "cm":
    result = num * 2.54
    print(f"{num} inches is equal to {result} centimeters.")
elif conversion_type.lower() == "inches":
    result = num / 2.54
    print(f"{num} centimeters is equal to {result} inches.")
else:
    print("Invalid conversion type. Please enter 'cm' or 'inches'.")
