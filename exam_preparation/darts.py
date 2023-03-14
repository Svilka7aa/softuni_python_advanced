def score(matrix, row, col):
    result = 0
    if matrix[row][col] == "B":
        result = 501
    elif matrix[row][col] == "D":
        result += (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 2

    elif matrix[row][col] == "T":
        result += (int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][col]) + int(matrix[-1][col])) * 3

    else:
        result -= int(matrix[row][col])

    return result


size = 7
player_one, player_two = input().split(", ")
matrix = [input().split() for i in range(size)]

player_one_score = 501
player_two_score = 501
player = True
player_one_counter = 0
player_two_counter = 0
command = input()

while True:
    row, col = eval(command)
    if row >= size or col >= size or row < 0 or col < 0:
        if player:
            player = False
        elif not player:
            player = True

    elif player:
        player_one_score -= score(matrix, row, col)
        player_one_counter += 1
        player = False
    elif not player:
        player_two_score -= score(matrix, row, col)
        player_two_counter += 1
        player = True

    if player_one_score <= 0 or player_two_score <= 0:
        break

    command = input()

if player_one_score <= 0:
    print(f"{player_one} won the game with {player_one_counter} throws!")
elif player_two_score <= 0:
    print(f"{player_two} won the game with {player_two_counter} throws!")
