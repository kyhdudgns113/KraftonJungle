import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

isVisit = list(False for _ in range(n))
f = list(0 for _ in range(n))


def func(idx):
    global n, a, f
    if isVisit[idx]:
        return f[idx]

    isVisit[idx] = True

    temp_max = 0
    for j in range(idx + 1, n):
        fj = func(j)
        if a[idx] < a[j]:
            temp_max = max(temp_max, fj)
    f[idx] = temp_max + 1
    return f[idx]


func(0)
result = 0

for i in range(n):
    result = max(result, f[i])

print(result)
