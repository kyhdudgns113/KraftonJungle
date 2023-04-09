import sys


n = int(sys.stdin.readline())

points = []

for _ in range(n):
    ix, iy = map(int, sys.stdin.readline().split())
    points.append([ix, iy])

points.sort()

prev_point = points[0]

#   같은 점이 있을때의 처리
for i, point in enumerate(points):
    if i == 0:
        continue
    if prev_point == point:
        print(0)
        exit()
    else:
        prev_point = point


def find_max_y_same_x(x, mid, right):
    global points

    while True:
        if mid < right and points[mid + 1][0] == x:
            mid += 1
        else:
            break
    return mid


def find_point_idx_max(x, left, right):
    global points
    print(f'    {left}  {right}')
    mid = (left + right) // 2

    if x < points[left][0]:
        return None
    if x > points[right][0]:
        return None

    if left == right:
        return left

    if x < points[mid][0]:
        return find_point_idx_max(x, left, mid)

    if x == points[mid][0]:
        return find_max_y_same_x(x, mid, right)

    if x > points[mid][0]:
        return 1

    return 1


for i in range(0, 12, 2):

    idx = find_point_idx_max(i, 0, len(points) - 1)
    if idx is not None and idx < len(points):
        print(f'{i} is point[{idx}]={points[idx]}')
