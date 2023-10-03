import random

names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

random_name = random.choice(names)

print("The random name is:", random_name)
