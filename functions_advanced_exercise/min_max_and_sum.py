def min_max_sum(num):
    print(f"The minimum number is {min(num)}")
    print(f"The maximum number is {max(num)}")
    print(f"The sum number is: {sum(num)}")


numbers = list(map(int, input().split()))
min_max_sum(numbers)