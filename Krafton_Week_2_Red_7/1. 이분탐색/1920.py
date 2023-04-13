import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))


def find_num_in_list(find_num, left, right):
    global a
    if left == right:
        if find_num == a[left]:
            return 1
        else:
            return 0
    mid = (left + right) // 2
    if find_num < a[mid]:
        return find_num_in_list(find_num, left, mid)
    elif find_num > a[mid]:
        return find_num_in_list(find_num, mid + 1, right)
    else:
        return 1


for check in check_list:
    res = find_num_in_list(check, 0, n - 1)
    sys.stdout.write(str(res) + '\n')

