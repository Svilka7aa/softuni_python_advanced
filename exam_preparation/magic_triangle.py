def get_magic_triangle(num):
    triangle = []

    for n in range(num):
        triangle.append([])
        triangle[n].append(1)
        for x in range(1, n):
            triangle[n].append(triangle[n - 1][x - 1] + triangle[n - 1][x])
        if n != 0:
            triangle[n].append(1)

    return triangle


get_magic_triangle(5)
