def get_magic_triangle(num_rows):
    result = []
    for n in range(num_rows):
        result.append([])
        result[n].append(1)
        for x in range(1, n):
            result[n].append(result[n - 1][x -1] + result[n - 1][x])
        if n != 0:
            result[n].append(1)

    return result


get_magic_triangle(5)