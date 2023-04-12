import sys
from queue import Queue

n, k = map(int, sys.stdin.readline().split())

Q = list((i + 1) for i in range(n))

sys.stdout.write('<')
idx = 0
now_size = n
for i in range(n - 1):
    idx = (idx + k - 1) % now_size
    sys.stdout.write(f'{Q[idx]}, ')
    Q.pop(idx)
    now_size -= 1
sys.stdout.write(f'{Q[0]}>')

