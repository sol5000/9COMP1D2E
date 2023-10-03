import math

def calculate_turf(length, width, radius):
    # Calculate the area of the rectangle
    rectangle_area = length * width
    
    # Calculate the area of the circle
    circle_area = math.pi * radius ** 2
    
    # Add the areas together to get the total turf needed
    total_turf = rectangle_area + circle_area
    
    return total_turf

length = float(input("What is the length of your lawn in meters? "))
width = float(input("What is the width of your lawn in meters? "))
radius = float(input("What is the radius of your circle in meters? "))

total_turf = calculate_turf(length, width, radius)

print("You will need", total_turf, "square meters of turf.")
