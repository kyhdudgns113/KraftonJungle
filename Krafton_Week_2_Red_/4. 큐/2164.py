from collections import deque
import sys

n = int(sys.stdin.readline())

Q = deque()

for i in range(n):
    Q.append(i + 1)

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())
print(Q.pop())
