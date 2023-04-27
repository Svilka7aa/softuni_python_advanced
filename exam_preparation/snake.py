def move(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col


def is_outside(size, row, col):
    return row < 0 or col < 0 or row >= size or col >= size


def b_condition(territory, row, col):
    position = burrows_position[0] if territory[row][col] == burrows_position[1] else burrows_position[1]
    return position[0], position[1]
#
#

size = int(input())

territory = []
current_row, current_col = 0, 0
food_eaten = 0
burrows_position = []

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == "S":
            current_row, current_col = row, col
        elif row_elements[col] == "B":
            burrows_position.append([row, col])

    territory.append(row_elements)

direction = input()

while True:
    territory[current_row][current_col] = "."
    current_row, current_col = move(direction, current_row, current_col)

    if is_outside(size, current_row, current_col):
        print("Game over!")
        break

    elif territory[current_row][current_col] == "*":
        food_eaten += 1

    elif territory[current_row][current_col] == "B":
        territory[current_row][current_col] = "."
        current_row, current_col = b_condition(territory, current_row, current_col)

    territory[current_row][current_col] = "S"

    if food_eaten == 10:
        print("You won! You fed the snake.")
        break



    direction = input()


print(f"Food eaten: {food_eaten}")
for row in territory:
    print("".join(row), sep="")