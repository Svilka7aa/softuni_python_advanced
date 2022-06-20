sublist = input().split("|")
result = []

for el in range(len(sublist) - 1, -1, -1):
    current_elements = sublist[el].strip().split()
    result.extend(current_elements)

print(" ".join(result))