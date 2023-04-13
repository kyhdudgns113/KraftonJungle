import sys

a, b, c = map(int, sys.stdin.readline().split())
powered_array = []


def sol(a, b, c):
    global powered_array

    key = 1
    temp_val = a % c
    for i in range(33):
        powered_array.append([key, temp_val])
        key *= 2
        temp_val = (temp_val * temp_val) % c

    result = 1
    n = len(powered_array)
    for i in range(n):
        now_key = powered_array[n - i - 1][0]
        now_val = powered_array[n - i - 1][1]
        if b >= now_key:
            b -= now_key
            result = (result * now_val) % c
    return result


print(sol(a, b, c))
