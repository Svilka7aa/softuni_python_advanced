file = open("./numbers.txt", "r")
sum_numbers = 0

for i in file:
    sum_numbers += int(i)

print(sum_numbers)

# print(sum([int(x) for x in file]))
