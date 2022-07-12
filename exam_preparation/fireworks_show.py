from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks_dict = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while firework_effects and explosive_power:
    current_firework = firework_effects.popleft()
    if current_firework <= 0:
        continue

    current_explosion = explosive_power.pop()
    if current_explosion <= 0:
        firework_effects.appendleft(current_firework)
        continue

    current_sum = current_firework + current_explosion

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        fireworks_dict["Palm Fireworks"] += 1

    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        fireworks_dict["Willow Fireworks"] += 1

    elif current_sum % 5 == 0 and current_sum % 3 == 0:
        fireworks_dict["Crossette Fireworks"] += 1

    else:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_power.append(current_explosion)

if all(value >= 3 for value in fireworks_dict.values()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, value in fireworks_dict.items():
    print(f"{key}: {value}")