import sys
from queue import Queue

n, k = map(int, sys.stdin.readline().split())

Q = Queue()

for i in range(n):
    Q.put(i + 1)

sys.stdout.write('<')
while Q.qsize() > 1:
    for _ in range(k - 1):
        Q.put(Q.get())
    sys.stdout.write(f'{Q.get()}, ')

sys.stdout.write(f'{Q.get()}>')
