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


def reposition(row, col, size):
    if row < 0:
        return size - 1, col
    if row >= size:
        return 0, col
    if col < 0:
        return row, size - 1
    if col >= size:
        return row, 0


size = int(input())
matrix = []
path = []
current_row, current_col = 0, 0
coins_collected = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "P":
            current_row, current_col = row, col
            path.append([row, col])
    matrix.append(row_elements)

direction = input()

while True:
    matrix[current_row][current_col] = 0
    current_row, current_col = move(direction, current_row, current_col)

    if is_outside(current_row, current_col, size):
        current_row, current_col = reposition(current_row, current_col, size)

    if matrix[current_row][current_col] == "X":
        print(f"Game over! You've collected {round(coins_collected / 2)} coins.")
        path.append([current_row, current_col])
        break

    coins_collected += int(matrix[current_row][current_col])
    path.append([current_row, current_col])

    if coins_collected >= 100:
        print(f"You won! You've collected {coins_collected} coins.")
        break

    direction = input()

print("Your path:")
for i in path:
    print(i)
