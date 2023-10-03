def calculate_average_speed(distance, time):
    return distance / time

distance = float(input("Enter the distance in meters: "))
time = float(input("Enter the time in seconds: "))

average_speed = calculate_average_speed(distance, time)

print("The average speed is", average_speed, "m/s")
