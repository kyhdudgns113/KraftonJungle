import sys

n = int(sys.stdin.readline())
w = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
result_minimum = list(list(0x7fffffff for _ in range(n)) for _ in range(1 << n))

result_minimum[1][0] = 0

for bit in range(1 << n):
    for now_node in range(n):
        if bit & (1 << now_node):
            for next_node in range(n):
                if now_node != next_node and not (bit & (1 << next_node)) and w[now_node][next_node]:
                    result_minimum[bit | (1 << next_node)][next_node] = min(
                        result_minimum[bit | (1 << next_node)][next_node],
                        result_minimum[bit][now_node] + w[now_node][next_node]
                    )
result_value = 0x7fffffff
for i in range(n):
    result_value = min(
        result_value,
        result_minimum[(1 << n) - 1][i] + result_minimum[i][0]
    )

print(result_value)

