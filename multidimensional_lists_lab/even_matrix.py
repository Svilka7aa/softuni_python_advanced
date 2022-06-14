n = int(input())

result = []

for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    result.append(
        [x for x in row if x % 2 == 0]
    )
print(result)
