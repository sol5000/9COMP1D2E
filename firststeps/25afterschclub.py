first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
gender = input("Enter your gender: ")
grade_level = input("Enter your grade level: ")

with open("file.txt", "w") as f:
    f.write(f"First Name: {first_name}\n")
    f.write(f"Last Name: {last_name}\n")
    f.write(f"Gender: {gender}\n")
    f.write(f"Grade Level: {grade_level}\n")

print("Information saved. tHanks.")
