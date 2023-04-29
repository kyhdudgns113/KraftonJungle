import sys

s = list(sys.stdin.readline().strip())

num_0 = 0
num_1 = 0
now = 'a'

for c in s:
    if c == '0' and c != now:
        now = c
        num_0 += 1
    elif c == '1' and c != now:
        now = c
        num_1 += 1

print(min(num_0, num_1))


