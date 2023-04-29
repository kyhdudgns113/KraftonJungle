import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

stack = []


def return_idx(val, left, right):
    global a

    mid = (left + right) // 2
    if left >= right:
        return left

    if val > stack[mid]:
        return return_idx(val, mid + 1, right)
    elif val < stack[mid]:
        return return_idx(val, left, mid)
    else:
        return mid


for i in range(n):
    idx = return_idx(a[i], 0, len(stack))
    if idx == len(stack):
        stack.append(a[i])
    else:
        stack[idx] = a[i]
print(len(stack))