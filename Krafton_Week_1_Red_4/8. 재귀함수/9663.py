import sys

n = int(sys.stdin.readline())

result = 0
queen = [0] * n


def is_ok(x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x - i):
            return False

    return True


def set_queen(x):
    global result

    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            queen[x] = i
            if is_ok(x):
                set_queen(x + 1)


set_queen(0)
print(result)
