import sys

n = int(sys.stdin.readline())

sequence = list(int(sys.stdin.readline()) for _ in range(n))
sequence.sort()

result = 0

i = 0
while i < n:
    if sequence[i] < 0:
        if i < n - 1 and sequence[i + 1] <= 0:
            result += sequence[i]*sequence[i + 1]
            i += 2
        else:
            result += sequence[i]
            i += 1
    else:
        break

i = n - 1
while i >= 0:
    if sequence[i] > 0:
        if i > 0 and sequence[i - 1] > 1:
            result += sequence[i]*sequence[i - 1]
            i -= 2
        else:
            result += sequence[i]
            i -= 1
    else:
        break
print(result)


