def even_odd(*args):
    result = []
    filter_command = args[-1]
    party = 0 if filter_command == "even" else 1
    for index in range(len(args) - 1):
        number = args[index]
        if number % 2 == party:
            result.append(number)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))