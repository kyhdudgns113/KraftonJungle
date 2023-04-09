import sys, math, queue


n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

prime_list = []

for i in range(2, 1001):
    isPrime = True
    for prime in prime_list:
        if i % prime == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(i)

print(len(list(1 for i in a if i in prime_list)))
