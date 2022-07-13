def move_snake(direction, row, col):
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
    position = burrows_positions[0] if territory[row][col] == burrows_positions[1] else burrows_positions[1]
    return position[0], position[1]


size = int(input())
territory = []
snake_row, snake_col = 0, 0
food_eaten = 0
burrows_positions = []

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == "S":
            snake_row, snake_col = row, col
        elif row_elements[col] == "B":
            burrows_positions.append([row, col])

    territory.append(row_elements)

direction = input()
while True:
    territory[snake_row][snake_col] = "."
    snake_row, snake_col = move_snake(direction, snake_row, snake_col)

    if is_outside(size, snake_row, snake_col):
        print("Game over!")
        break

    elif territory[snake_row][snake_col] == "*":
        food_eaten += 1

    elif territory[snake_row][snake_col] == "B":
        territory[snake_row][snake_col] = "."
        snake_row, snake_col = b_condition(territory, snake_row, snake_col)

    territory[snake_row][snake_col] = "S"

    if food_eaten == 10:
        print(f"You won! You fed the snake.")
        break

    direction = input()

print(f"Food eaten: {food_eaten}")
for row in territory:
    print(*row, sep="")
