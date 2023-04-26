import sys

n = int(sys.stdin.readline())

stations_distance = list(map(int, sys.stdin.readline().split()))
oil_prices = list(map(int, sys.stdin.readline().split()))

stations = list(0 for i in range(n))
for i in range(1, n):
    stations[i] = stations[i - 1] + stations_distance[i - 1]

minimum_price = 0x7fffffff
result_cost = 0

for i in range(n - 1):
    minimum_price = min(minimum_price, oil_prices[i])
    result_cost += minimum_price * stations_distance[i]

print(result_cost)

