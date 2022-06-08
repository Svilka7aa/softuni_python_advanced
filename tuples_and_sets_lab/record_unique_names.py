# Variant 1
# n = int(input())
# names = set()
# for name in range(n):
#     names.add(input())
#
# print("\n".join(names))

#VAriant 2
n = int(input())
names = {input() for _ in range(n)}
[print(name) for name in names]
