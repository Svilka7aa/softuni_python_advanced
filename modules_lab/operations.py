def perform_operations(sign, *args):
    if sign == "+":
        return sum(args)

    elif sign == "*":
        result = 1
        for x in args:
            result *= x
        return result

    elif sign == "/":
        return args[0] / args[1]

    elif sign == "-":
        return args[0] - args[1]

    elif sign == "**":
        return args[0] ^ args[1]


