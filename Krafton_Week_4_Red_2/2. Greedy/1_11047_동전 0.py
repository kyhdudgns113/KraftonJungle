import sys

n, k = map(int, sys.stdin.readline().split())

coins = list(int(sys.stdin.readline()) for _ in range(n))
coins.sort()
num_coins = 0

for i in range(n):
    while k >= coins[n - i - 1]:
        k -= coins[n - i - 1]
        num_coins += 1

print(num_coins)

