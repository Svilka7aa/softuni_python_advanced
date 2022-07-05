from operations import perform_operations

problem = input().split()
x = float(problem[0])
y = float(problem[2])
sign = problem[1]

print(f"{perform_operations(sign, x, y):.2f}")