size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []
for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - 1 - idx])

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")







