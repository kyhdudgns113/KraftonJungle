import sys

n, m = map(int, sys.stdin.readline().split())

is_small = list(0 for _ in range(n + 1))

for _ in range(m):
    is_small[int(sys.stdin.readline())] = 1

minimum_jump = list(list(0x7fffffff for _ in range(n + 1)) for _ in range(200))

if not is_small[2]:
    minimum_jump[1][2] = 1

for now_stone in range(2, n + 1):
    if is_small[now_stone]:
        continue
    for jump in range(1, min(199, n)):
        if jump > 1 and now_stone + jump - 1 <= n and not is_small[now_stone + jump - 1]:
            minimum_jump[jump - 1][now_stone + jump - 1] = min(
                minimum_jump[jump - 1][now_stone + jump - 1],
                minimum_jump[jump][now_stone] + 1
            )
        if jump + now_stone + 1 <= n and not is_small[now_stone + jump + 1]:
            minimum_jump[jump + 1][now_stone + jump + 1] = min(
                minimum_jump[jump + 1][now_stone + jump + 1],
                minimum_jump[jump][now_stone] + 1
            )
        if jump + now_stone <= n and not is_small[now_stone + jump]:
            minimum_jump[jump][now_stone + jump] = min(
                minimum_jump[jump][now_stone + jump],
                minimum_jump[jump][now_stone] + 1
            )
result = 0x7fffffff
for jump in range(1, 200):
    result = min(result, minimum_jump[jump][n])

if result != 0x7fffffff:
    print(result)
else:
    print(-1)