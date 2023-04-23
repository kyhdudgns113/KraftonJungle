import sys

n = int(sys.stdin.readline())
w = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
result_minimum = list(list(0x7fffffff for _ in range(n)) for _ in range(1 << n))


def tsp(visited_bit, now_node):
    if visited_bit == (1 << n) - 1:
        return w[now_node][0] if w[now_node][0] else 0x7fffffff

    if result_minimum[visited_bit][now_node] != 0x7fffffff:
        return result_minimum[visited_bit][now_node]

    for next_node in range(n):
        if visited_bit & (1 << next_node) == 0 and w[now_node][next_node]:
            result_minimum[visited_bit][now_node] = min(
                result_minimum[visited_bit][now_node],
                tsp(visited_bit | (1 << next_node), next_node) + w[now_node][next_node]
            )

    return result_minimum[visited_bit][now_node]


print(tsp((1 << 0), 0))

