import sys

n = int(sys.stdin.readline())

w = list(list(map(int, sys.stdin.readline().split())) for i in range(n))

isVisit = list(0 for _ in range(n))

result_val = 9999999999


# now_idx 에서 출발한다.
# 갈 수 있는 모든 지점을 다 돈다.
def func(start_idx, now_idx, remain, val):
    global isVisit, n, result_val

    if remain == 1:
        if w[now_idx][start_idx]:
            result_val = min(result_val, val + w[now_idx][start_idx])

        return

    isVisit[now_idx] = 1

    for i in range(n):
        if isVisit[i] == 0 and w[now_idx][i] > 0:
            func(start_idx, i, remain - 1, val + w[now_idx][i])
    isVisit[now_idx] = 0


for i in range(n):
    func(i, i, n, 0)

print(result_val)