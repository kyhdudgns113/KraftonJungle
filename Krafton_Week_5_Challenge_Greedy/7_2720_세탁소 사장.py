import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c = int(sys.stdin.readline())

    coins = [0, 0, 0, 0]

    while c >= 25:
        c -= 25
        coins[0] += 1
    while c >= 10:
        c -= 10
        coins[1] += 1
    while c >= 5:
        c -= 5
        coins[2] += 1
    while c >= 1:
        c -= 1
        coins[3] += 1

    print(*coins)





