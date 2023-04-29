from collections import deque

seats = input().split(", ")
first_line = deque(int(x) for x in input().split(', '))
second_line = deque(int(x) for x in input().split(", "))
possible_seat = []
seat_matches = []
rotations_count = 0

while first_line and second_line:
    current_firs_num = first_line.popleft()
    current_second_num = second_line.pop()
    current_sum = current_firs_num + current_second_num
    rotations_count += 1

    current_char = chr(current_sum)
    if current_char.isalpha() == False:
        first_line.append(current_firs_num)
        second_line.appendleft(current_second_num)

    for i in seats:
        if current_char == i[-1]:
            possible_seat.append(i)

    for s in possible_seat:
        if str(current_firs_num) + current_char == s or \
           str(current_second_num) + current_char == s:
            if s not in seat_matches:
                seat_matches.append(s)
            elif s in seat_matches:
                first_line.append(current_firs_num)
                second_line.appendleft(current_second_num)

        else:
            first_line.append(current_firs_num)
            second_line.appendleft(current_second_num)

    if len(seat_matches) == 3 or rotations_count == 10:
        break


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations_count}")




