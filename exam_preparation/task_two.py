# player_one, player_two = input().split(", ")
# current_player = ""
# next_player = ""
# size = 6
# maze = []
# turns_counter = 1
#
#
# for row in range(size):
#     row_elements = list(input().split())
#     maze.append(row_elements)
#
# coordinates = eval(input())
# while True:
#     row, col = coordinates
#     if turns_counter % 2 != 0:
#         current_player = player_one
#         next_player = player_two
#     else:
#         current_player = player_two
#         next_player = player_one
#
#     if maze[row][col] == "E":
#         print(f"{current_player} found the Exit and wins the game!")
#         break
#     elif maze[row][col] == "T":
#         print(f"{current_player} is out of the game! The winner is {next_player}.")
#         break
#     elif maze[row][col] == "W":
#         print(f"{current_player} hits a wall and needs to rest.")
#
#     turns_counter += 1
#     coordinates = eval(input())


def player_turn(current_player):
    next_player = ""
    other_player = ""
    if current_player == "Tom":
        next_player = "Jerry"
        other_player = "Tom"
    elif current_player == "Jerry":
        next_player = "Tom"
        other_player = "Jerry"

    return next_player, other_player


players_order = input().split(", ")
current_player = players_order[1]
other_player = players_order[0]
matrix = []
resting_player = []

for i in range(6):
    line = input().split(" ")
    matrix.append(line)

while True:
    current_player, other_player = player_turn(current_player)
    coordinates = input().split(", ")
    i = int(coordinates[0][1])
    j = int(coordinates[1][0])

    if current_player in resting_player:
        resting_player.remove(current_player)
        continue

    if matrix[i][j] == "W":
        resting_player.append(current_player)
        print(f"{current_player} hits a wall and needs to rest.")
    elif matrix[i][j] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[i][j] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break