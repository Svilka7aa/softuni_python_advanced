from collections import deque

pizza = deque(int(p) for p in input().split(", "))
employees = [int(e) for e in input().split(", ")]
pizza_made = 0

while pizza and employees:
    current_pizza = pizza.popleft()
    if current_pizza > 10 or current_pizza <= 0:
        continue

    current_employee = employees.pop()

    if current_employee >= current_pizza:
        pizza_made += current_pizza

    elif current_employee < current_pizza:
        pizza_made += current_employee
        current_pizza -= current_employee
        pizza.appendleft(current_pizza)

if not pizza:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizza_made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")

else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza)}")