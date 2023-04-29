def move(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col

size = 6
matrix = [input().split(" ") for _ in range(size)]
row, col = eval(input())
command = input()
while True:
    if command == "Stop":
        break
    command_parts = command.split(", ")
    action = command_parts[0]
    direction = command_parts[1]

    row, col = move(direction, row, col)

    if action == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."
    elif action == "Read":
        if matrix[row][col] != ".":
            print(matrix[row][col])

    elif action == "Create":
        value = command_parts[2]
        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif action == "Update":
        value = command_parts[2]
        if matrix[row][col] != ".":
            matrix[row][col] = value

    command = input()


for row in matrix:
    print(" ".join(row), sep="")