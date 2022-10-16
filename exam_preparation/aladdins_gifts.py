from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
crafted_gifts = {}

while materials and magic:
    material = materials.pop()
    current_magic = magic.popleft()
    current_sum = material + current_magic
    current_gift = None

    if current_sum < 100:
        if current_sum % 2 == 0:
            material = material * 2
            current_magic = current_magic * 3
            current_sum = material + current_magic
        else:
            current_sum = current_sum * 2
    if current_sum >= 500:
        current_sum = (material / 2) + (current_magic / 2)

    if 100 <= current_sum < 200:
        current_gift = "Gemstone"
        if current_gift not in crafted_gifts:
            crafted_gifts[current_gift] = 1
        else:
            crafted_gifts[current_gift] += 1

    if 200 <= current_sum < 300:
        current_gift = "Porcelain Sculpture"
        if current_gift not in crafted_gifts:
            crafted_gifts[current_gift] = 1
        else:
            crafted_gifts[current_gift] += 1

    if 300 <= current_sum < 400:
        current_gift = "Gold"
        if current_gift not in crafted_gifts:
            crafted_gifts[current_gift] = 1
        else:
            crafted_gifts[current_gift] += 1

    if 400 <= current_sum < 500:
        current_gift = "Diamond Jewellery"
        if current_gift not in crafted_gifts:
            crafted_gifts[current_gift] = 1
        else:
            crafted_gifts[current_gift] += 1

if "Gemstone" in crafted_gifts and "Porcelain Sculpture" in crafted_gifts \
        or "Gold" in crafted_gifts and "Diamond Jewellery" in crafted_gifts:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in crafted_gifts.items():
    print(f"{key}: {value}")
