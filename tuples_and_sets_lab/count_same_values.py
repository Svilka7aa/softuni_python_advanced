numbers_string = input()

occurrence_count = {}
numbers = [float(x) for x in numbers_string.split(" ")]

for number in numbers:
    if number not in occurrence_count:
        occurrence_count[number] = 0
    occurrence_count[number] += 1

for number, count in occurrence_count.items():
    print(f"{number} - {count} times")
