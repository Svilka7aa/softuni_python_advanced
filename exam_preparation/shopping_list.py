def shopping_list(budget, **kwargs):
    capacity = 5
    result = []
    if budget < 100:
        return "You do not have enough budget."

    for item, price in kwargs.items():
        current_price = price[0] * price[1]

        if capacity == 0:
            break
        if current_price >= budget:
            pass

        else:
            budget -= current_price
            capacity -= 1
            result.append(f"You bought {item} for {current_price:.2f} leva.")
    return "\n".join(result)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print("-" * 50)
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print("-" * 50)
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
