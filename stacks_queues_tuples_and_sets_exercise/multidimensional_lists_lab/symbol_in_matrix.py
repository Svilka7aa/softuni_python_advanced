def found_symbol(matrix, symbol):
    for row_index in range(n):
        for column_index in range(n):
            if matrix[row_index][column_index] == symbol:
                return row_index, column_index


n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

result = found_symbol(matrix, symbol)

if result:
    row_index, column_index = result
    print(f"({row_index}, {column_index})")
else:
    print(f"{symbol} does not occur in the matrix")
    