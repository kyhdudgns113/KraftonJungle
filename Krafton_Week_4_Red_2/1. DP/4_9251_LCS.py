import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())

max_cnt = 0
max_len = list(list(0 for _ in range(1005)) for _ in range(1005))


for ia in range(1, len(a) + 1):
    for ib in range(1, len(b) + 1):
        if a[ia - 1] == b[ib - 1]:
            max_len[ia][ib] = max_len[ia - 1][ib - 1] + 1
        else:
            max_len[ia][ib] = max(max_len[ia - 1][ib], max_len[ia][ib - 1])


print(max_len[len(a)][len(b)])
