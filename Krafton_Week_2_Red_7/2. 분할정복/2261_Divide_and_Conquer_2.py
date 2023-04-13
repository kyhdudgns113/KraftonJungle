import sys


n = int(sys.stdin.readline())

points = list([] for _ in range(20005))

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points[x].append(y)

for i in range(20005):
    points[i].sort()

    if points[i]:
        prev = points[i][0]
        for j in range(1, len(points[i])):
            if prev == points[i][j]:
                print(0)
                exit()
            prev = points[i][j]


def find_left_point_index(x, left, right):
    global points
    mid = (left + right) // 2

    return 1


