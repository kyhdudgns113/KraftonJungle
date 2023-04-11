import sys

n = int(sys.stdin.readline())

stick = list(int(sys.stdin.readline()) for _ in range(n))

stack = list(0 for i in range(100002))
current_max = 0
can_see = 0
for i in range(n - 1, -1, -1):
    if current_max < stick[i]:
        current_max = stick[i]
        can_see += 1

print(can_see)
