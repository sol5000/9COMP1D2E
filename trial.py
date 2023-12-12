# Define the shield object
shield = {
    "x": 100,  # x-coordinate of the shield's position
    "y": 200,  # y-coordinate of the shield's position
    "width": 50,  # width of the shield
    "height": 50  # height of the shield
}

# Define the other object
other_object = {
    "x": 150,  # x-coordinate of the other object's position
    "y": 250,  # y-coordinate of the other object's position
    "width": 30,  # width of the other object
    "height": 30  # height of the other object
}

# Function to check for collisions
def check_collision(obj1, obj2):
    if (obj1["x"] < obj2["x"] + obj2["width"] and
        obj1["x"] + obj1["width"] > obj2["x"] and
        obj1["y"] < obj2["y"] + obj2["height"] and
        obj1["y"] + obj1["height"] > obj2["y"]):
        return True
    else:
        return False

# Check for collision between the shield and the other object
if check_collision(shield, other_object):
    print("Collision detected!")
else:
    print("No collision detected.")
