size = 6
matrix = [input().split() for i in range(size)]
points = 0

for shot in range(3):
    command = eval(input())
    row, col = command
    if row >= size or col >= size or row < 0 or col < 0:
        pass
    elif matrix[row][col] == "B":
        matrix[row][col] = "0"
        result_list = [x[col] for x in matrix]
        bucket_sum = sum([int(x) for x in result_list])
        points += bucket_sum

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif points < 200:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
