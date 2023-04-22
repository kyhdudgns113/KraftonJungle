from queue import PriorityQueue, Queue
import sys

v, e = map(int, sys.stdin.readline().split())

connections_q = list(Queue() for _ in range(v + 1))

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    connections_q[a].put([b, c])

####################
#   Upper Tested   #
####################











