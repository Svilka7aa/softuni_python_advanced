from collections import deque

jobs = deque(int(x) for x in input().split(", "))
index = int(input())
clock_cycles = 0
smallest_job = 1223423
job_to_do = jobs[index]

while job_to_do in jobs:
    for i in jobs:
        if i <= smallest_job:
            smallest_job = i
    clock_cycles += smallest_job
    jobs.remove(smallest_job)
    smallest_job = 3423423
print(clock_cycles)


