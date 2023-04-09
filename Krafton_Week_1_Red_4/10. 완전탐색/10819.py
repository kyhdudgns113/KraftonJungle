import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

isVisit = list(False for i in range(n))
res_sum = 0


def func(now_idx, remain, res):
    global res_sum, isVisit, a
    if remain == 1:
        res_sum = max(res_sum, res)
        return

    isVisit[now_idx] = True

    for i in range(n):
        if not isVisit[i]:
            func(i, remain - 1, res + abs(a[now_idx] - a[i]))

    isVisit[now_idx] = False


for i in range(n):
    func(i, n, 0)

print(res_sum)


