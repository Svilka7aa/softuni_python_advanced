from collections import deque

bowls_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while customers:
    if len(bowls_ramen) == 0:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join([str(x) for x in customers])}")
        break

    current_customer = customers[0]
    current_ramen = bowls_ramen[-1]

    if current_customer >= current_ramen:
        current_customer -= current_ramen
        bowls_ramen.pop()
        customers[0] -= current_ramen
        if customers[0] == 0:
            customers.popleft()
    else:
        current_ramen -= current_customer
        customers.popleft()
        bowls_ramen[-1] -= current_customer

    if len(customers) == 0:
        print("Great job! You served all the customers.")
        if len(bowls_ramen) != 0:
            print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_ramen])}")
