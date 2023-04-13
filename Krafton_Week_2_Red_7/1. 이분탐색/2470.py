import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

res_sum = 3333333333

res_left = 0
res_right = n - 1


def get_abs(ia, ib):
    global num_list
    return abs(num_list[ia] - num_list[ib])


def find_converge(pivot, start, end):
    global num_list, res_sum, res_left, res_right

    mid = (start + end) // 2
    abs_mid = abs(num_list[mid] + num_list[pivot])
    if abs_mid < res_sum:
        res_sum = abs_mid
        res_left = pivot
        res_right = mid

    if mid - 1 >= start and abs_mid > abs(num_list[mid - 1] + num_list[pivot]):
        find_converge(pivot, start, mid - 1)
    elif mid + 1 <= end and abs_mid > abs(num_list[mid + 1] + num_list[pivot]):
        find_converge(pivot, mid + 1, end)


for i in range(n - 1):
    find_converge(i, i + 1, n - 1)
print(f'{num_list[res_left]} {num_list[res_right]}')