from collections import deque


def swap_paper(sizes):
    first = sizes.pop(0)
    last = sizes.pop(-1)

    sizes.insert(0, last)
    sizes.append(first)

    return sizes


eggs_sizes = deque(int(x) for x in input().split(", "))
paper_sizes = [int(x) for x in input().split(", ")]
box_size = 50
boxes_count = 0

while eggs_sizes and paper_sizes:
    current_egg = eggs_sizes.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        paper_sizes = swap_paper(paper_sizes)
        continue

    current_paper = paper_sizes.pop()
    current_sum = current_paper + current_egg

    if current_sum <= box_size:
        boxes_count += 1
    else:
        continue

if boxes_count:
    print(f"Great! You filled {boxes_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_sizes)}")

if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sizes)}")