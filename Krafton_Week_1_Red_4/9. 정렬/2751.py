import sys


def merge_sort(num_list):
    len_list = len(num_list)

    if len_list == 1:
        return

    left_list = num_list[0:len_list // 2]
    right_list = num_list[len_list // 2:len_list]

    idx_left = 0
    idx_right = 0
    idx_num = 0

    merge_sort(left_list)
    merge_sort(right_list)

    while idx_left < len(left_list) and idx_right < len(right_list):
        if left_list[idx_left] > right_list[idx_right]:
            num_list[idx_num] = right_list[idx_right]
            idx_right += 1
        else:
            num_list[idx_num] = left_list[idx_left]
            idx_left += 1
        idx_num += 1

    while idx_left < len(left_list):
        num_list[idx_num] = left_list[idx_left]
        idx_num += 1
        idx_left += 1

    while idx_right < len(right_list):
        num_list[idx_num] = right_list[idx_right]
        idx_num += 1
        idx_right += 1


n = int(sys.stdin.readline())

num_list = list(int(sys.stdin.readline()) for i in range(n))

merge_sort(num_list)

for num in num_list:
    print(num)