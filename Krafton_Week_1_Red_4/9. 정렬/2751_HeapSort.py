import sys

n = int(sys.stdin.readline())

num_list = list(int(sys.stdin.readline()) for i in range(n))


def heapify_top_bottom(arg_list, max_idx):
    now = 0
    while True:
        left = 2*now + 1
        right = 2*now + 2

        if right <= max_idx and arg_list[right] >= arg_list[left] and arg_list[right] > arg_list[now]:
            arg_list[now], arg_list[right] = arg_list[right], arg_list[now]
            now = right
        elif right <= max_idx and arg_list[left] >= arg_list[right] and arg_list[left] > arg_list[now] or \
            left <= max_idx and arg_list[left] > arg_list[now]:
            arg_list[now], arg_list[left] = arg_list[left], arg_list[now]
            now = left
        else:
            break


def heapify_insert(arg_list, idx):
    now = idx
    while now > 0:
        parent = (now - 1) // 2
        if arg_list[now] > arg_list[parent]:
            arg_list[now], arg_list[parent] = arg_list[parent], arg_list[now]
            now = parent
        else:
            break


def create_heap(arg_list):
    for i in range(len(arg_list)):
        heapify_insert(arg_list, i)


def heap_sort_min(arg_list):
    create_heap(arg_list)
    for i, num in enumerate(arg_list):
        last_idx = len(arg_list) - i - 1
        arg_list[0], arg_list[last_idx] = arg_list[last_idx], arg_list[0]
        heapify_top_bottom(arg_list, last_idx - 1)


heap_sort_min(num_list)

for num in num_list:
    sys.stdout.write(str(num) + '\n')

