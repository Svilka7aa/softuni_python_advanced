def get_player_position(matrix, player):
    for row_idx, row in enumerate(matrix):
        if player in row:
            return (row_idx, row.index(player))

    return (None, None)


def get_chess_position(row, col):
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    col_names = ["a", "b", "c", "d", "e", "f", "g", "h"]
    return row_names[row], col_names[col]


size = 8
matrix = [input().split(" ") for _ in range(size)]

current_player = "w"
other_player = "b"

current_player_position = get_player_position(matrix, "w")
other_player_position = get_player_position(matrix, "b")

current_delta = -1
other_delta = 1

is_capture = False
is_queen = False

while not is_capture and not is_queen:
    (current_player_row, current_player_col) = current_player_position
    (other_player_row, other_player_col) = other_player_position

    current_player_row += current_delta
    current_player_position = current_player_row, current_player_col

    if current_player_row == other_player_row and abs(current_player_col - other_player_col) == 1:
        is_capture = True
        break
    elif current_player_row in (0, size - 1):
        is_queen = True

    else:
        current_player_position, other_player_position = other_player_position, current_player_position
        current_delta, other_delta = other_player, current_delta
        current_player, other_player = other_player, current_player

player = "White" if current_player == "w" else "Black"
row_name, col_name = get_chess_position(*current_player_position)
position_name = f"{col_name}{row_name}"

if is_capture:
    print(f"Game over! {player} win, capture on {position_name}.")
if is_queen:
    print(f"Game over! {player} pawn is promoted to a queen at {position_name}.")
