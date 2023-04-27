def move(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def reposition(row, col, rows, cols):
    if row < 0:
        return rows - 1, col
    if row >= rows:
        return 0, col
    if col < 0:
        return row, cols - 1
    if col >= cols:
        return row, 0


rows, cols = [int(x) for x in input().split(", ")]
workshop = []
santa_row, santa_col = 0, 0
decorations = 0
gifts = 0
cookies = 0
items = 0
christmas = False

for row in range(rows):
    row_elements = input().split()
    for col in range(cols):
        if row_elements[col] == "Y":
            santa_row, santa_col = row, col
        elif row_elements[col] == "D" or row_elements[col] == "G" or row_elements[col] == "C":
            items += 1
    workshop.append(row_elements)

command = input()

while True:
    if command == "End" or command == " ":
        break

    command_parts = command.split("-")
    direction = command_parts[0]
    steps = int(command_parts[1])

    for step in range(steps):
        workshop[santa_row][santa_col] = "x"
        santa_row, santa_col = move(direction, santa_row, santa_col)

        if is_outside(santa_row, santa_col, rows, cols):
            santa_row, santa_col = reposition(santa_row, santa_col, rows, cols)

        if workshop[santa_row][santa_col] == "D":
            decorations += 1
            items -= 1

        elif workshop[santa_row][santa_col] == "C":
            cookies += 1
            items -= 1

        elif workshop[santa_row][santa_col] == "G":
            gifts += 1
            items -= 1

        workshop[santa_row][santa_col] = "Y"

        if items == 0:
            print("Merry Christmas!")
            christmas = True
            break

    if christmas:
        break

    command = input()

print(f"You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for row in workshop:
    print(" ".join(row), sep=" ")


