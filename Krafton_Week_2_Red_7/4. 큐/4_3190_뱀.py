from collections import deque
import sys

input = sys.stdin.readline

dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]

n = int(input())

isHere = list(list(0 for _ in range(101)) for _ in range(101))
isApple = list(list(0 for _ in range(101)) for _ in range(101))

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    isApple[a][b] = 1

l = int(input())
move = deque()
for _ in range(l):
    a, b = map(str, input().split())
    a = int(a)
    move.append([a, b])

dq = deque()
head = [1, 1]
dq.append(head)
isHere[1][1] = 1

idx = 0
cnt = 0
while True:
    a = head[0] + dir[idx][0]
    b = head[1] + dir[idx][1]
    head = [a, b]
    cnt += 1
    if 1 <= a <= n and \
            1 <= b <= n and \
            isHere[a][b] == 0:
        if isApple[a][b] == 1:
            dq.append(head)
            isHere[a][b] = 1
            isApple[a][b] = 0
        else:
            dq.append(head)
            isHere[a][b] = 1
            ret = dq.popleft()
            isHere[ret[0]][ret[1]] = 0
    else:
        break
    if len(move) > 0 and \
            move[0][0] == cnt:
        if move[0][1] == 'D':
            idx = (idx - 1) % 4
        else:
            idx = (idx + 1) % 4
        move.popleft()
print(cnt)
