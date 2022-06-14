def get_primary_diagonal(matrix):
    # the_sum = 0
    # n = len(matrix)
    # for i in range(n):
    #     the_sum += matrix[i][i]
    # return the_sum
    # good example of comprehension

    return sum(matrix[i][i] for i in range(n))


# def get_secondary_diagonal(matrix):
#     n = len(matrix)
#     return sum(matrix[i][n - i - 1] for i in range(n))


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split()]
    )

print(get_primary_diagonal(matrix))
# print(get_secondary_diagonal(matrix))
