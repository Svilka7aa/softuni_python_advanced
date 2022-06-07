# numbers = input().split(" ")
#
# reverse = numbers[::-1]
#
# print(" ".join(reverse))

numbers = input().split()

while numbers:
    last_number = numbers.pop()
    print(last_number, end=" ")
