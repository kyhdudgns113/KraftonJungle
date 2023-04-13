import sys


def get_mid_area(h, left, right):
    mid = (left + right) // 2
    idx_left = mid
    idx_right = mid

    max_area = h[mid]
    temp_height = h[mid]

    #   왼쪽 오른쪽 중 높이가 더 큰곳으로 이동한다.
    #   그러면서 mid 를 경유하는 사각형의 최대 넓이를 구한다.
    while idx_left > left and idx_right < right:
        if h[idx_left - 1] <= h[idx_right + 1]:
            idx_right += 1
            temp_height = min(temp_height, h[idx_right])
            max_area = max(max_area, temp_height * (idx_right - idx_left + 1))
        else:
            idx_left -= 1
            temp_height = min(temp_height, h[idx_left])
            max_area = max(max_area, temp_height * (idx_right - idx_left + 1))

    while idx_left > left:
        idx_left -= 1
        temp_height = min(temp_height, h[idx_left])
        max_area = max(max_area, temp_height * (idx_right - idx_left + 1))

    while idx_right < right:
        idx_right += 1
        temp_height = min(temp_height, h[idx_right])
        max_area = max(max_area, temp_height * (idx_right - idx_left + 1))

    return max_area


def get_max_area(h, left, right):
    mid = (left + right) // 2

    if left == right:
        return h[left]

    left_area = get_max_area(h, left, mid)
    right_area = get_max_area(h, mid + 1, right)
    cross_mid_area = get_mid_area(h, left, right)

    return max(cross_mid_area, max(left_area, right_area))


while True:
    h = list(map(int, sys.stdin.readline().split()))
    n = h.pop(0)
    if n == 0:
        break

    print(get_max_area(h, 0, len(h) - 1))
