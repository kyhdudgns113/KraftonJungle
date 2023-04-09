import sys

x, y, w, h = map(int, sys.stdin.readline().split())

min_width = min(x, w - x)
min_height = min(y, h - y)

print(min(min_width, min_height))