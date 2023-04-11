from collections import deque


def switch_values(list):
    last = list[-1]
    list.appendleft(last)
    list.pop()
    return list


def best_list_pureness(*args):
    list_of_numbers = deque(args[0])
    rotations = args[1]
    rotation = 0
    pureness_dict = {}
    purity = 0

    while rotations >= rotation:
        pureness = 0
        for idx, value in enumerate(list_of_numbers):
            pureness += idx * value
        pureness_dict[rotation] = pureness
        rotation += 1

        list_of_numbers = switch_values(list_of_numbers)

    rotations_needed = []
    for key, value in pureness_dict.items():
        if value == max(pureness_dict.values()):
            purity = value
            rotations_needed.append(key)

    return f"Best pureness {purity} after {rotations_needed[0]} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

print("_" * 50)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

print("_" * 50)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)