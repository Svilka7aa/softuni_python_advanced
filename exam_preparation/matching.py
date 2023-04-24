from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    male = males.pop()
    if male <= 0:
        continue
    elif male % 25 == 0:
        males.pop()
        continue
    female = females.popleft()
    if female <= 0:
        males.append(male)
        continue
    elif female % 25 == 0:
        females.popleft()
        continue

    if male == female:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}")
if len(males) == 0:
    males.append("none")
print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
if len(females) == 0:
    females.append("none")
print(f"Females left: {', '.join(str(x) for x in females)}")
