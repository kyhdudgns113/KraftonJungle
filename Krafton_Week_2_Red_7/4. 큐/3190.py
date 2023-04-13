import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]


isApple = list(list(0 for _ in range(101)) for __ in range(101))
isDummy = list(list(0 for _ in range(101)) for __ in range(101))

Q = deque()

for _ in range(k):
    row, col = map(int, sys.stdin.readline().split())
    isApple[row][col] = 1

L = int(sys.stdin.readline())
xc = list([0, 0] for _ in range(L))

for i in range(L):
    x, c = sys.stdin.readline().split()
    xc[i] = [int(x), c]
xc.sort()

idx_xc = 0
idx_direction = 0
elapsed_time = 0
now_row = now_col = 1
isDummy[1][1] = 1
Q.appendleft([1, 1])
while True:
    elapsed_time += 1

    now_row = now_row + directions[idx_direction][0]
    now_col = now_col + directions[idx_direction][1]
    # sys.stdout.write(f'({now_row}, {now_col}) ')
    if now_row < 1 or now_row > n or now_col < 1 or now_col > n:
        break

    if isDummy[now_row][now_col] == 1:
        break

    Q.appendleft([now_row, now_col])
    isDummy[now_row][now_col] = 1
    if isApple[now_row][now_col] == 0:
        popped = Q.pop()
        isDummy[popped[0]][popped[1]] = 0

    if idx_xc < len(xc) and xc[idx_xc][0] == elapsed_time:
        if xc[idx_xc][1] == 'L':
            idx_direction = (idx_direction + 1) % 4
        else:
            idx_direction = (idx_direction - 1) % 4
        idx_xc += 1
    # for q in Q:
        # sys.stdout.write(f' ({q[0]},{q[1]})')
    # print()
print(elapsed_time)
# print(isDummy[1][1])
