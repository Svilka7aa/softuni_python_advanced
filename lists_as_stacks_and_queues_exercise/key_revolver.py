from collections import deque


bullet_price = int(input())
size_of_barrel = int(input())
bullets = [int(x) for x in input().split(" ")]
locks = deque([int(x) for x in input().split()])
value_of_intelligence = int(input())
bullets_counter = 0
bullets_shot = 0


for bullet in reversed(bullets):
    if bullet > locks[0]:
        print("Ping!")
        bullets.remove(bullet)
        bullets_counter += 1
        bullets_shot += 1

    else:
        print("Bang!")
        locks.popleft()
        bullets.remove(bullet)
        bullets_counter += 1
        bullets_shot += 1

    if bullets_counter == size_of_barrel and len(bullets) > 0:
        print("Reloading!")
        bullets_counter = 0

    if len(locks) == 0:
        print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence - (bullet_price * bullets_shot)}")
        break

    elif len(bullets) == 0 and len(locks) != 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
