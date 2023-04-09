import sys

n = int(sys.stdin.readline())
num_list = list(int(sys.stdin.readline()) for i in range(n))


def quick_sort(left, right):
    global num_list

    pivot = left
    if left >= right:
        return

    idx_left = left + 1
    idx_right = right
    while idx_left <= idx_right:
        while idx_left <= idx_right and num_list[idx_left] < num_list[pivot]:
            idx_left += 1
        while idx_right >= idx_left and num_list[idx_right] > num_list[pivot]:
            idx_right -= 1
        if idx_left < idx_right:
            num_list[idx_left], num_list[idx_right] = num_list[idx_right], num_list[idx_left]

    if num_list[pivot] > num_list[idx_right]:
        num_list[pivot], num_list[idx_right] = num_list[idx_right], num_list[pivot]

    quick_sort(left, idx_right - 1)
    quick_sort(idx_right + 1, right)


quick_sort(0, n - 1)

for num in num_list:
    print(num)