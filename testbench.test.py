def check_grade(num):
    if num % 4 != 0 or num < 0 or num > 100:
        return "suspicious"
    else:
        return "not suspicious"

grades = [66, 69, 96, 95, 73, 69, 28, 23, 67, 39, 31,]
for grade in grades:
    if check_grade(grade) == "suspicious":
        print(grade)
