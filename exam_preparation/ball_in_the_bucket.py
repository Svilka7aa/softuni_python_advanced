def is_outside(size, row, col):
    return row < 0 or col < 0 or row >= size or col >= size


size = 6
field = [input().split(" ") for _ in range(size)]
points_collected = 0


for shot in range(3):
    row, col = eval(input())
    if is_outside(size, row, col) or field[row][col] != "B":
        pass
    else:
        field[row][col] = 0
        points = [x[col] for x in field]
        points_collected += sum(int(x) for x in points)

prize = None

if 100 <= points_collected < 200:
    prize = "Football"
elif 200 <= points_collected < 300:
    prize = "Teddy Bear"
elif 300 <= points_collected:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {points_collected} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - points_collected} points more to win a prize.")

