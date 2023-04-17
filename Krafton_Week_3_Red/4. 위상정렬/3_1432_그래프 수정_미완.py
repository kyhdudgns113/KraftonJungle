from collections import deque
import sys

n = int(sys.stdin.readline())

matrix = list(list(sys.stdin.readline().strip()) for _ in range(n))
connection_list = list([] for _ in range(n + 1))

topology_list = []




