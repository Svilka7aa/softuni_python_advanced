def number_creator(mine_field, row, col):
    moves =[
        [row, col + 1],
        [row, col - 1],
        [row - 1, col],
        [row + 1, col],
        [row - 1, col - 1],
        [row + 1, col + 1],
        [row + 1, col - 1],
        [row - 1, col + 1]
    ]
    mines_count = 0
    for r, c in moves:
        if 0 <= r < len(mine_field) and 0 <= c < len(mine_field) and mine_field[r][c] == "*":
            mines_count += 1
    return mines_count

size = int(input())
mine_field = []

for row in range(size):
    mine_field.append([0 for x in range(size)])

number_mines = int(input())

for mine in range(number_mines):
    coordinates = eval(input())
    row, col = coordinates[0], coordinates[1]
    mine_field[row][col] = "*"


for row in range(size):
    for col in range(size):
        if mine_field[row][col] == "*":
            continue
        mine_field[row][col] = number_creator(mine_field, row, col)

for row in mine_field:
    print(*row, sep=" ")