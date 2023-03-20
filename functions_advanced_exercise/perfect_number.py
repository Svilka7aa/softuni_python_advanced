def perfect_number(num):
    sum_of_dividers = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_dividers += i
            if sum_of_dividers == num:
                print("We have a perfect number!")
    if sum_of_dividers != num:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
