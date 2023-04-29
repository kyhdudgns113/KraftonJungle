import sys

n = int(sys.stdin.readline())

dp_end_00 = list(0 for _ in range(n + 5))
dp_end_1 = list(0 for _ in range(n + 5))

dp_end_00[2] = 1
dp_end_1[1] = 1

for i in range(n + 1):
    dp_end_1[i + 1] += dp_end_00[i] + dp_end_1[i]
    dp_end_00[i + 2] += dp_end_00[i] + dp_end_1[i]
    dp_end_00[i + 1] %= 15746
    dp_end_00[i + 2] %= 15746

print((dp_end_00[n] + dp_end_1[n]) % 15746)


