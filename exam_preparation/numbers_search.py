
def numbers_searching(*args):
    duplicates = []
    numbers_without_duplicates = []

    for n in args:
        if n not in numbers_without_duplicates:
            numbers_without_duplicates.append(n)
        else:
            duplicates.append(n)

    a = sorted(numbers_without_duplicates)
    b = [x for x in range(a[0], a[-1] + 1)]
    a = set(a)
    missing_num = list(a ^ set(b))
    final_duplicate_list = []

    for d in duplicates:
        if d not in final_duplicate_list:
            final_duplicate_list.append(d)

    return [missing_num[0], sorted(final_duplicate_list)]

#
# print(numbers_searching(1, 2, 4, 2, 5, 4))
#
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

