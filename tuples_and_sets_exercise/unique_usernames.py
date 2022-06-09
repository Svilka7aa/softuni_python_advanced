number = int(input())
usernames_set = set()

for _ in range(number):
    username = input()
    usernames_set.add(username)

print("\n".join(usernames_set))
