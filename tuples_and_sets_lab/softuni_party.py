def is_vip(guest):
    return guest[0].isdigit()


n = int(input())
vip_guest = set()
regular_guests = set()

for _ in range(n):
    reservation = input()
    if is_vip(reservation):
        vip_guest.add(reservation)
    else:
        regular_guests.add(reservation)

while True:
    guest = input()
    if guest == "END":
        break
    if is_vip(guest):
        vip_guest.remove(guest)
    else:
        regular_guests.remove(guest)

print(len(vip_guest) + len(regular_guests))
[print(guest) for guest in sorted(vip_guest)]
[print(guest) for guest in sorted(regular_guests)]