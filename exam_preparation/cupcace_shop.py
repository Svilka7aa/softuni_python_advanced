from collections import deque


def delivery_func(items, inventory):
    for item in items:
        inventory.append(item)
    return inventory


def sell_func(items, inventory):
    to_sell = [x for x in items]
    if len(to_sell) == 0:
        inventory.remove(inventory[0])

    for sell in to_sell:
        if sell in inventory:
            while sell in inventory:
                inventory.remove(sell)
        if isinstance(sell, int):
            for _ in range(sell):
                inventory.remove(inventory[0])

    return inventory


def stock_availability(*args):
    items = deque(args)
    stock = list(items.popleft())
    action = items.popleft()

    if action == "delivery":
        stock = delivery_func(items, stock)

    elif action == "sell":
        stock = sell_func(items, stock)

    return stock


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))