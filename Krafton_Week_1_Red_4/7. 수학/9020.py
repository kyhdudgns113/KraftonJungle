import sys, math, queue

prime_list = []

for i in range(2, 10001):
    isPrime = True
    for prime in prime_list:
        if i % prime == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(i)

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    for i in range(0, n//2):
        a = n//2 - i
        b = n//2 + i
        if a in prime_list and b in prime_list:
            print(str(a) + ' ' + str(b))
            break



