from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0


while females and males:
    current_female = females.popleft()
    current_male = males.pop()

    if current_female <= 0:
        males.append(current_male)
        continue

    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue

    if current_female != current_male:
        males.append(current_male - 2)

    elif current_female == current_male:
        matches += 1

print(f"Matches: {matches}")
if males:
    males_left = reversed(males)
    print(f"Males left: {', '.join(str(x) for x in males_left)}")
else:
    print(f"Males left: none")
if females:
    print(f'Females left: {", ".join(str(x) for x in females)}')
else:
    print("Females left: none")

