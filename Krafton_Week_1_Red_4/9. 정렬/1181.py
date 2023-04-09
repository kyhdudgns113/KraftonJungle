import sys

n = int(sys.stdin.readline())

str_list = []

for _ in range(n):
    inp = sys.stdin.readline().strip()
    str_list.append(inp)

str_list.sort()
str_list.sort(key=len)

result_list = []

for strs in str_list:

    if not result_list or result_list[-1] != strs:
        result_list.append(strs)
        sys.stdout.write(strs + '\n')