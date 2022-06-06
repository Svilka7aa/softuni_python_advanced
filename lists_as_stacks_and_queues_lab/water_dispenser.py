from collections import deque

people = deque()
watter_quantity = int(input())
while True:
    command = input()
    if command == "Start":
        break

    people.append(command)

while True:
    command = input()
    if command == "End":
        break
    elif command.startswith("refill "):
        params = command.split(" ")
        watter_quantity += int(params[1])
    else:
        person = people.popleft()
        water_wanted = int(command)

        if water_wanted <= watter_quantity:
            print(f"{person} got water")
            watter_quantity -= water_wanted
        else:
            print(f"{person} must wait")

print(f"{watter_quantity} liters left")
