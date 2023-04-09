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

min_distance = 1600000000


def get_distance_square(idx_a, idx_b):
    global points
    return (points[idx_a][0] - points[idx_b][0])**2 + (points[idx_a][1] - points[idx_b][1])**2


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
    # print(f'    {left}  {right}')
    mid = (left + right) // 2

    if x < points[left][0] or x > points[right][0]:
        return None

    if left == right:
        return left

    if x < points[mid][0]:
        return find_point_idx_max(x, left, mid)
    elif x == points[mid][0]:
        return find_max_y_same_x(x, mid, right)
    else:
        if x >= points[mid + 1][0]:
            return find_point_idx_max(x, mid + 1, right)
        else:
            return mid


def find_min_y_same_x(x, mid, left):
    global points

    while True:
        if mid > left and points[mid - 1][0] == x:
            mid -= 1
        else:
            break
    return mid


def find_point_idx_min(x, left, right):
    global points
    # print(f'    {left}  {right}')
    mid = (left + right) // 2

    if x < points[left][0] or x > points[right][0]:
        return None

    if left == right:
        return left

    if x > points[mid][0]:
        return find_point_idx_min(x, mid + 1, right)
    elif x == points[mid][0]:
        return find_min_y_same_x(x, mid, left)
    else:
        if x <= points[mid - 1][0]:
            return find_point_idx_min(x, left, mid)
        else:
            return mid


# # Test for finding point idx
# for i in range(0, 14, 1):
#
#     idx = find_point_idx_min(i, 0, len(points) - 1)
#     if idx is not None and idx < len(points):
#         print(f'{i} is point[{idx}]={points[idx]}')


def get_min_distance(n_low, n_high):
    global points, min_distance
    n_mid = (n_low + n_high) // 2

    if n_low == n_high:
        idx_start = find_point_idx_min(n_low, 0, len(points) - 1)
        idx_end = find_point_idx_max(n_low, 0, len(points) - 1)
        if idx_start is not None:
            prev_val = points[0][1]
            temp_min_distance = 1600000000
            for i in range(idx_start + 1, idx_end + 1):
                temp_min_distance = min(temp_min_distance, points[i][1] - prev_val)
                prev_val = points[i][0]
            return temp_min_distance
        else:
            return None

    left_min = get_min_distance(n_low, n_mid)
    right_min = get_min_distance(n_mid + 1, n_high)
    cross_min = 0
    #
    #
    #   GKD_Master
    #   여기 짜야됨
    #
    #

    return 1
