from collections import deque

def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list


eggs_size_list = deque([int(x) for x in input().split(", ")])
paper_size_list = [int(x) for x in input().split(", ")]
box_size = 50
boxes_count = 0

while eggs_size_list and paper_size_list:
    current_egg = eggs_size_list.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        paper_size_list = swapList(paper_size_list)
        continue

    current_paper = paper_size_list.pop()
    current_sum = current_egg + current_paper

    if current_sum <= 50:
        boxes_count += 1
    else:
        continue

if boxes_count > 0:
    print(f"Great! You filled {boxes_count} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_size_list:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_size_list])}")
if paper_size_list:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_size_list])}")


