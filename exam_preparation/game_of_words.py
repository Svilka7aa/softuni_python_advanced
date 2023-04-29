def move(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def outside_position(row, col, size):
    if row < 0:
        return 0, col
    if row >= size:
        return size - 1, col
    if col < 0:
        return row, 0
    if col >= size:
        return row, size - 1


string = input()
size = int(input())
field = []
player_row = 0
player_col = 0

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == "P":
            player_row, player_col = row, col
    field.append(row_elements)

number_of_commands = int(input())

for i in range(number_of_commands):
    direction = input()
    field[player_row][player_col] = "-"
    player_row, player_col = move(direction, player_row, player_col)

    if is_outside(player_row, player_col, size):
        player_row, player_col = outside_position(player_row, player_col, size)
        string = string[:-1]

    if field[player_row][player_col] != "-":
        string += field[player_row][player_col]

    field[player_row][player_col] = "P"

print(string)
for row in field:
    print("".join(row), sep="")
# Hello
# 4
# P---
# Mark
# -l-y
# --e-
# 4
# down
# right
# right
# right


# Initial
# 5
# -----
# t-r--
# --Pa-
# --S--
# z--t-
# 4
# up
# left
# left
# left