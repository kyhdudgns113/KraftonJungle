import sys

v, e = map(int, sys.stdin.readline().split())

abcs = []
for _ in range(e):
    abcs.append(list(map(int, sys.stdin.readline().split())))
abcs.sort(key=lambda x: x[2])

parent = list(i for i in range(v + 1))


def get_parent(idx):
    if parent[idx] == idx:
        return idx
    else:
        return get_parent(parent[idx])


result = 0
for a, b, c in abcs:
    ap = get_parent(a)
    bp = get_parent(b)
    if ap != bp:
        parent[bp] = ap
        result += c




