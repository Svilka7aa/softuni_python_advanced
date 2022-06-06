original_string = input()

s = []
for i in original_string:
    s.append(i)

reversed_string = ""

while s:
    reversed_string += s.pop()

print(reversed_string)
