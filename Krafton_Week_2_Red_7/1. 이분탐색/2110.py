import sys

n, c = map(int, sys.stdin.readline().split())
x = list(int(sys.stdin.readline()) for i in range(n))
x.sort()


def is_settable(distance):
    global c, x
    remain_anchor = c - 1
    prev_position = x[0]

    for i in range(1, n):
        if x[i] - prev_position >= distance:
            remain_anchor -= 1
            prev_position = x[i]
        if remain_anchor == 0:
            break

    return not remain_anchor


def get_max_distance(low, high):
    global x
    mid = (low + high) // 2

    if low >= high or low + 1 == high:
        if is_settable(high):
            return high
        else:
            return low

    if is_settable(mid):
        return get_max_distance(mid, high)
    else:
        return get_max_distance(low, mid - 1)


res = get_max_distance(0, 1000000001)
print(res)

