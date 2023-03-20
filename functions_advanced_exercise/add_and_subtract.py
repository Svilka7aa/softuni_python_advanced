def sum_of_numbers(a, b):
    return a + b


def subtract(current_num, c):
    return current_num - c


a, b, c = int(input()), int(input()), int(input())
result = subtract(sum_of_numbers(a, b), c)
print(result)
