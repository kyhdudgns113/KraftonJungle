import sys

a, b = map(int, sys.stdin.readline().split())

minimum_count = 0x7fffffff


def dfs(now, now_count):
    global minimum_count
    if now == b:
        minimum_count = min(minimum_count, now_count)

    if 2*now <= b:
        dfs(2*now, now_count + 1)
    if 10*now + 1 <= b:
        dfs(10*now + 1, now_count + 1)


dfs(a, 0)


if minimum_count == 0x7fffffff:
    print(-1)
else:
    print(minimum_count + 1)


