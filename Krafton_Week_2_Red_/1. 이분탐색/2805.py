import sys

n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))
tree.sort()


def cut_tree(height):
    ret = 0
    for i in range(n):
        if tree[n - i - 1] <= height:
            break
        ret += tree[n - i - 1] - height
    return ret


def find_height(low, high):
    global n, tree
    mid = (low + high) // 2

    if low >= high:
        return mid

    if low + 1 == high:
        crop_low = cut_tree(high)
        if crop_low >= m:
            return high
        else:
            return low

    crop_mid = cut_tree(mid)

    if crop_mid < m:
        return find_height(low, mid - 1)
    elif crop_mid > m:
        return find_height(mid, high)
    else:
        return mid


res = find_height(0, 1000000001)

print(res)
