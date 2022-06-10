n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(x) for x in first_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    current_intersection = first.intersection(second)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}]"
      f" with length {len(longest_intersection)}")
