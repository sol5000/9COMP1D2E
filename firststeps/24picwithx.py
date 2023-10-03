def display_x(num1, num2):
    print(" " * num1 + "X" * num2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def draw_picture():
    display_x(10, 1)
    display_x(9, 3)
    display_x(8, 5)
    display_x(7, 7)
    display_x(6, 9)
    display_x(5, 11)
    display_x(4, 13)
    display_x(3, 15)
    display_x(2, 17)
    display_x(1, 19)
    display_x(0, 21)

draw_picture()
