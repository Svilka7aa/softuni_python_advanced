from collections import deque


def delivery_func(items, inventory):
    to_deliver = []
    for item in items:
        to_deliver.append(item)

    for delivery in to_deliver:
        inventory.append(delivery)

    return inventory


def sell_func(items, inventory):
    to_sell = []
    for item in items:
        to_sell.append(item)

    if len(to_sell) == 0:
        inventory.remove(inventory[0])

    else:
        for sell in to_sell:
            if sell in inventory:
                while sell in inventory:
                    inventory.remove(sell)
            else:
                for _ in range(sell):
                    inventory.remove(inventory[0])

    return inventory


def stock_availability(*args):
    items = deque(args)
    inventory = list(items.popleft())
    command = items.popleft()

    if command == "delivery":
        inventory = delivery_func(items, inventory)

    elif command == "sell":
        inventory = sell_func(items, inventory)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))