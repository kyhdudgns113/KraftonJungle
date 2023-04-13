import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

sequence_length = list(1 for i in range(n))

for i in range(n - 2, -1, -1):
    temp_max = 1
    for j in range(i, n):
        if a[i] < a[j]:
            temp_max = max(temp_max, sequence_length[j] + 1)
    sequence_length[i] = temp_max

print(max(sequence_length))

