def shopping_cart(*args):
    limits = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    products = {}
    result = ""
    for element in args:
        if element == "Stop":
            break
        group = element[0]
        product = element[1]
        if group not in products:
            products[group] = set()
        if len(products[group]) < limits[group]:
            products[group].add(product)

    if not products:
        result = "No products in the cart!"
        return result

    for key in limits:
        if key not in products:
            products[key] = ""

    for key in products:
        products[key] = sorted(products[key])

    products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in products:
        result += f"{key}:\n"
        if value:
            for element in value:
                result += f" - {element}\n"
    return result



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print("-" * 50)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print("-" * 50)

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

