import sys

n = int(sys.stdin.readline())

meetings = list([] for _ in range(n))
for i in range(n):
    meetings[i] = list(map(int, sys.stdin.readline().split()))
meetings.sort()

last_finished = -1
last_started = -2
result = 0
for i in range(n):
    if last_started == meetings[i][0] == meetings[i][1]:
        result += 1
    elif last_finished == meetings[i][0] == meetings[i][1]:
        result += 1
    elif last_started <= meetings[i][0] and meetings[i][1] <= last_finished:
        last_started = meetings[i][0]
        last_finished = meetings[i][1]
    elif last_finished <= meetings[i][0]:
        last_started = meetings[i][0]
        last_finished = meetings[i][1]
        result += 1
print(result)


