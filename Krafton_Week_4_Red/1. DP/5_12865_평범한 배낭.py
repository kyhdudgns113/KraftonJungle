import sys

n, k = map(int, sys.stdin.readline().split())

things = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

max_value = list(list(0 for _ in range(200005)) for _ in range(n))

for idx_things in range(n):
    now_weight = things[idx_things][0]
    now_value = things[idx_things][1]
    if idx_things == 0:
        max_value[idx_things][now_weight] = now_value
    else:
        for weight in range(k + 1):
            if weight < now_weight:
                max_value[idx_things][weight] = max_value[idx_things - 1][weight]
            else:
                max_value[idx_things][weight] = max(
                    max_value[idx_things - 1][weight],
                    max_value[idx_things - 1][weight - now_weight] + now_value
                )

result = 0
for weight in range(k + 1):
    result = max(result, max_value[n - 1][weight])

print(result)




