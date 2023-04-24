def find_count(board, row, col):
    moves = [
        [row, col + 1],
        [row, col - 1],
        [row - 1, col],
        [row + 1, col],
        [row - 1, col - 1],
        [row + 1, col + 1],
        [row + 1, col - 1],
        [row - 1, col + 1]
    ]
    result = 0
    for r, c in moves:
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == "K":
            result += 1

    return result

size = 8
board = [input().split() for i in range(size)]

print(find_count(board, row, col))

for row in board:
     print(row, sep="")
