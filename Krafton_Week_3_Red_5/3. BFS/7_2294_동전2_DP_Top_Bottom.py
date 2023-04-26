import sys
sys.setrecursionlimit(10**5)

n, k = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(n))
counts = list(0 for _ in range(k + 1))


def find_count(now_cost):

    if counts[now_cost] or not now_cost:
        return counts[now_cost]

    ret = 0x7fffffff

    for coin in coins:
        if now_cost > coin:
            ret = min(
                ret,
                find_count(now_cost - coin) + 1
            )
    counts[now_cost] = ret
    return ret


for coin in coins:
    if coin <= k:
        counts[coin] = 1

res = find_count(k)

if res > 10000:
    print(-1)
else:
    print(res)
