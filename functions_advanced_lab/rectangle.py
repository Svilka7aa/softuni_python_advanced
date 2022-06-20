def rectangle(length, width):
    def area():
        return length * width

    def parameter():
        return 2 * (length + width)

    if not isinstance(length, int) or not isinstance(width, int):
        return  "Enter valid values!"

    return f"""Rectangle area: {area()}
Rectangle perimeter: {parameter()}"""


print(rectangle(2, 10))
