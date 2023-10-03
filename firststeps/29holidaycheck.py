destination = input("What is the destination of your holiday? ")
num_things_to_pack = int(input("How many things do you need to pack? "))
num_tasks_to_complete = int(input("How many tasks do you need to complete to prepare? "))
things_to_pack = []
for i in range(num_things_to_pack):
    thing = input("Enter thing to pack: ")
    things_to_pack.append(thing)

tasks_to_complete = []
for i in range(num_tasks_to_complete):
    task = input("Enter task to complete: ")
    tasks_to_complete.append(task)

print("Destination:", destination)
print("Things to pack:", things_to_pack)
print("Tasks to complete:", tasks_to_complete)
